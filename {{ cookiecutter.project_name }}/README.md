# {{ cookiecutter.project_name }}

<div align="center">

[![Build status](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/workflows/build/badge.svg?branch=master&event=push)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases)
[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENCE)

{{ cookiecutter.project_description }}
</div>

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

4. Run codestyle (codestyle uses `pre-commit`; ensure you've run `make install`):

```bash
make codestyle
```

5. Upload initial code to `GitHub`:

```bash
git add .
git commit -m ":tada: Initial commit"
git remote add origin https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}.git
git push -u origin master
```

### Initial setting up

- Set up [Dependabot](https://github.com/marketplace/dependabot-preview) to enshure you have latest dependencies.
- Set up [Stale bot](https://github.com/apps/stale) for automatic issue closing.

### Poetry

All manipulations with dependencies are executed through Poetry. If you're new to it, look through [the documentation](https://python-poetry.org/docs/).

Poetry's [commands](https://python-poetry.org/docs/cli/#commands) are very intuitive and easy to learn, like:

- `poetry add numpy`
- `poetry run pytest`
- `poetry build`
- etc

### Building your package

Building a new version of the application contains steps:

- Bump the version of your package `poetry version <version>`. You can pass the new version explicitly, or a rule such as `major`, `minor`, or `patch`. For more details, refer to the [Semantic Versions](https://semver.org/) standard.
- Make a commit to `GitHub`.
- Create a `GitHub release`.
- And... publish 🙂 `poetry publish --build`

## What's next

Well, that's up to you. I can only recommend the packages and articles that helped me.

Packages:

- [`Typer`](https://github.com/tiangolo/typer) is great for creating CLI applications.
- [`Rich`](https://github.com/willmcgugan/rich) makes it easy to add  beautiful formatting in the terminal.
- [`FastAPI`](https://github.com/tiangolo/fastapi) is a type-driven asynchronous web framework.
- [`IceCream`](https://github.com/gruns/icecream) is a little library for sweet and creamy debugging

Articles:

- [Open Source Guides](https://opensource.guide/)
- [GitHub Actions Documentation](https://help.github.com/en/actions)
- Maybe you would like to add [gitmoji](https://gitmoji.carloscuesta.me/) to commit names. This is really funny. 😄

## 🚀 Features

For your development we've prepared:

- Supports for `Python 3.7` and higher.
- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/pyproject.toml) and [`setup.cfg`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/setup.cfg).
- Power of [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade) formatters.
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with formatters above.
- Type checks with the configured [`mypy`](https://mypy.readthedocs.io).
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint).
- Security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit).
- Well-made [`.editorconfig`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.editorconfig) and [`.gitignore`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.gitignore). You don't have to worry about those things.

For building and deployment:

- `GitHub` integration.
- [`Makefile`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/Makefile#L89) for building routines. Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc. More details at [Makefile summary](#makefile-usage)).
- [Dockerfile](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/docker/Dockerfile) for your package.
- `Github Actions` with predefined [build workflow](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.github/workflows/build.yml) as the default CI/CD.
- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/) (You will only [need to setup free plan](https://github.com/marketplace/dependabot-preview)).
- Automatic drafts of new release with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). It creates a list of changes based on lables in merged `Pull Requests`. You can see labels (aka `categories`) in [`release-drafter.yml`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.

For creating your open source community:

- Ready-to-use [Pull Requests templates](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/tree/master/.github/ISSUE_TEMPLATE).
- Files such as: `LICENCE.md`, `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` are generated automatically.
- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.github/.stale.yml).
- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).

## Installation

```bash
pip install {{ cookiecutter.project_name }}
```

or install with `Poetry`

```bash
poetry add {{ cookiecutter.project_name }}
```

Then you can run

```bash
{{ cookiecutter.project_name }} --help
```

```bash
{{ cookiecutter.project_name }} --name Roman
```

or if installed with `Poetry`:

```bash
poetry run {{ cookiecutter.project_name }} --help
```

```bash
poetry run {{ cookiecutter.project_name }} --name Roman
```

### Makefile usage

[`Makefile`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/Makefile) contains many functions for fast assembling and convenient work.

<details>
<summary>1. Download Poetry</summary>
<p>

```bash
make download-poetry
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

```bash
make install
```

If you do not want to install pre-commit hooks, run the command with the NO_PRE_COMMIT flag:

```bash
make install NO_PRE_COMMIT=1
```

</p>
</details>

<details>
<summary>3. Check the security of your code</summary>
<p>

```bash
make check-safety
```

This command launches a `Poetry` and `Pip` integrity check as well as identifies security issues with `Safety` and `Bandit`. By default, the build will not crash if any of the items fails. But you can set `STRICT=1` for the entire build, or you can configure strictness for each item separately.

```bash
make check-safety STRICT=1
```

or only for `safety`:

```bash
make check-safety SAFETY_STRICT=1
```

multiple

```bash
make check-safety PIP_STRICT=1 SAFETY_STRICT=1
```

> List of flags for `check-safety` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`.

</p>
</details>

<details>
<summary>4. Check the codestyle</summary>
<p>

The command is similar to `check-safety` but to check the code style, obviously. It uses `Black`, `Darglint`, `Isort` and `Mypy` inside.

```bash
make check-style
```

It may also contain the `STRICT` flag.

```bash
make check-style STRICT=1
```

> List of flags for `check-style` (can be set to `1` or `0`): `STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.

</p>
</details>

<details>
<summary>5. Run all the codestyle formaters</summary>
<p>

Codestyle uses `pre-commit` hooks, so ensure you've run `make install` before.

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
make test && make check-safety && make check-style
```

> List of flags for `lint` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `SAFETY_STRICT`, `BANDIT_STRICT`, `BLACK_STRICT`, `DARGLINT_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.

</p>
</details>

<details>
<summary>8. Build docker</summary>
<p>

```bash
make docker
```

which is equivalent to:

```bash
make docker VERSION=latest
```

More information [here](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup docker</summary>
<p>

```bash
make clean_docker
```

or to remove all build

```bash
make clean
```

More information [here](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/tree/master/docker).

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option you can categorize pull requests in release notes using labels.

For Pull Request this labels are configured, by default:

- Features: `enhancement`, `feature`
- Fixes & Refactoring: `bug`, `refactoring`, `bugfix`, `fix`, `hotfix`
- Build System & CI/CD: `build`, `ci`, `testing`
- Breaking Changes: `breaking`
- Documentation: `documentation`
- Dependencies updates: `dependencies`

You can update it in [`release-drafter.yml`](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.github/release-drafter.yml).

## 🛡 License

[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENCE)

This project is licensed under the terms of the `{{ cookiecutter.license }}` licence. See [LICENSE](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENCE) for more details.

## 📃 Citation

```
{% raw %}@misc{{% endraw %}{{ cookiecutter.project_name }},
  author = {% raw %}{{% endraw %}{{ cookiecutter.organization }}{% raw %}}{% endraw %},
  title = {% raw %}{{% endraw %}{{ cookiecutter.project_description }}{% raw %}}{% endraw %},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}{% raw %}}}{% endraw %}
}
```

## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
