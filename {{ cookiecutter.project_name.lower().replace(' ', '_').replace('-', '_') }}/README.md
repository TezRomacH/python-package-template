# {{ cookiecutter.project_name }}

<div align="center">

[![Build status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/workflows/build/badge.svg?branch=main&event=push)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![License](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

{{ cookiecutter.project_description }}

</div>

## 🚀 Features

- TODO

## Installation

```bash
pip install -U {{ cookiecutter.project_name }}
```

or install with `Poetry`:

```bash
poetry add {{ cookiecutter.project_name }}
```

{% if cookiecutter.create_example_template == 'cli' -%}Then you can run:

```bash
{{ cookiecutter.project_name }} --help
```

or with `Poetry`:

```bash
poetry run {{ cookiecutter.project_name }} --help
```{%- endif %}

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/releases) page. We follow the [Semantic Versioning](https://semver.org/) specification.

## 🛡 License

[![License](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/blob/main/LICENSE)

This project is licensed under the terms of the `{{ cookiecutter.license }}` license. See [LICENSE](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/blob/main/LICENSE) for more details.

## Credits

This project was generated with [`python-package-template`](https://github.com/JensRoland/python-package-template), based on [`python-package-template`](https://github.com/TezRomacH/python-package-template/) by Roman Tezikov.
