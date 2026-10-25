---
name: personal-wiki-builder
description: Interview-first scaffolding for persistent, LLM-maintained personal Markdown wikis. Use when a user wants to design or create a personal knowledge base, second brain, personal wiki, or Karpathy-style LLM wiki; gather requirements through a guided interview or quick-start defaults; produce a confirmed blueprint; and scaffold a local or GitHub repository with raw sources, wiki pages, an agent schema, templates, indexes, logs, capture inboxes, and export boundaries. Covers requirements, blueprinting, repository generation, and validation only, not ongoing ingestion or wiki maintenance.
---

# Personal Wiki Builder

## Purpose

Turn a user's goals and working style into a customized personal wiki blueprint, then generate and validate a repository that an LLM agent can maintain later.

Preserve Karpathy's three-layer pattern: immutable raw sources, a persistent interlinked Markdown wiki, and a schema that governs agent behavior. Add guided requirements discovery, explicit judgment and decision provenance, tiered write permissions, privacy-aware exports, and pilot acceptance criteria.

## Scope

Include:

- Guided Interview and Quick Start modes.
- A user-confirmed `BLUEPRINT.md`.
- A domain-customized starter repository.
- A canonical agent schema, defaulting to `AGENTS.md`.
- Generic English templates and optional repository creation through available GitHub tools.
- Scaffold validation and a clear handoff.

Exclude:

- Ingesting the user's real sources.
- Maintaining the resulting wiki after handoff.
- Automatic publishing or public export of private content.
- Introducing vector search, embeddings, a website, or complex automation by default.

Do not turn this setup skill into an ongoing maintenance session. After validation, hand maintenance over to the generated schema or a separate maintenance workflow.

## Workflow

### 1. Select a mode

Use **Guided Interview** when requirements are open-ended or the user wants to think through the design. Read [references/interview.md](references/interview.md).

Use **Quick Start** when the user requests speed or accepts editable defaults. Read the defaults in [references/blueprint.md](references/blueprint.md).

When the user does not choose, recommend Guided Interview for a new personal knowledge system and Quick Start for a proof of concept. Conduct the interview in the user's language even though the skill documentation and assets are in English.

### 2. Establish requirements

For Guided Interview:

- Proceed in small stages, normally three to five questions at a time.
- Adapt questions to earlier answers; do not mechanically ask the whole question bank.
- Summarize each stage and distinguish confirmed decisions from assumptions.
- Ask only about genuinely unresolved ambiguity.

For Quick Start:

- Use known requirements and fill gaps with the documented defaults.
- Present one consolidated configuration with editable defaults.
- Do not skip repository visibility or other privacy-relevant confirmation.

### 3. Produce and confirm the blueprint

Read [references/blueprint.md](references/blueprint.md). Create a concise but complete blueprint covering purpose, domains, sources, page types, workflows, write permissions, evidence rules, outputs, privacy, implementation, and pilot acceptance.

Write the blueprint in the user's preferred language. Mark confirmed decisions, proposed defaults, and unresolved items separately.

**Wait for explicit user confirmation before creating or modifying a repository.** A request to discuss or design a wiki is not permission to create it.

### 4. Scaffold the repository

Read [references/scaffolding.md](references/scaffolding.md). Save the confirmed blueprint as a Markdown file outside the target repository, then run:

```bash
python3 <skill-root>/scripts/scaffold_wiki.py \
  --target /path/to/new-repository \
  --name "My Personal Wiki" \
  --domains learning personal-reflection \
  --blueprint /path/to/confirmed-blueprint.md \
  --schema AGENTS.md
```

Use lowercase domain slugs containing only letters, numbers, and hyphens. The target must be new or empty.

After scaffolding:

- Adapt the generated schema, README, index, and templates to the confirmed blueprint.
- Keep one canonical schema. Default to `AGENTS.md`; adapt the filename when the host environment requires another convention instead of creating divergent copies.
- Preserve English starter templates unless the user explicitly requests localized scaffolding. Generated blueprint and later wiki content may use the user's language.
- Do not copy the skill's MIT license into the user's wiki as a license for their personal content.

If Python is unavailable, copy `assets/starter-repo/` manually and follow the fallback checklist in [references/scaffolding.md](references/scaffolding.md).

### 5. Validate

Run:

```bash
python3 <skill-root>/scripts/verify_scaffold.py \
  --target /path/to/new-repository \
  --domains learning personal-reflection \
  --schema AGENTS.md
```

Confirm that:

- Required directories, templates, blueprint, index, log, and schema exist.
- Every confirmed domain has a directory.
- No unresolved `{{...}}` placeholders remain.
- The blueprint is present and substantive.
- Repository visibility matches the user's decision.
- No credentials or unintended personal content were introduced.

If validation fails, fix the cause and rerun the affected checks.

### 6. Deliver and hand off

Report:

- Local path or actual repository URL.
- Guided Interview or Quick Start mode.
- Confirmed domains and schema filename.
- Validation result.
- The next recommended step: ingest one small pilot batch under the generated repository's rules.

Do not claim that a remote repository exists unless it was actually created. Do not begin ingestion or maintenance in this skill.

## Repository and Privacy Rules

- Default newly generated personal wikis to **private**.
- Require explicit confirmation before making any wiki public.
- Keep the public skill repository free of user-specific wiki content.
- Never include passwords, tokens, private keys, identity documents, or account credentials in scaffolding or examples.
- If GitHub tooling is unavailable, create a local repository and provide Git commands instead of pretending to publish.
- Public export governance belongs in the generated schema, but this skill does not perform exports.

## Design Rules

- Prefer Markdown, YAML, bidirectional links, `index.md`, and `log.md` before adding search infrastructure.
- Keep raw sources immutable after ingestion; the setup only creates the structure that enforces this rule.
- Distinguish facts, external viewpoints, user judgments, and AI inference.
- Preserve human-readable judgment history rather than relying only on Git history.
- Require confirmation for changes to established claims, principles, and important decisions.
- Treat tags as secondary to links and explicit page relationships.
- Use generic examples only; never embed a particular user's private domains, notes, or decisions in the public skill.

## Attribution

This is an unofficial implementation inspired by Andrej Karpathy's [llm-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). No endorsement is implied.

The original pattern provides raw sources, a persistent wiki, a schema, ingest/query/lint operations, indexing, and logging. This skill adds requirements discovery, blueprint confirmation, deterministic scaffolding, judgment and decision provenance, tiered write permissions, privacy-aware export boundaries, and pilot acceptance criteria.
