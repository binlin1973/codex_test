# Repository Guidelines

## Project Structure & Module Organization
The `src/` directory houses production code, including the starter `src/calc.py`. Group future modules by feature (`src/auth/`, `src/api/`, etc.) and collect reusable helpers in `src/lib/`. Keep configuration in `config/`, and mirror the production layout inside `tests/` (`src/api/orders.py` → `tests/api/test_orders.py`). Store supporting assets or fixtures in `assets/`, and log additional folders in `docs/structure.md` so the layout stays discoverable.

## Build, Test, and Development Commands
Back common tasks with a `Makefile` or `justfile` so every contributor runs the same workflow. Recommended targets:
- `make bootstrap` — install dependencies declared in `requirements.txt`, `pyproject.toml`, or similar.
- `make lint` — execute formatters and linters (for example `black`, `ruff`) and fail on warnings.
- `make test` — run the automated suite under `tests/` via `python -m pytest`.
- `make serve` — launch the current entry point (for now `python -m src.calc` once the module exposes a CLI).
Place longer scripts inside `scripts/` and invoke them from these targets instead of duplicating logic.

## Coding Style & Naming Conventions
Use four-space indentation and keep lines under 120 characters. Modules stay lowercase with underscores (`data_loader.py`), classes use PascalCase, and functions or variables stick to snake_case. Prefer explicit exports in `__init__.py` (or barrel modules) to control the import surface. Run `black` or the equivalent formatter plus the linter’s autofix mode before committing, and keep tool configuration centralized in the project root to avoid divergence.

## Testing Guidelines
Author unit tests alongside code under `tests/`, naming files with a `_test` suffix. Default to `pytest` (or the primary framework you adopt) and store shared fixtures in `tests/fixtures/`. Target coverage on the critical paths and include regression tests for any bug fix. Run `make test` before every push, and pin integration dependencies in `docker-compose.test.yml`, documenting environment steps in `docs/testing.md`.

## Commit & Pull Request Guidelines
Follow Conventional Commit prefixes (`feat:`, `fix:`, `chore:`, `docs:`) so commit history stays searchable. Keep each commit focused, clean up temporary files, and reference tickets in the body when relevant. Pull requests should include a short summary, screenshots or logs for UI or CLI changes, and links to related issues. Request at least one review, wait for green CI, and use draft PRs for early discussion before promoting them for review.
