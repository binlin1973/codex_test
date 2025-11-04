# Makefile
test:
	/root/codex_env/bin/pytest

lint:
	@echo "add your linter here (e.g. ruff . || eslint .)"

format:
	@echo "add your formatter here (e.g. black .)"
