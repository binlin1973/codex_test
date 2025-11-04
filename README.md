# codex_test
A minimal Python project showing how to use **pytest** and **OpenAI Codex**.
It contains a simple calculator module (`src/calc.py`) and matching tests (`tests/test_calc.py`).
---
## 🧩 Project Structure
```
codex_test/
├── src/
│   ├── __init__.py
│   └── calc.py            # simple add/sub functions
├── tests/
│   └── test_calc.py       # pytest tests
├── pyproject.toml         # pytest configuration
├── Makefile               # convenience tasks
├── AGENTS.md              # repository / contributor guidelines
├── .gitignore             # ignores venv & caches
└── LICENSE
---
## ⚙️ 1. Create and Activate Virtual Environment
### Linux / macOS
```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -U pip pytest
```
### Windows (PowerShell)
```powershell
py -m venv .venv
. .venv\Scripts\Activate.ps1
py -m pip install -U pip pytest
```

> 💡 Virtual environment is local (`.venv/`) — it won’t affect your system Python.
---

## 🧪 2. Run Tests
Once activated and inside the project root:
```bash
python -m pytest -q
```
Expected output:
```
..........                                              [100%]
11 passed in 0.03s
```
If you prefer using the included Makefile (Unix-like systems):
```bash
make test
```
or with explicit virtualenv path:
```bash
.venv/bin/pytest -q
```
## 🤰 3. Configuration Files
### `pyproject.toml`
### `Makefile`
## 🧩 4. Troubleshooting

## 🤖 5. Using OpenAI Codex
If you have the **Codex CLI**, you can let it analyze or modify this repo interactively.
Typical workflow inside project root:
Then instruct it:
Write tests for @src/calc.py using pytest.
Find and fix a bug @src/calc.py
Run tests directly:
python -m pytest -q
