# Personal Wiki Builder

Interview-first scaffolding for LLM-maintained personal wikis, inspired by [Karpathy's llm-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Personal Wiki Builder turns the high-level llm-wiki idea into a confirmed design and a validated starter repository. It helps a user decide what the wiki should accumulate, how an agent may change it, and which boundaries must hold before content is created.

This is an unofficial, agent-agnostic setup skill. It covers requirements discovery, blueprinting, scaffolding, and validation—not ongoing ingestion or wiki maintenance.

## What It Inherits from llm-wiki

The generated repositories preserve Karpathy's core pattern:

- **A persistent, compounding wiki** instead of repeatedly rediscovering knowledge at query time.
- **Three layers:** immutable raw sources, an LLM-maintained Markdown wiki, and a schema that governs agent behavior.
- **Ingest, query, and lint** as the main maintenance operations.
- **`index.md` and `log.md`** for content navigation and append-only operational history.
- **Knowledge compounding through archival:** valuable answers and explorations can become durable wiki pages rather than disappearing into chat history.

## Three Concrete Extensions

### 1. Design Before Scaffolding

The original pattern intentionally leaves implementation details to each user and agent. This skill supplies a repeatable setup process:

- Resolve goals, sources, knowledge objects, workflows, permissions, outputs, privacy, and acceptance criteria through a Guided Interview.
- Offer Quick Start defaults when speed matters more than deliberation.
- Separate **Confirmed**, **Default**, and **Open** decisions instead of hiding assumptions in polished prose.
- Require explicit user confirmation of the complete blueprint before creating or modifying a repository.
- Keep `BLUEPRINT.md` and the canonical agent schema distinct: the blueprint records design intent and user decisions; the schema governs future maintenance.

### 2. Preserve How Understanding Evolves

A personal wiki can be more than a collection of summaries. This skill makes judgment formation and revision first-class knowledge:

- Use `claim`, `principle`, `decision`, and `question` as core page types.
- Distinguish **facts, external viewpoints, user judgments, and AI inference**.
- Record supporting evidence, counterevidence, applicability boundaries, source dates, and unresolved questions.
- Keep human-readable judgment history inside claim and principle pages rather than relying only on Git history.
- Capture a decision's original context, options, expectations, actual outcome, and review attribution.

In short: **`log.md` records what happened; page-level history explains why a judgment changed.**

### 3. Make Agent Maintenance Governable

The generated schema turns the pattern's broad LLM-maintainer role into explicit operating boundaries:

- Automatically maintain low-risk source, concept, and entity pages.
- Mark AI-inferred claims and principles as drafts rather than user-confirmed views.
- Require confirmation before changing established claims, principles, important decisions, or performing destructive page operations.
- Preserve old judgments when contradictory evidence arrives; record the trigger and reason for any confirmed revision.
- Support both agent-selected archival and an explicit `Archive` command with a limited authorization scope.
- Default personal wikis to private and require manual selection and sanitization for public exports.

## Six Core Features

| Feature | What it provides |
|---|---|
| **1. Two setup modes** | A staged Guided Interview for open-ended design and a Quick Start path with editable defaults. Interviews use the user's language; starter documentation and templates remain clear, simple, and reviewable. |
| **2. Confirmed blueprint and canonical schema** | A user-confirmed `BLUEPRINT.md`, domain-specific configuration, and one canonical schema—`AGENTS.md` by default, with `CLAUDE.md` supported. |
| **3. Judgment-centric knowledge model** | Ten templates covering core judgment pages, supporting source, concept, and entity pages, reviews, periodic synthesis, and manually reviewed public drafts. |
| **4. Evidence and revision provenance** | Four-way epistemic separation, source traceability, counterevidence, applicability boundaries, judgment revision history, and decision reviews. |
| **5. Governed workflows and privacy boundaries** | Tiered write permissions, contradiction handling, quick capture, themed ingestion, dual archival, private-by-default repositories, and sanitized public exports. |
| **6. Deterministic delivery and acceptance** | Dependency-free scaffolding scripts, empty-target protection, domain generation, structural verification, small pilot recommendations, and an explicit validation step before use. |

## Comparison Brief: LLM-Wiki Variants

| Project | What it emphasizes | Main strengths | Best for |
|---|---|---|---|
| **Original Karpathy pattern** | Persistent, compounding wiki as a memory layer | Minimal, conceptually strong, durable knowledge accumulation, raw/wiki/schema separation, cross-linking | People learning the core idea and wanting to build their own custom workflow from the ground up |
| **ScrapingArt / Karpathy-LLM-Wiki-Stack** | Practical implementation stack | Concrete build-out, tooling, Obsidian/Claude workflows, stronger operational guidance than the gist alone | Users who want a working setup quickly and prefer opinionated, build-ready examples |
| **LLM Wiki v2** | Knowledge lifecycle and maintenance quality | Confidence, freshness, versioning, supersession and review discipline, extends the base pattern toward a more mature knowledge system | People who want their wiki to reason about obsolescence, trust, and revision over time |
| **llmwiki.app** | Productized wiki experience | Easy onboarding, UI-first workflow, lower friction for non-technical users, quick adoption | Users who want an accessible wiki tool without custom scaffolding or deep setup work |
| **Personal Wiki Builder** | Guided setup and safe governance | Interview-first design, confirmed blueprint, schema boundaries, judgments and evidence tracking, privacy-first defaults | People who want a personal wiki designed intentionally before content is created, with strong guardrails |

### Short Recommendation

- If you want the simplest and most influential conceptual model: choose the original Karpathy pattern.
- If you want a concrete implementation to adapt quickly: choose ScrapingArt's stack.
- If you want stronger knowledge lifecycle and trust management: choose LLM Wiki v2.
- If you want a low-friction product rather than a custom system: choose llmwiki.app.
- If you want a private, governed personal wiki built intentionally and safely: choose Personal Wiki Builder.

## Use with an Agent

Expose this directory as a skill in an agent environment that supports `SKILL.md` workflows. The installation location depends on the host environment.

For a guided setup, ask:

> Use personal-wiki-builder to interview me and design a personal wiki. Do not create the repository until I confirm the blueprint.

For a faster start, ask:

> Use personal-wiki-builder in Quick Start mode. Show me the editable defaults first, then scaffold a private wiki after I confirm them.

The agent should produce the blueprint, wait for confirmation, generate the repository, validate it, and stop before ingesting real sources.

## Run the Scaffolder Directly

The scripts use only the Python standard library. Save the confirmed blueprint outside the new target directory, then run:

```bash
python3 <skill-root>/scripts/scaffold_wiki.py \
  --target /path/to/new-repository \
  --name "My Personal Wiki" \
  --domains learning personal-reflection \
  --blueprint /path/to/confirmed-blueprint.md \
  --schema AGENTS.md
```

Use lowercase domain slugs containing only letters, numbers, and hyphens. The target must be new or empty. To use a Claude-oriented schema filename, pass `--schema CLAUDE.md`.

Validate the generated structure:

```bash
python3 <skill-root>/scripts/verify_scaffold.py \
  --target /path/to/new-repository \
  --domains learning personal-reflection \
  --schema AGENTS.md
```

Structural validation does not prove semantic fit. Review the generated rules and templates against the confirmed blueprint, then test the maintenance workflow with a small pilot batch.

The scaffolding scripts do not initialize Git, create a remote repository, ingest sources, or publish content.

## Generated Repository

```text
├── AGENTS.md                 # Or the selected canonical schema filename
├── BLUEPRINT.md              # Confirmed design decisions
├── README.md                 # Generated wiki overview
├── index.md                  # Content navigation
├── log.md                    # Append-only operational history
├── inbox/
│   ├── capture/              # Unprocessed notes and materials
│   └── suggestions/          # Changes awaiting user confirmation
├── raw/                      # Immutable original sources
├── wiki/
│   ├── domains/              # Domain-specific knowledge pages
│   ├── sources/              # Source summaries and assessments
│   └── synthesis/            # Cross-domain and periodic synthesis
├── templates/                # Ten English knowledge-page templates
└── exports/
    ├── private/              # Private outputs
    └── public/               # Manually reviewed public drafts
```

## Scope and Handoff

This skill intentionally stops at setup and validation. It does not:

- Ingest a user's real sources.
- Maintain the wiki after delivery.
- Publish private material or treat a public draft as published.
- Introduce vector search, embeddings, websites, or complex automation by default.

After handoff, use the generated canonical schema or a separate maintenance workflow. Begin with a small pilot and check source traceability, judgment history, confirmation gates, index and log updates, and privacy boundaries.

## Attribution

This project is an unofficial implementation inspired by Andrej Karpathy's [llm-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). No endorsement is implied.

The original pattern supplies the persistent wiki, raw-source layer, agent schema, ingest/query/lint operations, indexing, and logging. Personal Wiki Builder adds structured requirements discovery, blueprinting, validation, and explicit governance around how a future agent may change the personal wiki.

## License

This skill is available under the [MIT License](LICENSE). Do not treat the skill's license as a license for private content later added to a generated personal wiki.
