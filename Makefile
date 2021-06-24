#* Variables
SHELL := /usr/bin/env bash
PYTHON := python

#* Poetry
.PHONY: poetry-download
poetry-download:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) - --uninstall

#* Installation
.PHONY: install
install:
	poetry lock -n && poetry export --without-hashes > requirements.txt
	poetry install -n

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

#* Formatters
.PHONY: codestyle
codestyle:
	poetry run pyupgrade --exit-zero-even-if-changed --py37-plus **/*.py
	poetry run isort --settings-path pyproject.toml hooks tests
	poetry run black --config pyproject.toml hooks tests

.PHONY: formatting
formatting: codestyle

#* Linting
.PHONY: test
test:
	poetry run pytest

.PHONY: check-codestyle
check-codestyle:
	poetry run isort --diff --check-only --settings-path pyproject.toml hooks tests
	poetry run black --diff --check --config pyproject.toml hooks tests
	poetry run darglint --verbosity 2 hooks tests

.PHONY: mypy
mypy:
	poetry run mypy  --install-types --non-interactive --show-traceback --config-file pyproject.toml ./

.PHONY: check-safety
check-safety:
	poetry check
	poetry run safety check --full-report
	poetry run bandit -ll --recursive hooks

.PHONY: lint
lint: test check-codestyle mypy check-safety

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: clean-all
clean-all: pycache-remove build-remove
