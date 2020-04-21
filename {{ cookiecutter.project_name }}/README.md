# {{ cookiecutter.project_name }}

<p align="center">

[![Build status](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/workflows/test/badge.svg?branch=master&event=push)](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Atest)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)

</p>

{{ cookiecutter.project_description }}

## Installation

```bash
pip install {{ cookiecutter.project_name }}
```

or follow

```bash
poetry add {{ cookiecutter.project_name }}
```

## License

{{ cookiecutter.license }}. See [LICENSE](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/blob/master/LICENCE) for more details.

## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
