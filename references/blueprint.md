# Blueprint Reference

Use this reference to produce `BLUEPRINT.md` and to configure Quick Start mode. The blueprint may be written in the user's language.

## Required Blueprint Sections

### 1. Purpose and Success Criteria

State the one-sentence purpose and the primary result that defines success. Explain what the wiki should help the user understand or do, not merely what files it should contain.

### 2. Scope and Non-Goals

List initial domains and what the first version deliberately excludes. Distinguish long-term possibilities from current commitments.

### 3. Raw Sources and Privacy

List accepted source types, prohibited content, repository visibility, public-export boundaries, and any third-party confidentiality constraints.

### 4. Knowledge Model and Navigation

Define:

- Domain organization and slugs.
- Core and supporting page types.
- Cross-domain relationships.
- The respective roles of `index.md` and `log.md`.

### 5. Workflows

Describe quick capture, themed ingestion, querying, archival, contradiction handling, health checks, and reviews. This blueprint configures future maintenance even though the builder skill does not execute those workflows.

### 6. Agent Permission Matrix

Specify what the future maintainer may do automatically, what requires confirmation, and what is prohibited. Address established claims, principles, decisions, page merges, deletions, exports, and publication.

### 7. Evidence and Judgment History

Explain how pages will distinguish facts, external viewpoints, user judgments, and AI inference. Define how sources, dates, counterevidence, and changes in judgment are recorded.

### 8. Outputs

List priority private and public outputs. State that public output requires manual selection and sanitization unless the user explicitly chooses another policy.

### 9. Implementation

Record:

- Repository name and target location.
- Private or public visibility.
- Canonical schema filename.
- Domain slugs.
- Viewer and capture expectations.
- Technology boundaries.

### 10. Pilot and Acceptance

Define two small end-to-end pilots when possible. Include checks for source traceability, judgment history, index and log updates, archival behavior, confirmation gates, and safe export boundaries.

## Decision Labels

Use three labels throughout the blueprint:

- **Confirmed**: explicitly chosen by the user.
- **Default**: proposed by the agent and accepted or left editable.
- **Open**: unresolved and not silently guessed.

Do not hide assumptions inside polished prose.

## Quick Start Defaults

Use these defaults only for missing requirements. Present them as one editable configuration before scaffolding.

| Area | Default |
|---|---|
| Purpose | Build compounding personal knowledge and preserve why judgments form or change |
| Domains | `learning`, `personal-reflection` |
| Repository | `personal-wiki`, private |
| Sources | External readings, personal notes, AI conversations, research data |
| Navigation | Domain directories plus type indexes |
| Core pages | `claim`, `principle`, `decision`, `question` |
| Supporting pages | `source`, `concept`, `entity`, `review` |
| Capture | Mixed quick inbox and themed batches |
| Automatic writes | Source summaries, concepts, entities, and draft questions |
| Confirmation gate | Established claims, principles, important decisions, merges, deletions, exports |
| Contradictions | Preserve old judgments and record new evidence and reasons for change |
| Archival | Agent-selected valuable output plus explicit `Archive` command |
| Evidence | Separate facts, external viewpoints, user judgments, and AI inference |
| Outputs | Private by default; sanitized public drafts only on request |
| Technology | Markdown, YAML, bidirectional links, index, log; no search service |
| Viewer | Obsidian optional |
| Pilot | Two small batches, one per domain when practical |

If the user already supplied a domain, repository name, or other choice, use it instead of the default. Never overwrite a stated preference with this table.

## Blueprint Quality Check

Before requesting confirmation, verify that:

- The blueprint answers why, what, how, and who may change what.
- Every initial domain has a clear purpose.
- Core page types reflect actual user priorities.
- Privacy and repository visibility are explicit.
- The first version avoids unnecessary infrastructure.
- Acceptance criteria can be tested with small real batches.
- No private source material has been copied into the public builder skill.
