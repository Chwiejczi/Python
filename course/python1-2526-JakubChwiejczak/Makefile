# Zmienne
PYTHON = python
MAMBA = mamba
RUFF = ruff
PYTEST = pytest
ENV_NAME = python1course-env

# Domyślny target
.PHONY: help
help:
	@echo "Dostępne komendy:"
	@echo "  make env              - Utwórz środowisko i zainstaluj pre-commit"
	@echo "  make lock-file        - Wygeneruj pliki conda-lock"
	@echo "  make conda-lock-install - Zainstaluj środowisko z lock file"
	@echo "  make setup-pre-commit - Zainstaluj pre-commit hooks"
	@echo "  make lint             - Sprawdź kod używając ruff"
	@echo "  make format           - Sformatuj kod"
	@echo "  make test             - Uruchom testy"
	@echo "  make clean            - Usuń pliki tymczasowe"
	@echo "  make recreate-env     - Usuń i odtwórz środowisko" 


	@echo "  make build            - Zbuduj pakiet (dist/)"
	@echo "  make install-editable - Zainstaluj pakiet w trybie edytowalnym"
	@echo "  make pre-release      - Pełny proces przed publikacją"

# Generowanie lock files
.PHONY: lock-file
lock-file:
	conda-lock --mamba -f env.yml -f env-dev.yml --lockfile conda-lock-dev.yml
	conda-lock --mamba -f env.yml --lockfile conda-lock.yml

# Instalacja środowiska z lock file
.PHONY: conda-lock-install
conda-lock-install:
	conda-lock install --mamba -n $(ENV_NAME) conda-lock-dev.yml

# Instalacja pre-commit
.PHONY: setup-pre-commit
setup-pre-commit:
	pre-commit install

# Stwórz środowisko
.PHONY: env
env: conda-lock-install

# Linting
.PHONY: lint
lint:
	$(RUFF) check .

# Formatowanie
.PHONY: format
format:
	$(RUFF) format .
	$(RUFF) check --fix .

# Testy
.PHONY: test
test:
	$(PYTEST) tests/

# Czyszczenie
.PHONY: clean
clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Usunięcie środowiska
.PHONY: remove-env
remove-env:
	mamba env remove -n $(ENV_NAME)

# Odtworzenie środowiska od zera
.PHONY: recreate-env
recreate-env: remove-env lock-file env
	@echo "Środowisko zostało odtworzone!" 

# Budowanie pakietu
.PHONY: build
build:
	$(PYTHON) -m build

# Instalacja pakietu w trybie edytowalnym
.PHONY: install-editable
install-editable:
	pip install -e .

# Pełny proces przed publikacją
.PHONY: pre-release
pre-release: lint format test build
	@echo "Gotowe do publikacji!"