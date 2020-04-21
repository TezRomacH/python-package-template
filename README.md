# Package template for Python libraries and CLI apps

<p align="center">

[![Build status](https://github.com/TezRomacH/python-package-template/workflows/test/badge.svg?branch=master&event=push)](https://github.com/TezRomacH/python-package-template/actions?query=workflow%3Atest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</p>

Yet another cookiecutter template for Python packages.

Mostly built on [wemake-python-package](https://github.com/wemake-services/wemake-python-package) but with [Black formatter](https://github.com/psf/black).

## Features

- Supports latest `python3.7+`
- [`Poetry`](https://github.com/python-poetry/poetry) dependencies manager
- [`black`](https://github.com/psf/black) formatter
- [`isort`](https://github.com/timothycrosley/isort) for sorting imports
- [`pre-commit`](https://pre-commit.com/) hooks
- [`mypy`](https://mypy.readthedocs.io) for optional static typing

## Installation

```bash
pip install cookiecutter lice
```

```bash
cookiecutter gh:TezRomacH/python-package-template
```

## License

MIT. See [LICENSE](https://github.com/TezRomacH/python-package-template/blob/master/LICENCE) for more details.
