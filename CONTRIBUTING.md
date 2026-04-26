# Contributing

This is a solo project maintained by [Cam Immesoete](https://github.com/CameronImmesoete). External contributions are not accepted. Pull requests from outside contributors will be closed.

Found a bug or have a feature idea? [Open an issue](../../issues/new/choose).

The standards below document how I contribute to this repo. They exist for consistency, not collaboration.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Branch Naming

```
user/CameronImmesoete/<descriptor>
```

Descriptors are kebab-case, 3-6 words, describe the outcome not the activity.

Good: `user/CameronImmesoete/add-elasticity-calculators`
Bad: `user/CameronImmesoete/fix-stuff`

## Pull Requests

- One PR per branch. One branch per task.
- All PRs start as drafts.
- Never close a PR to open a replacement. Fix in place.
- Squash merge only.
- Branches auto-delete after merge.
- Every PR includes: a summary, what was tested, and what could break.

## Local Validation

Run before every push:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
uv run pytest tests/ -v --tb=short
gitleaks protect --staged --no-banner
```

All must pass. No exceptions.

## CI

All CI checks must be green before merge. No `[skip ci]` commits unless pure documentation. If CI is red on main, fixing it is top priority.

## Commit Messages

Imperative mood, present tense, first line under 72 characters.

Good: `Prevent division by zero in break-even calculator`
Bad: `fix bug` / `Update stuff` / `hopefully this works`

No hedging. No fix-the-fix chains. Squash before opening the PR.

## Security

Secrets are never committed. Gitleaks enforces this as a pre-commit hook.

## Code Quality

| Tool | Purpose | Config |
|------|---------|--------|
| uv | Package management | `pyproject.toml` |
| ruff | Linting and formatting | `pyproject.toml` |
| mypy | Static type checking (strict) | `pyproject.toml` |
| pytest | Testing + coverage | `pyproject.toml` |
| gitleaks | Secret scanning | `.pre-commit-config.yaml` |

Tests required for all new functions. No new dependencies without justification.
