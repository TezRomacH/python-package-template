SHELL:=/usr/bin/env bash

ifeq ($(STRICT),1)
	SEP =
else
	SEP = -
endif

.PHONY: download-poetry
download-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

.PHONY: install
install:
	poetry lock -n
	poetry install -n
	poetry run pre-commit install

.PHONY: check-safety
check-safety:
	poetry check
	$(SEP)pip check
	$(SEP)poetry run safety check --full-report
	-poetry run bandit -r **/*.py

.PHONY: check-style
check-style:
	$(SEP)poetry run black --diff --target-version py37 --check ./
	$(SEP)poetry run darglint -v 2 **/*.py
	$(SEP)poetry run mypy --config-file setup.cfg  **/*.py

.PHONY: codestyle
codestyle:
	poetry run pre-commit run --all-files

.PHONY: clean
clean:
	rm -rf build/
