# {{WIKI_NAME}}

A persistent, LLM-maintained personal Markdown wiki designed to preserve sources, judgments, decisions, and changes in understanding.

Generated on {{DATE}}. Read [BLUEPRINT.md](BLUEPRINT.md) for the confirmed design and [{{SCHEMA_FILE}}]({{SCHEMA_FILE}}) for future maintenance rules.

## Domains

{{DOMAIN_LIST}}

## Repository Layout

```text
inbox/capture/          Unprocessed notes and materials
inbox/suggestions/      Core changes awaiting confirmation
raw/                    Original sources; do not rewrite after ingestion
wiki/domains/           Domain knowledge pages
wiki/sources/           Source summaries and assessments
wiki/synthesis/         Cross-domain and periodic synthesis
templates/              Page and output templates
exports/private/        Private outputs
exports/public/         Sanitized public drafts only
BLUEPRINT.md            Confirmed design decisions
index.md                Content-oriented wiki index
log.md                  Append-only maintenance history
```

## Working with the Wiki

Use an agent that can read and edit this repository. Typical requests after setup:

- `Process my capture inbox.`
- `Ingest this source into the relevant domain.`
- `Archive this discussion.`
- `Answer from the wiki and distinguish facts from my judgments.`
- `Run a wiki health check.`
- `Prepare a sanitized public draft.`

The future agent must follow `{{SCHEMA_FILE}}`, especially its confirmation and privacy rules.

## Viewing and Capture

The repository can be browsed with Obsidian, a text editor, or Git hosting tools. Obsidian is optional. Quick capture belongs in `inbox/capture/`; do not require mobile users to classify notes before capture.

## Boundaries

- Do not store passwords, tokens, private keys, identity documents, or account credentials.
- Repository visibility and public-export rules are defined in `BLUEPRINT.md`.
- A public draft is not published until a separate explicit publication action succeeds.
- Start without vector search or a website unless the blueprint explicitly requires them.

## Provenance

Scaffolded with [Personal Wiki Builder](https://github.com/laurenceshan/personal-wiki-builder), an unofficial implementation inspired by Andrej Karpathy's [llm-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). This notice does not apply a license to user content.
