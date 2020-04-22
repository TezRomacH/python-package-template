SHELL:=/usr/bin/env bash

#! An ugly hack to create individual flags
ifeq ($(STRICT),1)
	POETRY_IGNORE_FLAG =
	PIP_IGNORE_FLAG =
	SAFETY_IGNORE_FLAG =
	BANDIT_IGNORE_FLAG =
	BLACK_IGNORE_FLAG =
	DARGLINT_IGNORE_FLAG =
	MYPY_IGNORE_FLAG =
else
	POETRY_IGNORE_FLAG = -
	PIP_IGNORE_FLAG = -
	SAFETY_IGNORE_FLAG = -
	BANDIT_IGNORE_FLAG = -
	BLACK_IGNORE_FLAG = -
	DARGLINT_IGNORE_FLAG = -
	MYPY_IGNORE_FLAG = -
endif

##! Please tell me how to use `for loops` to create variables in Makefile :(

ifeq ($(POETRY_STRICT),1)
	POETRY_IGNORE_FLAG =
else ifeq ($(POETRY_STRICT),0)
	POETRY_IGNORE_FLAG = -
endif

ifeq ($(PIP_STRICT),1)
	PIP_IGNORE_FLAG =
else ifeq ($(PIP_STRICT),0)
	PIP_IGNORE_FLAG = -
endif

ifeq ($(SAFETY_STRICT),1)
	SAFETY_IGNORE_FLAG =
else ifeq ($SAFETY_STRICT),0)
	SAFETY_IGNORE_FLAG = -
endif

ifeq ($(BANDIT_STRICT),1)
	BANDIT_IGNORE_FLAG =
else ifeq ($(BANDIT_STRICT),0)
	BANDIT_IGNORE_FLAG = -
endif

ifeq ($(BLACK_STRICT),1)
	BLACK_IGNORE_FLAG =
else ifeq ($(BLACK_STRICT),0)
	BLACK_IGNORE_FLAG = -
endif

ifeq ($(DARGLINT_STRICT),1)
	DARGLINT_IGNORE_FLAG =
else ifeq (DARGLINT_STRICT),0)
	DARGLINT_IGNORE_FLAG = -
endif

ifeq ($(MYPY_STRICT),1)
	MYPY_IGNORE_FLAG =
else ifeq ($(MYPY_STRICT),0)
	MYPY_IGNORE_FLAG = -
endif

#! The end of the ugly part. I'm really sorry

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
	$(POETRY_IGNORE_FLAG)poetry check
	$(PIP_IGNORE_FLAG)pip check
	$(SAFETY_IGNORE_FLAG)poetry run safety check --full-report
	$(BANDIT_IGNORE_FLAG)poetry run bandit -r **/*.py

.PHONY: check-style
check-style:
	$(BLACK_IGNORE_FLAG)poetry run black --diff --target-version py37 --check ./
	$(DARGLINT_IGNORE_FLAG)poetry run darglint -v 2 **/*.py
	$(MYPY_IGNORE_FLAG)poetry run mypy --config-file setup.cfg  **/*.py

.PHONY: codestyle
codestyle:
	poetry run pre-commit run --all-files

.PHONY: clean
clean:
	rm -rf build/
