# Agent Guidelines

## PR Rules
- One PR per branch, one branch per task
- Never close a PR to open a replacement. Fix in place.
- Never push directly to main
- Squash merge only
- Branches auto-delete after merge
- Branch naming: `user/<username>/<description>` or `feature/<description>`

## CI Requirements
- All CI checks must pass before merge
- No `[skip ci]` commits unless pure documentation
- If CI is red on main, fix it before other work

## Security
- Never commit secrets, API keys, tokens, or credentials
- Never add dependencies without justification
- Never force push to main
- Run tests before pushing

## Code Quality
- Tests required for all new functions
- Lint must pass (ruff for Python, eslint for TypeScript)
- Type checks must pass (mypy for Python, tsc for TypeScript)
