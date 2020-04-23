# Package template for Python libraries and CLI apps

<div align="center">

[![Build status](https://github.com/TezRomacH/python-package-template/workflows/test/badge.svg?branch=master&event=push)](https://github.com/TezRomacH/python-package-template/actions?query=workflow%3Atest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/TezRomacH/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

</div>

Yet another cookiecutter template for Python packages.

Mostly built on [wemake-python-package](https://github.com/wemake-services/wemake-python-package) but with [Black formatter](https://github.com/psf/black).

## Features

- Supports `python3.7+`
- [`Poetry`](https://github.com/python-poetry/poetry) dependencies manager
- [`black`](https://github.com/psf/black) formatter
- [`isort`](https://github.com/timothycrosley/isort) for sorting imports
- [`pre-commit`](https://pre-commit.com/) hooks
- Fully typed with annotations and checked with [`mypy`](https://mypy.readthedocs.io)
- Always [up-to-date](https://github.com/TezRomacH/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot) dependencies with the help of [`@dependabot`](https://dependabot.com/)
- `Github Actions` as the default CI

## Installation

Install dependencies:

```bash
pip install -U cookiecutter lice
```

Then, create your package:

```bash
cookiecutter gh:TezRomacH/python-package-template
```

## License

MIT. See [LICENSE](https://github.com/TezRomacH/python-package-template/blob/master/LICENCE) for more details.

## Citation

```
@misc{python-package-template,
  author = {Roman Tezikov},
  title = {Package template for Python libraries and CLI apps},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/TezRomacH/python-package-template}}
}
```
