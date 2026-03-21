"""
Coop-framework: Toy network simulation

Models three interconnected dynamics:
  1. Trust propagation — Claude adoption spreads through co-op relationships
  2. Network growth — new co-ops form and connect over time
  3. Resource distribution — co-ops share surplus resources along trust links

Run:  python3 coop_sim.py
"""

import random
import math


class Coop:
    """A single cooperative in the network."""

    TYPES = {
        "food": {"trust_rate": 0.15, "resource_cap": 100, "label": "Food Co-op"},
        "grain": {"trust_rate": 0.12, "resource_cap": 150, "label": "Grain Elevator"},
        "electric": {"trust_rate": 0.10, "resource_cap": 200, "label": "Electric Co-op"},
        "credit": {"trust_rate": 0.08, "resource_cap": 300, "label": "Credit Union"},
        "worker": {"trust_rate": 0.18, "resource_cap": 80, "label": "Worker Co-op"},
    }

    def __init__(self, name, coop_type, region):
        spec = self.TYPES[coop_type]
        self.name = name
        self.coop_type = coop_type
        self.region = region
        self.trust_rate = spec["trust_rate"]
        self.resource_cap = spec["resource_cap"]
        self.resources = random.randint(20, spec["resource_cap"])
        self.adopted = False
        self.adoption_tick = None
        self.connections = []  # list of (other_coop, trust_strength)

    def __repr__(self):
        status = "ADOPTED" if self.adopted else "pending"
        return f"{self.name} ({self.TYPES[self.coop_type]['label']}, {self.region}) [{status}]"


class CoopNetwork:
    """The full cooperative network simulation."""

    REGIONS = ["Minnesota", "Wisconsin", "Vermont", "Oregon", "Appalachia", "Dakotas"]

    def __init__(self, seed=42):
        self.rng = random.Random(seed)
        self.tick = 0
        self.coops = []
        self.history = []
        self._name_counter = 0

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
            # prefer same-region connections
            candidates.sort(key=lambda c: (0 if c.region == coop.region else 1, self.rng.random()))
            for partner in candidates[:n_connections]:
                trust = round(self.rng.uniform(0.1, 0.6), 2)
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
        """Advance one tick: propagate trust, grow network, distribute resources."""
        self.tick += 1
        adoptions = self._propagate_trust()
        new_coops = self._grow_network()
        transfers = self._distribute_resources()
        snapshot = self._snapshot(adoptions, new_coops, transfers)
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
                # Probability = trust_strength * partner's trust_rate * network_effect
                network_bonus = 1 + 0.05 * sum(1 for c, _ in partner.connections if c.adopted)
                prob = trust * partner.trust_rate * network_bonus
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
        for coop in self.coops:
            if coop.resources <= coop.resource_cap * 0.3:
                continue  # nothing to spare
            for partner, trust in coop.connections:
                if partner.resources < partner.resource_cap * 0.4:
                    # Share proportional to trust
                    amount = int(coop.resources * trust * 0.1)
                    if amount > 0:
                        coop.resources -= amount
                        partner.resources = min(partner.resources + amount, partner.resource_cap)
                        transfers.append((coop.name, partner.name, amount))
        return transfers

    # --- Helpers ---

    def _spawn_coop(self, coop_type, region):
        self._name_counter += 1
        name = f"{region[:3].upper()}-{coop_type[:2].upper()}{self._name_counter:03d}"
        coop = Coop(name, coop_type, region)
        self.coops.append(coop)
        return coop

    def _snapshot(self, adoptions, new_coops, transfers):
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

        # Adoption curve
        print("\nAdoption curve:")
        max_bar = 40
        for snap in self.history:
            filled = int(snap["adoption_pct"] / 100 * max_bar)
            bar = "#" * filled + "." * (max_bar - filled)
            print(f"  t={snap['tick']:>3} [{bar}] {snap['adoption_pct']}%")


def run(ticks=30, network_size=30, seeds=2, seed=42):
    """Run the full simulation."""
    print("Coop-framework Network Simulation")
    print(f"  {network_size} co-ops, {seeds} initial adopters, {ticks} ticks\n")

    net = CoopNetwork(seed=seed)
    net.generate_network(network_size)
    net.seed_adoption(seeds)

    net.print_status()

    for _ in range(ticks):
        net.step()
        snap = net.history[-1]
        if snap["new_adoptions"] > 0 or snap["new_coops"] > 0:
            net.print_status()

    net.print_summary()
    return net


if __name__ == "__main__":
    run()
