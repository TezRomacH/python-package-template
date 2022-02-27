# Python Packages Project Generator

<div align="center">

[![Build status](https://github.com/JensRoland/python-package-template/workflows/build/badge.svg?branch=master&event=push)](https://github.com/JensRoland/python-package-template/actions?query=workflow%3Abuild)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/JensRoland/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/JensRoland/python-package-template/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/JensRoland/python-package-template/releases)
[![License](https://img.shields.io/github/license/JensRoland/python-package-template)](https://github.com/JensRoland/python-package-template/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Your next Python package needs a bleeding-edge project structure.
</div>

## TL;DR

```bash
cookiecutter gh:JensRoland/python-package-template --checkout v1.2.0
```

## Credit, Improvements & TODOs

This cookiecutter is based on the excellent work by Roman Tezikov <https://github.com/TezRomacH/python-package-template/> and remains 99% his creation. I have merely added some features and removed others to make it more suitable for my own needs.

Specifically, this repo includes the following changes/improvements:

    [x] Added a 'Proprietary' license option.
    [x] Moved source code into /src/ folder and changed all linters etc. to target that folder only.
    [x] Changed the 'github_name' input to 'github_username' to avoid confusion.
    [x] Added virtualenvs.in-project = true (to store virtualenv in project/.venv/)
    [x] Fixed a minor bug (incorrect directory) in the post-gen instructions.
    [x] Bumped a few package versions.
    [x] Added pylint to linters.
    [x] isort: Added list of files to skip.
    [x] black: Removed color=true setting because it broke black when running in my VS Code using formatOnSave (OS X w. ZSH)
    [x] Expanded on the post-gen instructions to include pyenv versioning and GitHub repo creation.
    [x] Fixed `make install` so the created virtualenv will use the selected python version.
    [x] VS Code settings.json: added python defaultInterpreterPath (to auto-activate virtualenv) and activated the various linters and pytest
    [x] VS Code launch.json: enable features for running and debugging code.
    [x] Cleaned up the .pre-commit-config.yaml file a bit, e.g. removing the python version because it made commits fail if you were running a higher (but compatible) Python version.
    [x] Mypy linting of Python code
    [x] Makefile update-dev-deps: black no longer needs prerelease version

And in the future I will add:

    [ ] Makefile -> [`Invoke`](http://www.pyinvoke.org/) / [`Nox`](https://nox.thea.codes/en/stable/)?
    [ ] Auto-documentation with [`MkDocs`](https://www.mkdocs.org/) and possibly [Material Design theme](https://github.com/squidfunk/mkdocs-material) and [`mkdocstrings`](https://github.com/pawamoy/mkdocstrings).
    [ ] Pytest-xdist for parallelized unit test running.
    [ ] CDK constructs ready for deployment to AWS.
    [ ] Code metrics with [`Radon`](https://github.com/rubik/radon).

## 🚀 Features

In this [cookiecutter 🍪](https://github.com/cookiecutter/cookiecutter) template we combine state-of-the-art libraries and best development practices for Python.

### Development features

- Supports `Python 3.7` and higher.
- [`Poetry`](https://python-poetry.org/) as a dependencies manager. See configuration in [`pyproject.toml`](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/pyproject.toml) and [`setup.cfg`](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/setup.cfg).
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort), [`pylint`](https://pylint.org/) and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Ready-to-use [`.editorconfig`](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.editorconfig), [`.dockerignore`](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.dockerignore), and [`.gitignore`](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitignore).
- VS Code settings for automatic virtualenv activation, formatting & linting on save, as well as testing and debugging.

### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/workflows/build.yml) as the default CI/CD.
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile#L89). More details in [makefile-usage](#makefile-usage).
- [Dockerfile](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker/Dockerfile) for your package.
- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/). You only need to [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).
- Automatic release notes with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). You may see the list of labels in [`release-drafter.yml`](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.

### Open source community features

- Ready-to-use [Pull Requests templates](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/JensRoland/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/ISSUE_TEMPLATE).
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/.stale.yml).
- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).

## 🤯 How to use it

### Installation

To begin using the template consider updating `cookiecutter`

```bash
pip install -U cookiecutter
```

then go to a directory where you want to create your project and run:

```bash
cookiecutter gh:JensRoland/python-package-template --checkout v1.2.0
```

### Input variables

Template generator will ask you to fill some variables.

The input variables, with their default values:

|       **Parameter**       |      **Default value**      | **Description**                                                                                                                                                                                     |
| :-----------------------: | :-------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      `project_name`       |      `python-project`       | [Check the availability of possible name](http://ivantomic.com/projects/ospnc/) before creating the project.                                                                                        |
|   `project_description`   | based on the `project_name` | Brief description of your project.                                                                                                                                                                  |
|      `organization`       | based on the `project_name` | Name of the organization. We need to generate LICENCE and to specify ownership in `pyproject.toml`.                                                                                                 |
|         `license`         |            `MIT`            | One of `MIT`, `BSD-3`, `GNU GPL v3.0`, `Apache Software License 2.0`, and `Proprietary`.                                                                                                            |
| `minimum_python_version`  |            `3.7`            | Minimum Python version. One of `3.7`, `3.8` and `3.9`. It is used for builds, GitHub workflow and formatters (`black`, `isort` and `pyupgrade`).                                                    |
|     `github_username`     | based on the `organization` | GitHub username for hosting. Also used to set up `README.md`, `pyproject.toml` and template files for GitHub.                                                                                       |
|          `email`          | based on the `organization` | Email for `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`.                                                                                |
|         `version`         |           `0.1.0`           | Initial version of the package. Make sure it follows the [Semantic Versions](https://semver.org/) specification.                                                                                    |
|       `line_length`       |             120             | The max length per line (used for codestyle with `black` and `isort`). NOTE: This value must be between 50 and 300.                                                                                 |
| `create_example_template` |           `none`            | If `cli` is chosen generator will create simple CLI application with [`Typer`](https://github.com/tiangolo/typer) and [`Rich`](https://github.com/willmcgugan/rich) libraries. One of `cli`, `none` |

All input values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. 😉

#### Demo

[![Demo of github.com/JensRoland/python-package-template](https://asciinema.org/a/422052.svg)](https://asciinema.org/a/422052)

### More details

Your project will contain `README.md` file with instructions for development, deployment, etc. You can read [the project README.md template](https://github.com/JensRoland/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D) before.

### Initial set up

#### Initialize `poetry`

By running `make install`

After you create a project, it will appear in your directory, and will display [a message about how to initialize the project](https://github.com/JensRoland/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D#very-first-steps).

#### Initialize `pre-commit`

By running `make pre-commit-install`. Make sure to set up git first via `git init`.

### Package example

Want to know more about Poetry? Check [its documentation](https://python-poetry.org/docs/).

<details>
<summary>Details about Poetry</summary>
<p>

Poetry's [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry publish --build`

etc.
</p>
</details>

#### CLI example

If you set `create_example_template` to be `cli` the template comes with a cute little CLI application example. It utilises [`Typer`](https://github.com/tiangolo/typer) and [`Rich`](https://github.com/willmcgugan/rich) for CLI input validation and beautiful formatting in the terminal.

After installation via `make install` (preferred) or `poetry install` you can try to play with the example:

```bash
poetry run <project_name> --help
```

```bash
poetry run <project_name> --name Jens
```

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

### Makefile usage

[`Makefile`](https://github.com/JensRoland/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile) contains a lot of functions for faster development.

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

Pre-commit hooks can be installed after `git init` via:

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort`, and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black`, `darglint`, and `pylint`.

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

More information [about docker](https://github.com/JensRoland/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker).

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

## 🎯 What's next

Well, that's up to you 💪🏻. I can only recommend the packages and articles that helped me.

- [`Typer`](https://github.com/tiangolo/typer) is great for creating CLI applications.
- [`Rich`](https://github.com/willmcgugan/rich) makes it easy to add beautiful formatting in the terminal.
- [`Pydantic`](https://github.com/samuelcolvin/pydantic/) – data validation and settings management using Python type hinting.
- [`Loguru`](https://github.com/Delgan/loguru) makes logging (stupidly) simple.
- [`tqdm`](https://github.com/tqdm/tqdm) – fast, extensible progress bar for Python and CLI.
- [`IceCream`](https://github.com/gruns/icecream) is a little library for sweet and creamy debugging.
- [`orjson`](https://github.com/ijl/orjson) – ultra fast JSON parsing library.
- [`Returns`](https://github.com/dry-python/returns) makes you function's output meaningful, typed, and safe!
- [`Hydra`](https://github.com/facebookresearch/hydra) is a framework for elegantly configuring complex applications.
- [`FastAPI`](https://github.com/tiangolo/fastapi) is a type-driven asynchronous web framework.

Articles:

- [Open Source Guides](https://opensource.guide/).
- [A handy guide to financial support for open source](https://github.com/nayafia/lemonade-stand)
- [GitHub Actions Documentation](https://help.github.com/en/actions).
- Maybe you would like to add [gitmoji](https://gitmoji.carloscuesta.me/) to commit names. This is really funny. 😄

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/JensRoland/python-package-template/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               | **Title in Releases**  |
| :-----------------------------------: | :--------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

## 🛡 License

[![License](https://img.shields.io/github/license/JensRoland/python-package-template)](https://github.com/JensRoland/python-package-template/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/JensRoland/python-package-template/blob/master/LICENSE) for more details.

## 🏅 Acknowledgements

This template was inspired by several great articles:

- [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
- [Ultimate Setup for Your Next Python Project](https://martinheinz.dev/blog/14)
- [Nine simple steps for better-looking python code](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf)
- [Modern Python developer's toolkit](https://pycon.switowski.com/)

and repositories:

- [`Cookiecutter`](https://github.com/cookiecutter/cookiecutter)
- [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package)
- [Audreyr's `cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage)
- [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [Cookiecutter Data Science Template: `cdst`](https://github.com/crplab/cdst)

Give them your ⭐️, these resources are amazing! 😉
