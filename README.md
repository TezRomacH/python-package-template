# Python Packages Project Generator

<div align="center">

[![Build status](https://github.com/TezRomacH/python-package-template/workflows/build/badge.svg?branch=master&event=push)](https://github.com/TezRomacH/python-package-template/actions?query=workflow%3Abuild)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/TezRomacH/python-package-template/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/TezRomacH/python-package-template/releases)
[![License](https://img.shields.io/github/license/TezRomacH/python-package-template)](https://github.com/TezRomacH/python-package-template/blob/master/LICENSE)

Your next Python package needs a bleeding-edge project structure.
</div>

## TL;DR

```bash
cookiecutter gh:TezRomacH/python-package-template
```

## 🚀 Features

In this [cookiecutter 🍪](https://github.com/cookiecutter/cookiecutter) template, we aimed to combine the most state-of-the-art libraries and best development practices for Python.

For your development we've prepared:

- Supports for `Python 3.7` and higher.
- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/pyproject.toml) and [`setup.cfg`](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/setup.cfg).
- Power of [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade) formatters.
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with formatters above.
- Type checks with the pre-configured [`mypy`](https://mypy.readthedocs.io).
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint).
- Security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit).
- Well-made [`.editorconfig`](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.editorconfig), [`.dockerignore`](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.dockerignore), and [`.gitignore`](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.gitignore). You don't have to worry about those things.

For building and deployment:

- `GitHub` integration.
- [`Makefile`](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile#L89) for building routines. Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc. More details at [Makefile summary](#makefile-usage)).
- [Dockerfile](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker/Dockerfile) for your package.
- `Github Actions` with predefined [build workflow](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/workflows/build.yml) as the default CI/CD.
- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/) (You will only [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates)).
- Automatic drafts of new releases with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). It creates a list of changes based on labels in merged `Pull Requests`. You can see labels (aka `categories`) in [`release-drafter.yml`](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.

For creating your open source community:

- Ready-to-use [Pull Requests templates](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/ISSUE_TEMPLATE).
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/.github/.stale.yml).
- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).

## 🤯 How to use it

### Installation

Before creating a new project from this template, you need to install the dependency:

```bash
pip install -U cookiecutter
```

Go to the directory where you want to create your project and run:

```bash
cookiecutter gh:TezRomacH/python-package-template
```

### Input variables

The `cookiecutter generator`  will ask you for some data, you might want to have at hand before generating the project.

The input variables, with their default values (some auto-generated), are:

|     **Parameter**     |      **Default value**      | **Description**                                                                                                                                                               |
|:---------------------:|:---------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project_name`           | `python-project`            | The name of the project. It might be a good idea to  [check the availability of such name](http://ivantomic.com/projects/ospnc/) before creating the project. |
| `project_description`    | based on the `project_name` | Brief description of your project. |
| `organization`           | based on the `project_name` | Name of the organization. This is needed to generate the license file and to specify the ownership of the project in `pyproject.toml`. |
| `license`                | `MIT`                       | Type of license. One of `MIT`, `BSD-3`, `GNU GPL v3.0` and `Apache Software License 2.0`. |
| `minimal_python_version` | `3.7`                       | Minimal Python version for your project. One of `3.7`, `3.8` and `3.9`. Used for builds, GitHub workflow and formatters (`black`, `isort` and `pyupgrade`). |
| `github_name`            | based on the `organization` | GitHub username where the package will be hosted. The cookiecutter will use this name to correctly configure the `README.md`, `pyproject.toml` and template files for GitHub. |
| `email`                  | based on the `organization` | Email is needed for generating the `CODE_OF_CONDUCT.md`, `SECURITY.md` files and to specify the ownership of the project in `pyproject.toml`. |
| `version`                | `0.1.0`                     | An initial version of the package. Make sure it follows the [Semantic Versions](https://semver.org/) specification. |
| `line_length`             | 88                         | The max length per line (used for autoformatting with `black` and `isort`). NOTE: This value must be between 50 and 300. |

The entered values will be saved in the `cookiecutter-config-file.yml` file so that you won't lose them. 😉

#### Demo

[![Demo of github.com/TezRomacH/python-package-template](https://asciinema.org/a/422052.svg)](https://asciinema.org/a/422052)

#### More details

After using this generator, your new project (the directory created) will contain an extensive `README.md` with instructions for development, deployment, etc. You can read [the project `README.md` template](https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D) before.

### Initial setting up

#### Initialize `poetry` and `pre-commit`

By running `make install`

After you run the cookiecutter command and the project appears in your directory, the console will display [a message about how to initialize the project](https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D#very-first-steps).

#### Package example

All manipulations with dependencies are executed through Poetry. If you're new to it, look through [the documentation](https://python-poetry.org/docs/).

<details>
<summary>Notes about Poetry</summary>
<p>

Poetry's [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:

- `poetry add numpy@latest`
- `poetry run pytest`
- `poetry build`
- etc

</p>
</details>

The template comes with a cute little CLI application example. It uses [`Typer`](https://github.com/tiangolo/typer) to CLI and [`Rich`](https://github.com/willmcgugan/rich) for beautiful formatting in the terminal output.

After installation via `make install` (preferred) or `poetry install` you can try to play with the example:

```bash
poetry run <project_name> --help
```

```bash
poetry run <project_name> --name Roman
```

### Building and releasing your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

### Makefile usage

[`Makefile`](https://github.com/TezRomacH/python-package-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/Makefile) contains many functions for fast assembling and convenient work.

<details>
<summary>1. Download Poetry</summary>
<p>

```bash
make poetry-download
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

```bash
make install
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Check the security of your code</summary>
<p>

```bash
make check-safety
```

This command launches a `Poetry` and `Pip` integrity check as well as identifies security issues with `Safety` and `Bandit`. By default, the build will not crash if any of the items fail.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>4. Check the codestyle</summary>
<p>

The command is similar to `check-safety` but to check the code style, obviously. It uses `Black`, `Darglint`, `Isort`, and `Mypy` inside.

```bash
make check-codestyle
```

</p>
</details>

<details>
<summary>5. Run all the codestyle formaters</summary>
<p>

Ensure you've run `make install` before.

```bash
make codestyle
```

</p>
</details>

<details>
<summary>6. Run tests</summary>
<p>

```bash
make test
```

</p>
</details>

<details>
<summary>7. Run all the linters</summary>
<p>

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
<summary>8. Build docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

More information [about docker](https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/TezRomacH/python-package-template/tree/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker).

Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Or to remove all of this

```bash
make clean-all
```
</p>
</details>

## 🎯 What's next

Well, that's up to you. I can only recommend the packages and articles that helped me.

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
- [GitHub Actions Documentation](https://help.github.com/en/actions).
- Maybe you would like to add [gitmoji](https://gitmoji.carloscuesta.me/) to commit names. This is really funny. 😄

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/TezRomacH/python-package-template/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

For Pull Request we configured this labels:

|               **Label**               |  **Title in Releases**  |
|:-------------------------------------:|:----------------------:|
| `enhancement`, `feature`              | 🚀 Features             |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
| `build`, `ci`, `testing`              | 📦 Build System & CI/CD |
| `breaking`                            | 💥 Breaking Changes     |
| `documentation`                       | 📝 Documentation        |
| `dependencies`                        | ⬆️ Dependencies updates |

## 🧪 TODOs

This template will continue to develop and follow the bleeding edge new tools and best practices to improve the Python development experience.

Here is a list of things that have yet to be implemented:

- Add examples of libraries created using this template.
- Tests coverage reporting ([`Codecov`](https://github.com/marketplace/codecov) ?).
- Auto uploading your package to [`PyPI`](https://pypi.org/).
- Automatic creation and deployment of documentation to GitHub pages (I'm mostly looking at [`MkDocs`](https://www.mkdocs.org/) with [Material Design theme](https://github.com/squidfunk/mkdocs-material) and [`mkdocstrings`](https://github.com/pawamoy/mkdocstrings)).
- Code metrics with [`Radon`](https://github.com/rubik/radon).
- Docstring coverage with [`interrogate`](https://github.com/econchick/interrogate)
- `Dockerfile` linting with [`dockerfilelint`](https://github.com/replicatedhq/dockerfilelint).
- [Hall of fame](https://github.com/sourcerer-io/hall-of-fame) from `Sourcerer`.
- Some advanced Python linting (?).
- End-to-end testing and validation of the cookiecutter template.

## 🛡 License

[![License](https://img.shields.io/github/license/TezRomacH/python-package-template)](https://github.com/TezRomacH/python-package-template/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/TezRomacH/python-package-template/blob/master/LICENSE) for more details.

## 🏅 Acknowledgements

This template was inspired by those great articles:

- [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)
- [Ultimate Setup for Your Next Python Project](https://martinheinz.dev/blog/14)
- [Nine simple steps for better-looking python code](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf)

and repositories:

- [`Cookiecutter`](https://github.com/cookiecutter/cookiecutter)
- [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package)
- [Audreyr's `cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage)
- [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [Cookiecutter Data Science Template: `cdst`](https://github.com/crplab/cdst)

Give them your ⭐️, these resources are amazing! 😉

## 📃 Citation

```bibtex
@misc{python-package-template,
  author = {Roman Tezikov},
  title = {Python Packages Project Generator},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/TezRomacH/python-package-template}}
}
```

Markdown source for the badge [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

```markdown
[![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)
```
