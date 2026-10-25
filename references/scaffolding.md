# Scaffolding Reference

Use this reference after the user confirms the blueprint.

## Starter Assets

`assets/starter-repo/` contains:

- `AGENTS.md`: default future-maintenance rules.
- `README.md`: generated wiki overview.
- `index.md` and `log.md`: navigation and append-only history.
- `inbox/`: unprocessed captures and pending core-change suggestions.
- `raw/`: immutable source categories.
- `wiki/domains/`: user-selected domains.
- `wiki/sources/`: source summaries and assessments.
- `wiki/synthesis/`: cross-domain and periodic synthesis.
- `templates/`: generic English page and output templates.
- `exports/`: private and public-draft boundaries.

The builder copies the confirmed blueprint to `BLUEPRINT.md` separately. Do not treat the blueprint as agent instructions; the canonical schema governs maintenance.

## Deterministic Scaffolding

Run from any working directory:

```bash
python3 <skill-root>/scripts/scaffold_wiki.py \
  --target /path/to/new-repository \
  --name "My Personal Wiki" \
  --domains learning personal-reflection \
  --blueprint /path/to/confirmed-blueprint.md \
  --schema AGENTS.md
```

Rules:

- The target must be new or empty.
- The blueprint must already exist and contain the confirmed design.
- Domain arguments are slugs, not display names. Convert names to lowercase ASCII letters, numbers, and hyphens before invoking the script.
- The schema argument is a filename, not a path.
- The script does not initialize Git, create a remote repository, ingest content, or publish anything.

The script copies assets, creates domain directories, replaces supported placeholders, installs the blueprint, and adapts the schema filename.

## Post-Scaffold Customization

Review the generated files against the blueprint:

1. Update the future agent schema if the user selected different write permissions, archival behavior, or export rules.
2. Preserve one canonical schema. Default to `AGENTS.md`; use another filename only when required or explicitly requested.
3. Review domain display names in README and index. The script derives English display names from slugs; localize them if the user requested localized scaffolding.
4. Keep generic supporting templates unless the user explicitly excluded them.
5. Do not insert real source material during setup.
6. Do not copy the builder's license into the generated wiki as a license for user content.

## Validation

Run:

```bash
python3 <skill-root>/scripts/verify_scaffold.py \
  --target /path/to/new-repository \
  --domains learning personal-reflection \
  --schema AGENTS.md
```

Then perform semantic checks that a script cannot perform:

- The schema matches the confirmed permission matrix.
- The blueprint and generated navigation agree on domains.
- Private and public boundaries are not contradictory.
- No real private content or credentials appear in examples.
- The schema filename matches the target agent environment.

## Manual Fallback

If Python is unavailable:

1. Copy `assets/starter-repo/` into a new empty target.
2. Create `wiki/domains/<domain-slug>/` for every confirmed domain.
3. Copy the confirmed blueprint to `BLUEPRINT.md`.
4. Replace `{{WIKI_NAME}}`, `{{DOMAIN_LIST}}`, `{{DOMAIN_SECTIONS}}`, `{{SCHEMA_FILE}}`, and `{{DATE}}` in generated Markdown files.
5. Rename `AGENTS.md` if another canonical schema filename was confirmed.
6. Check the required files and unresolved placeholders manually.

Do not claim scripted validation passed when it was not run. Report manual verification instead.

## Local Delivery

When no remote creation tool is available, leave the generated repository locally and provide:

```bash
cd /path/to/new-repository
git init
git add .
git commit -m "Initialize personal wiki"
```

Add remote creation or push commands only when the user supplies or confirms the destination.

## GitHub Delivery

When GitHub tooling is available:

1. Confirm owner, repository name, and visibility from the blueprint.
2. Create the repository only after blueprint confirmation.
3. Push the generated files to the confirmed branch.
4. Read back the root and important directories to verify the result.
5. Return the actual URL returned by the tool.

Default to private. Never infer that a public builder skill implies a public personal wiki.

## Handoff

Stop after setup and validation. Summarize the created artifact and recommend one small pilot ingestion as the next separate task. Do not silently begin maintaining the new wiki.
