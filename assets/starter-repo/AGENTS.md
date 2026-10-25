# Agent Maintenance Rules

This file is the canonical operating schema for this personal wiki. `BLUEPRINT.md` records the initial design; this file governs future maintenance. If they conflict, ask the user before changing either one.

## 1. Purpose

Build compounding knowledge rather than repeated retrieval. Preserve traceability between raw sources, current understanding, decisions, and changes in judgment.

## 2. Core Rules

1. Distinguish facts, external viewpoints, user judgments, and AI inference.
2. Never fabricate sources, dates, quotations, experiences, or user opinions.
3. Update related pages, links, `index.md`, and `log.md` when new knowledge is integrated.
4. Search for an existing page before creating a new one.
5. Preserve human-readable judgment history; Git history is not a substitute.
6. Keep repository visibility and export behavior aligned with `BLUEPRINT.md`.
7. Never store passwords, tokens, private keys, identity documents, or account credentials.

## 3. Layers and Work Areas

### Raw Sources

`raw/` contains original material after capture. Do not rewrite, polish, summarize over, or silently correct raw files.

- `raw/external/`: readings, papers, articles, and web clippings.
- `raw/personal/`: notes, journals, and voice transcripts.
- `raw/ai-conversations/`: AI conversations and generated research; claims still require verification.
- `raw/research-data/`: datasets, analysis results, and project records.
- `raw/assets/`: images and attachments.

Explain transcription noise, uncertainty, and missing context in a `source` page instead of changing the raw file. If a raw file must move, update every reference and append a log entry.

### Wiki

`wiki/` contains persistent Markdown knowledge:

- `wiki/domains/<domain>/`: domain-specific pages.
- `wiki/sources/`: one summary and assessment page per raw source.
- `wiki/synthesis/`: cross-domain and periodic synthesis.

Use one canonical copy of each page. Connect it to other contexts through links and indexes rather than duplicates.

### Inbox and Exports

- `inbox/capture/`: unprocessed notes and materials.
- `inbox/suggestions/`: proposed changes requiring user confirmation.
- `exports/private/`: private outputs.
- `exports/public/`: manually reviewed public drafts; never proof of publication.

## 4. Page Types

Core types:

- `claim`: a current judgment, evidence, counterevidence, boundaries, and change history.
- `principle`: an action principle, its origin, scope, costs, and revision history.
- `decision`: context, options, reasoning, action, expected outcome, actual outcome, and review.
- `question`: a long-term question that aggregates sources, claims, conflicts, and unknowns.

Supporting types:

- `source`: source metadata, summary, external viewpoints, user assessment, and limitations.
- `concept`: definitions, examples, scope, misconceptions, and relationships.
- `entity`: records for people, organizations, projects, assets, events, or other domain objects.
- `review`: structured reflection on decisions, actions, periods, or outcomes.

Use only types that serve the confirmed blueprint. Additional types require a clear need.

## 5. Markdown and Metadata

Use this minimum frontmatter unless the blueprint specifies otherwise:

```yaml
---
type: claim
domains: [domain-slug]
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- Use lowercase English type values and domain slugs.
- Use `draft`, `active`, or `archived` for status unless a page type needs a documented alternative.
- Use `confidence: low | medium | high` only when useful for claims.
- Use `decision_date` and `review_on` for decisions when known.
- Prefer stable, readable filenames and avoid unnecessary renaming.
- Prefer `[[Page Name]]` for wiki links; disambiguate by path when necessary.
- Treat tags as secondary to explicit links.

## 6. Write Permissions

| Action | Default permission |
|---|---|
| Organize inbox items and create source summaries | Automatic; never rewrite raw originals |
| Create or update concept and entity pages | Automatic |
| Create long-term questions or synthesis drafts | Automatic |
| Archive valuable non-core discussion output | Automatic and logged |
| Create an AI-inferred claim or principle | Draft only; never present it as user-confirmed |
| Change an established claim, principle, or important decision | Propose first; require user confirmation |
| Merge, delete, or substantially rewrite pages | Require user confirmation |
| Create a public export | Require an explicit user request and sanitization |
| Publish externally or change repository visibility | Prohibited without explicit user instruction |

An explicit `Archive` command authorizes archival of the current discussed result, not unrelated changes. If it contains a core judgment, archive only what the user actually confirmed.

## 7. Ingestion

For each source or coherent themed batch:

1. Preserve the original under `raw/`.
2. Create or update a `source` page with source date, ingestion date, and raw path.
3. Separate verifiable facts, external viewpoints, and user assessment.
4. Update relevant concepts, entities, claims, decisions, and questions according to permissions.
5. Handle contradictions using Section 9.
6. Update `index.md` and append to `log.md`.
7. For a themed batch, finish with a synthesis of strengthened, weakened, and unresolved judgments.

Do not invent completeness. Record missing evidence and open questions.

## 8. Query and Archival

1. Read `index.md` first, then relevant wiki pages, then raw sources when needed.
2. Distinguish existing wiki synthesis from new inference in the answer.
3. State when the wiki is insufficient; suggest useful missing sources when appropriate.
4. Archive valuable results by updating an existing page or creating a non-duplicate new page.
5. Support both agent-selected archival and the explicit `Archive` command.
6. Route core changes through `inbox/suggestions/` unless the user has explicitly confirmed them.

## 9. Contradictions and Judgment Changes

When new evidence conflicts with an old judgment:

- Preserve the old judgment and its original supporting context.
- Collect supporting evidence, counterevidence, and applicability boundaries.
- Do not silently replace an established current judgment.
- After confirmation, update the current judgment and append the date, old judgment, new judgment, triggering source, and reason for change.
- If no conclusion is justified, retain the conflict and define what would resolve it.

## 10. Index and Log

Update `index.md` whenever pages are created, renamed, merged, removed, or significantly reframed. Give every listed page a link and one-line summary.

Append to `log.md`; never rewrite old entries. Use consistent headings:

```markdown
## [YYYY-MM-DD] ingest | Source or theme
## [YYYY-MM-DD] archive | Page or discussion
## [YYYY-MM-DD] lint | Scope
## [YYYY-MM-DD] synthesis | Period or theme
## [YYYY-MM-DD] export | Output
## [YYYY-MM-DD] decision | Decision or review
```

The log records what happened. Claim and principle pages record why judgments changed.

## 11. Health Checks and Reviews

When the user requests a health check, inspect:

- Broken links, duplicate names, orphan pages, and missing backlinks.
- Unprocessed inbox items and pending suggestions.
- Unsupported key claims and missing source dates.
- Contradictions, stale claims, and overdue reviews.
- Useful missing pages and research questions.

Small link and metadata repairs may be automatic. Merges, deletions, and core judgment changes still require confirmation.

## 12. Privacy and Public Exports

- Do not expose private content in public issues, gists, repositories, or publishing tools.
- Remove third-party personal data, sensitive experiences, exact financial details, confidential project material, internal paths, and private notes from public drafts.
- Use publicly accessible citations in public outputs; private raw paths are not usable public citations.
- Never treat a public draft as published.
- If a secret enters Git history, deleting the current file is insufficient; alert the user for dedicated remediation.

## 13. Technology Boundary

Start with Markdown, YAML, links, `index.md`, `log.md`, and file search. Add vector search, semantic retrieval, websites, or automation only when a demonstrated scale problem justifies them and the user approves.
