# {{ cookiecutter.project_name }}

<div align="center">

[![Build status](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/workflows/build/badge.svg?branch=main&event=push)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases)
[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

{{ cookiecutter.project_description }}

</div>

## Very first steps
### Initialize your code
1. Initialize `git` inside your repo:

```bash
cd {{ cookiecutter.project_name }} && git init
```

2. If you don't have `Poetry` installed run:

```bash
make poetry-download
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
make pre-commit-install
```

4. Run the codestyle:

```bash
make codestyle
```

5. Upload initial code to GitHub:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M main
git remote add origin https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}.git
git push -u origin main
```

### Building and releasing your package
Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

### Set up bots
- Set up [Dependabot](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates) to ensure you have the latest dependencies.
- Set up [Stale bot](https://github.com/apps/stale) for automatic issue closing.

### Poetry
Want to know more about Poetry? Check [its documentation](https://python-poetry.org/docs/).

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc
</p>
</details>

## 🚀 Features
### Development features
- Supports for `Python {{ cookiecutter.minimal_python_version }}` and higher.
- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/pyproject.toml) and [`setup.cfg`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/setup.cfg).
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Ready-to-use [`.editorconfig`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/.editorconfig), [`.dockerignore`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/.dockerignore), and [`.gitignore`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/.gitignore). You don't have to worry about those things.

### Deployment features
- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/.github/workflows/build.yml) as the default CI/CD.
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/Makefile#L89). More details in [makefile-usage](#makefile-usage).
- [Dockerfile](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/docker/Dockerfile) for your package.
- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/). You will only [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).

### Open source community features

- Ready-to-use [Pull Requests templates](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/tree/main/.github/ISSUE_TEMPLATE).
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.

## Installation
```bash
pip install -U {{ cookiecutter.project_name }}
```

or install with `Poetry`

```bash
poetry add {{ cookiecutter.project_name }}
```

{% if cookiecutter.create_example_template == 'cli' -%}Then you can run

```bash
{{ cookiecutter.project_name }} --help
```

or with `Poetry`:

```bash
poetry run {{ cookiecutter.project_name }} --help
```{%- endif %}

### Makefile usage

[`Makefile`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

</p>
</details>

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/tree/main/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 📈 Releases
You can see the list of available releases on the [GitHub Releases](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/LICENSE)

This project is licensed under the terms of the `{{ cookiecutter.license }}` license. See [LICENSE](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/main/LICENSE) for more details.

## Credits 
This project was generated with [`python-package-template`](https://github.com/william-cass-wright/cookiecutter-pypackage-slim)
