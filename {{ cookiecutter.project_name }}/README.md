# {{ cookiecutter.project_name }}

<div align="center">

[![Build status](https://github.com/{{ cookiecutter.git_name }}/{{ cookiecutter.project_name }}/workflows/build/badge.svg?branch=master&event=push)](https://github.com/{{ cookiecutter.git_name }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/{{ cookiecutter.git_name }}/{{ cookiecutter.project_name }}/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

</div>

{{ cookiecutter.project_description }}

## Very first steps

### Initial

1. Initialize `git` inside your repo:

```bash
git init
```

2. If you don't have `Poetry` installed run:

```bash
make download-poetry
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
```

4. Upload initial code to `GitHub`:

```bash
git add .
git commit -m "first commit"
git remote add origin https://github.com/{GITHUB_USER}/{PROJECT_NAME}.git
git push -u origin master
```

### What's next

- Set up [Dependabot](https://github.com/marketplace/dependabot-preview) to enshure you have latest dependencies.
- Set up [Stale bot](https://github.com/apps/stale) for automatic issue closing.

## Features

- Supports `python3.7+`
- [`Poetry`](https://github.com/python-poetry/poetry) dependencies manager
- [`black`](https://github.com/psf/black) formatter
- [`isort`](https://github.com/timothycrosley/isort) for sorting imports
- [`pre-commit`](https://pre-commit.com/) hooks
- Fully typed with annotations and checked with [`mypy`](https://mypy.readthedocs.io)
- `Github Actions` as the default CI

## Installation

```bash
pip install {{ cookiecutter.project_name }}
```

or follow

```bash
poetry add {{ cookiecutter.project_name }}
```

## License

{{ cookiecutter.license }}. See [LICENSE](https://github.com/{{ cookiecutter.git_name }}/{{ cookiecutter.project_name }}/blob/master/LICENCE) for more details.

## Citation

```
{% raw %}@misc{{% endraw %}{{ cookiecutter.project_name }},
  author = {% raw %}{{% endraw %}{{ cookiecutter.organization }}{% raw %}}{% endraw %},
  title = {% raw %}{{% endraw %}{{ cookiecutter.project_description }}{% raw %}}{% endraw %},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/{{ cookiecutter.git_name }}/{{ cookiecutter.project_name }}{% raw %}}}{% endraw %}
}
```

## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
