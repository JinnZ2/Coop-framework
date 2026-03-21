"""
Coop-framework: Toy network simulation

Models three interconnected dynamics:
  1. Trust propagation — Claude adoption spreads through co-op relationships
  2. Network growth — new co-ops form and connect over time
  3. Resource distribution — co-ops share surplus resources along trust links

Extensions (togglable):
  4. Bridge events — conferences that create cross-region connections
  5. Adoption decay — co-ops that see no network value may drop Claude
  6. Type affinity — same-type co-ops form stronger trust bonds
  7. Resource hub report — identifies most generous and most helped co-ops

Run:  python3 coop_sim.py
      python3 coop_sim.py --extended    (all extensions enabled)
"""

import random
import sys


class Coop:
    """A single cooperative in the network."""

    TYPES = {
        "food": {"trust_rate": 0.15, "resource_cap": 100, "label": "Food Co-op"},
        "grain": {"trust_rate": 0.12, "resource_cap": 150, "label": "Grain Elevator"},
        "electric": {"trust_rate": 0.10, "resource_cap": 200, "label": "Electric Co-op"},
        "credit": {"trust_rate": 0.08, "resource_cap": 300, "label": "Credit Union"},
        "worker": {"trust_rate": 0.18, "resource_cap": 80, "label": "Worker Co-op"},
    }

    # Type affinity: pairs that trust each other more (supply chain proximity)
    TYPE_AFFINITY = {
        frozenset({"food", "grain"}): 1.4,
        frozenset({"food", "worker"}): 1.3,
        frozenset({"grain", "electric"}): 1.2,
        frozenset({"electric", "credit"}): 1.1,
        frozenset({"worker", "credit"}): 1.2,
    }

    def __init__(self, name, coop_type, region, rng=None):
        spec = self.TYPES[coop_type]
        self.name = name
        self.coop_type = coop_type
        self.region = region
        self.trust_rate = spec["trust_rate"]
        self.resource_cap = spec["resource_cap"]
        rng = rng or random
        self.resources = rng.randint(20, spec["resource_cap"])
        self.adopted = False
        self.adoption_tick = None
        self.dropped_tick = None
        self.connections = []  # list of (other_coop, trust_strength)
        self.resources_given = 0
        self.resources_received = 0

    @classmethod
    def affinity(cls, type_a, type_b):
        """Return trust multiplier for two co-op types."""
        if type_a == type_b:
            return 1.5  # same type = strongest affinity
        return cls.TYPE_AFFINITY.get(frozenset({type_a, type_b}), 1.0)

    def __repr__(self):
        status = "ADOPTED" if self.adopted else "pending"
        return f"{self.name} ({self.TYPES[self.coop_type]['label']}, {self.region}) [{status}]"


class CoopNetwork:
    """The full cooperative network simulation."""

    REGIONS = ["Minnesota", "Wisconsin", "Vermont", "Oregon", "Appalachia", "Dakotas"]

    def __init__(self, seed=42, extensions=None):
        self.rng = random.Random(seed)
        self.tick = 0
        self.coops = []
        self.history = []
        self._name_counter = 0
        # Extensions: toggle optional dynamics
        self.ext = {
            "bridge_events": False,
            "adoption_decay": False,
            "type_affinity": False,
        }
        if extensions:
            self.ext.update(extensions)

    # --- Setup ---

    def generate_network(self, n=30):
        """Create an initial network of co-ops with random connections."""
        types = list(Coop.TYPES.keys())
        for _ in range(n):
            self._spawn_coop(self.rng.choice(types), self.rng.choice(self.REGIONS))

        # Wire up initial connections (supply chain relationships)
        for coop in self.coops:
            n_connections = self.rng.randint(1, 4)
            candidates = [c for c in self.coops if c is not coop and c not in [x[0] for x in coop.connections]]
            # prefer same-region connections, randomize within region groups
            tiebreakers = {id(c): self.rng.random() for c in candidates}
            candidates.sort(key=lambda c: (0 if c.region == coop.region else 1, tiebreakers[id(c)]))
            for partner in candidates[:n_connections]:
                trust = round(self.rng.uniform(0.1, 0.6), 2)
                if self.ext["type_affinity"]:
                    trust = round(min(trust * Coop.affinity(coop.coop_type, partner.coop_type), 0.95), 2)
                coop.connections.append((partner, trust))
                partner.connections.append((coop, trust))

    def seed_adoption(self, count=2):
        """Seed initial Claude adopters."""
        seeds = self.rng.sample(self.coops, count)
        for coop in seeds:
            coop.adopted = True
            coop.adoption_tick = 0

    # --- Simulation Steps ---

    def step(self):
        """Advance one tick: propagate trust, grow network, distribute resources, extensions."""
        self.tick += 1
        bridge = self._bridge_event() if self.ext["bridge_events"] else []
        adoptions = self._propagate_trust()
        decayed = self._adoption_decay() if self.ext["adoption_decay"] else []
        new_coops = self._grow_network()
        transfers = self._distribute_resources()
        snapshot = self._snapshot(adoptions, new_coops, transfers, bridge, decayed)
        self.history.append(snapshot)
        return snapshot

    def _propagate_trust(self):
        """Adopted co-ops may convince their connections to adopt."""
        newly_adopted = []
        adopters = [c for c in self.coops if c.adopted]
        for coop in adopters:
            for partner, trust in coop.connections:
                if partner.adopted:
                    continue
                # Probability = trust_strength * partner's trust_rate * network_effect * affinity
                network_bonus = 1 + 0.05 * sum(1 for c, _ in partner.connections if c.adopted)
                affinity = Coop.affinity(coop.coop_type, partner.coop_type) if self.ext["type_affinity"] else 1.0
                prob = trust * partner.trust_rate * network_bonus * affinity
                if self.rng.random() < prob:
                    partner.adopted = True
                    partner.adoption_tick = self.tick
                    newly_adopted.append(partner)
        return newly_adopted

    def _grow_network(self):
        """Occasionally spawn new co-ops drawn by existing network activity."""
        new_coops = []
        adopted_count = sum(1 for c in self.coops if c.adopted)
        # Growth chance scales with adoption density
        growth_chance = 0.05 + 0.02 * (adopted_count / max(len(self.coops), 1))
        if self.rng.random() < growth_chance:
            # New co-op appears near an adopted one
            adopted = [c for c in self.coops if c.adopted]
            if adopted:
                anchor = self.rng.choice(adopted)
                coop_type = self.rng.choice(list(Coop.TYPES.keys()))
                new_coop = self._spawn_coop(coop_type, anchor.region)
                # Connect to anchor and maybe one more neighbor
                trust = round(self.rng.uniform(0.2, 0.5), 2)
                new_coop.connections.append((anchor, trust))
                anchor.connections.append((new_coop, trust))
                new_coops.append(new_coop)
        return new_coops

    def _distribute_resources(self):
        """Co-ops share surplus resources along trust links."""
        transfers = []
        # Snapshot budgets so giving order doesn't create bias
        budgets = {id(c): c.resources for c in self.coops}
        for coop in self.coops:
            budget = budgets[id(coop)]
            if budget <= coop.resource_cap * 0.3:
                continue  # nothing to spare
            for partner, trust in coop.connections:
                if partner.resources < partner.resource_cap * 0.4:
                    # Share proportional to trust, based on start-of-tick budget
                    amount = int(budget * trust * 0.1)
                    if amount > 0 and coop.resources >= amount:
                        coop.resources -= amount
                        coop.resources_given += amount
                        partner.resources = min(partner.resources + amount, partner.resource_cap)
                        partner.resources_received += amount
                        transfers.append((coop.name, partner.name, amount))
        return transfers

    # --- Extensions ---

    def _bridge_event(self):
        """Simulate a conference/gathering that creates cross-region connections."""
        bridges = []
        # ~15% chance each tick of a regional conference
        if self.rng.random() > 0.15:
            return bridges
        # Pick 2 random regions to connect
        if len(self.REGIONS) < 2:
            return bridges
        r1, r2 = self.rng.sample(self.REGIONS, 2)
        pool1 = [c for c in self.coops if c.region == r1 and c.adopted]
        pool2 = [c for c in self.coops if c.region == r2]
        if not pool1 or not pool2:
            return bridges
        # 1-3 new cross-region connections form
        n_bridges = self.rng.randint(1, min(3, len(pool1), len(pool2)))
        for _ in range(n_bridges):
            a = self.rng.choice(pool1)
            b = self.rng.choice(pool2)
            # Skip if already connected
            if any(c is b for c, _ in a.connections):
                continue
            trust = round(self.rng.uniform(0.15, 0.4), 2)
            if self.ext["type_affinity"]:
                trust = round(min(trust * Coop.affinity(a.coop_type, b.coop_type), 0.95), 2)
            a.connections.append((b, trust))
            b.connections.append((a, trust))
            bridges.append((a.name, b.name, a.region, b.region))
        return bridges

    def _adoption_decay(self):
        """Co-ops that see no adopted neighbors may drop Claude."""
        decayed = []
        for coop in self.coops:
            if not coop.adopted or coop.adoption_tick == self.tick:
                continue
            # How many ticks since adoption?
            tenure = self.tick - coop.adoption_tick
            if tenure < 5:
                continue  # grace period
            adopted_neighbors = sum(1 for c, _ in coop.connections if c.adopted)
            total_neighbors = len(coop.connections)
            if total_neighbors == 0:
                isolation = 1.0
            else:
                isolation = 1 - (adopted_neighbors / total_neighbors)
            # Decay chance: high isolation + long tenure = more likely to drop
            decay_prob = isolation * 0.03
            if self.rng.random() < decay_prob:
                coop.adopted = False
                coop.dropped_tick = self.tick
                decayed.append(coop)
        return decayed

    # --- Helpers ---

    def _spawn_coop(self, coop_type, region):
        self._name_counter += 1
        name = f"{region[:3].upper()}-{coop_type[:2].upper()}{self._name_counter:03d}"
        coop = Coop(name, coop_type, region, rng=self.rng)
        self.coops.append(coop)
        return coop

    def _snapshot(self, adoptions, new_coops, transfers, bridges=None, decayed=None):
        total = len(self.coops)
        adopted = sum(1 for c in self.coops if c.adopted)
        avg_resources = sum(c.resources for c in self.coops) / max(total, 1)
        return {
            "tick": self.tick,
            "total_coops": total,
            "adopted": adopted,
            "adoption_pct": round(100 * adopted / total, 1),
            "new_adoptions": len(adoptions),
            "new_coops": len(new_coops),
            "resource_transfers": len(transfers),
            "avg_resources": round(avg_resources, 1),
            "bridges_formed": len(bridges) if bridges else 0,
            "decayed": len(decayed) if decayed else 0,
        }

    # --- Reporting ---

    def print_status(self):
        total = len(self.coops)
        adopted = sum(1 for c in self.coops if c.adopted)
        print(f"\n=== Tick {self.tick} | {adopted}/{total} adopted ({100*adopted/total:.0f}%) ===")

        regions = {}
        for c in self.coops:
            regions.setdefault(c.region, {"total": 0, "adopted": 0})
            regions[c.region]["total"] += 1
            if c.adopted:
                regions[c.region]["adopted"] += 1
        for region in sorted(regions):
            r = regions[region]
            bar_len = r["adopted"]
            bar = "#" * bar_len + "." * (r["total"] - bar_len)
            print(f"  {region:<12} [{bar}] {r['adopted']}/{r['total']}")
        if self.history:
            snap = self.history[-1]
            notes = []
            if snap.get("bridges_formed"):
                notes.append(f"{snap['bridges_formed']} bridge link(s)")
            if snap.get("decayed"):
                notes.append(f"{snap['decayed']} dropout(s)")
            if notes:
                print(f"  >> {', '.join(notes)}")

    def print_summary(self):
        print("\n" + "=" * 60)
        print("SIMULATION SUMMARY")
        print("=" * 60)
        print(f"  Duration:         {self.tick} ticks")
        print(f"  Final network:    {len(self.coops)} co-ops")
        adopted = sum(1 for c in self.coops if c.adopted)
        print(f"  Total adopted:    {adopted} ({100*adopted/len(self.coops):.0f}%)")
        total_transfers = sum(s["resource_transfers"] for s in self.history)
        print(f"  Resource shares:  {total_transfers} transfers")

        if adopted > 0:
            ticks = [c.adoption_tick for c in self.coops if c.adopted and c.adoption_tick is not None]
            print(f"  Adoption spread:  tick {min(ticks)} to tick {max(ticks)}")

        total_bridges = sum(s["bridges_formed"] for s in self.history)
        total_decayed = sum(s["decayed"] for s in self.history)
        if total_bridges:
            print(f"  Bridge events:    {total_bridges} cross-region links formed")
        if total_decayed:
            print(f"  Adoption decay:   {total_decayed} co-ops dropped out")

        # Resource hub report
        self._print_resource_hubs()

        # Adoption curve
        print("\nAdoption curve:")
        max_bar = 40
        for snap in self.history:
            filled = int(snap["adoption_pct"] / 100 * max_bar)
            bar = "#" * filled + "." * (max_bar - filled)
            print(f"  t={snap['tick']:>3} [{bar}] {snap['adoption_pct']}%")

    def _print_resource_hubs(self):
        """Show top givers and receivers — the network's multiplier nodes."""
        givers = sorted(self.coops, key=lambda c: c.resources_given, reverse=True)
        receivers = sorted(self.coops, key=lambda c: c.resources_received, reverse=True)
        top_givers = [c for c in givers[:5] if c.resources_given > 0]
        top_receivers = [c for c in receivers[:5] if c.resources_received > 0]
        if not top_givers:
            return
        print("\nResource hubs (multiplier nodes):")
        print("  Most generous:")
        for c in top_givers:
            label = Coop.TYPES[c.coop_type]["label"]
            print(f"    {c.name:<12} {label:<16} gave {c.resources_given:>4} units")
        print("  Most supported:")
        for c in top_receivers:
            label = Coop.TYPES[c.coop_type]["label"]
            print(f"    {c.name:<12} {label:<16} received {c.resources_received:>4} units")


def run(ticks=30, network_size=30, seeds=2, seed=42, extensions=None):
    """Run the full simulation."""
    ext_label = ""
    if extensions and any(extensions.values()):
        enabled = [k for k, v in extensions.items() if v]
        ext_label = f"  extensions: {', '.join(enabled)}\n"

    print("Coop-framework Network Simulation")
    print(f"  {network_size} co-ops, {seeds} initial adopters, {ticks} ticks")
    if ext_label:
        print(ext_label, end="")
    print()

    net = CoopNetwork(seed=seed, extensions=extensions)
    net.generate_network(network_size)
    net.seed_adoption(seeds)

    net.print_status()

    for _ in range(ticks):
        net.step()
        snap = net.history[-1]
        if snap["new_adoptions"] > 0 or snap["new_coops"] > 0 or snap["bridges_formed"] > 0 or snap["decayed"] > 0:
            net.print_status()

    net.print_summary()
    return net


if __name__ == "__main__":
    extended = "--extended" in sys.argv
    extensions = {
        "bridge_events": extended,
        "adoption_decay": extended,
        "type_affinity": extended,
    }
    run(extensions=extensions)
