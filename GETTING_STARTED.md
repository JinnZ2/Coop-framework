# Getting Started with Claude for Your Co-op

This guide walks you through using Claude AI for the first time. No technical background needed. If you can copy and paste, you can do this.

## Step 1: Create a Claude Account

1. Go to **[claude.ai](https://claude.ai)** in your web browser
2. Click **Sign up**
3. Enter your email address and create a password
4. Verify your email

The free tier lets you try it out. Paid plans (starting around $20/month) give you more usage. Cancel anytime — no contracts, no lock-in.

Before you put real co-op data in, take two minutes on **Step 5: Check Your Privacy Setting** below.

## Step 2: Pick a Template

Browse the templates in this repository and find one that fits your situation:

| If you run a... | Start with... |
|---|---|
| Food co-op | [Vendor Order Generator](practical-plugins.md) |
| Grain elevator | [Harvest Intake Tracker](grain-elevator-coop.md) |
| Electric co-op | [Outage Response Coordinator](practical-plugins.md#electrical-co-op-plug-ins) |
| Credit union | [Loan Document Summarizer](credit-union-plugin.md) |
| Housing co-op | [Maintenance Request Triage](housing-coop-plugin.md) |
| Worker-owned business | [Profit-Sharing Calculator](worker-owned-plugin.md) |
| Montessori school | [Enrollment Manager](Montessori-plugin.md) |
| Auto repair shop | [Job Tracking & Estimates](auto-repair-shop-plugin.md) |

Or browse the full [Template Index](template-index.md).

## Step 3: Copy, Customize, Paste

Here's a real example. Say you manage a food co-op and want to draft vendor orders.

**1. Copy this template:**

```
I run a food co-op. Here are my vendors and what we typically order monthly:

[Vendor 1]: [Product list with quantities]
[Vendor 2]: [Product list with quantities]
[Vendor 3]: [Product list with quantities]

Generate individual purchase order emails for each vendor for this month.
Adjust quantities: [up 10% for seasonal demand / down 15% because of surplus / keep same].
Format each as a ready-to-send email with subject line, itemized list, and requested delivery date of [date].
```

**2. Replace the `[brackets]` with your real information:**

```
I run a food co-op. Here are my vendors and what we typically order monthly:

Harmony Valley Farm: 40 cases mixed greens, 20 cases root vegetables, 15 cases seasonal fruit
Driftless Provisions: 200 lbs cheddar, 100 lbs gouda, 50 lbs butter
North Country Bakery: 60 loaves sourdough, 40 loaves whole wheat, 30 dozen rolls

Generate individual purchase order emails for each vendor for this month.
Adjust quantities: up 15% for spring demand.
Format each as a ready-to-send email with subject line, itemized list, and requested delivery date of March 15, 2026.
```

**3. Paste it into Claude and hit enter.**

Claude will generate ready-to-send purchase order emails for each vendor with adjusted quantities, subject lines, and professional formatting.

**4. Review, edit, and use.** Claude's output is a draft — always review before sending. You can ask follow-up questions like:
- "Add a note to Harmony Valley about switching to summer greens mix"
- "Make the tone more casual — we've worked with these vendors for years"
- "Also add a new vendor: River Valley Eggs, 30 dozen large, 20 dozen medium"

## Step 4: Stop Re-Pasting — Set Up a Project

Step 3 works, but you don't want to paste the same template and the same background about your co-op every single month. **Projects** fix that.

A Project is a folder for related conversations that share a common set of background material — its **knowledge base**. Anything you put in the knowledge base is available to every chat inside that Project.

**Set one up once:**

1. In Claude, create a new Project and name it after your operation — "Viroqua Food Co-op"
2. Open the Project's knowledge base and add:
   - The template(s) you use regularly, from this repository
   - Your standing facts: co-op name, address, member count, delivery schedule, your vendor list, your fiscal year
   - Anything you'd otherwise retype every time
3. Start a chat inside the Project

Now your monthly vendor order is one sentence — *"Run the vendor order for March, up 15% for spring"* — instead of a wall of pasted text.

**The one thing to know:** context is **not** shared between chats in a Project unless it's in the knowledge base. If you tell Claude something useful in one chat, that chat's neighbors won't know it. Anything you want to persist, put in the knowledge base.

A good pattern is one Project per area of the operation — one for board and governance, one for ordering and vendors, one for grants — each with the relevant templates and background loaded.

## Step 5: Upload Your Files Instead of Retyping Them

Many templates in this repository show your data written out as a structured block — bins, jobs, meter reads, payroll rows. That format exists so the example is clear and so you can see exactly what Claude needs.

**You usually don't have to retype any of it.** If the data already lives in a spreadsheet, an exported report, or a PDF, attach the file and point the template at it:

```
Here's this week's job board, attached as a spreadsheet.
Using the questions below, tell me:
1. Which jobs can I finish today based on parts availability?
2. Generate customer-ready estimates for each open job.
```

You can attach files to a single chat, or add them to a Project's knowledge base if they're reference material you'll use again (your rate schedule, your bylaws, your chart of accounts).

**A few practical limits.** For PDFs, Claude reads both text and visual elements up to 100 pages; from 101 to 1,000 pages it reads text only; over 1,000 pages won't upload. Very large spreadsheets are better trimmed to the columns that matter.

**Claude can hand files back, too.** When a template asks for a "printable checklist," a "board packet," or an "annual meeting presentation," you can ask for it as a real file — a spreadsheet, a document, a slide deck, a PDF — instead of text you reformat by hand:

> "Give me that reserve study as an .xlsx with the formulas intact, not a table in the chat."

## Step 6: Check Your Privacy Setting

This repository exists because co-ops deserve tools without data extraction. That means being straight with you about how your data is actually handled — not making comfortable claims.

Claude has a **model improvement setting** that controls whether your conversations are used to train future models. On the Free, Pro, and Max plans, you choose:

- **Setting off:** your chats are retained for 30 days and are not used to train models
- **Setting on:** your chats may be used to train future models and are retained for up to 5 years

You can find it in your **Privacy Settings** and change it at any time. Turning it off applies going forward and to past chats — Anthropic will not use your previous or new conversations for training. Deleting a chat also removes it from future training.

**Before you paste member records, payroll, loan files, or anything else sensitive, go look at this setting and decide deliberately.** Then tell the next co-op to do the same. Different plan types have different defaults and business/enterprise terms differ, so check yours rather than assuming.

## Step 7: Try More Templates

Once you've used one template successfully, try another. The templates are designed to be mixed and matched:

- Draft your **vendor orders** on Monday morning
- Process your **board meeting minutes** Tuesday night
- Generate your **member newsletter** at the end of the month
- Analyze a **supplier contract** when renewal comes up
- Build a **grant application** when funding opportunities appear

## Tips for Getting the Most Out of Claude

**Be specific.** The more real details you give Claude, the more useful the output. Don't say "some vendors" — name them. Don't say "a few products" — list them with quantities.

**Ask follow-ups.** Claude remembers the whole conversation. After it generates something, you can say "change the tone" or "add a section about X" or "now do the same thing for next month."

**Attach real documents.** Contracts, meeting notes, financial reports, scanned invoices, spreadsheets — upload them directly. Ask Claude to summarize, analyze, or reformat.

**Turn on web search when you need current information.** Claude can search the live web and cite its sources. That's useful for grant deadlines, regulatory changes, or what comparable co-ops are charging. Verify anything price-sensitive or time-sensitive against your own source before acting on it.

**It's a conversation, not a form.** You don't have to use templates at all. You can just describe what you need in plain language: "I need to write a letter to our members explaining why eggs are more expensive this month."

**Correct it.** If Claude gets a number or an assumption wrong, say so plainly. It'll rework it. Don't start over.

## What Claude Is Good At

- Drafting emails, letters, newsletters, and reports
- Summarizing long documents into plain language
- Analyzing numbers and spotting trends
- Reading your spreadsheets and exports directly
- Producing finished files — spreadsheets, documents, slide decks, PDFs
- Planning events and creating checklists
- Comparing options and modeling scenarios
- Organizing messy notes into clean documents
- Looking up current information on the web, with citations

## What Claude Is Not

- Not a replacement for professional legal, financial, or medical advice
- Not automatically aware of your operation — it knows what's in the current chat, plus whatever you've put in that Project's knowledge base
- Not a system of record — it doesn't replace your books, your member database, or your compliance files
- Not infallible — always review its work, especially numbers and legal language

## Share What Works

If a template saves you time, tell another co-op. That's how this spreads — not through sales calls, but through trust.

---

*Questions? Open an issue on GitHub or share what's working in your co-op network.*
