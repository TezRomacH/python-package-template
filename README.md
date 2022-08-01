# cookiecutter pypackage slim

## Summary
### Purpose
- cookiecutter template for creating python packages with modern project structure
- accelerate your package development cycle and create more with software!
- for a step-by-step guide on building a non-templated package, see [this blog post](https://mathspp.com/blog/how-to-create-a-python-package-in-2022) by [Rodrigo Girão Serrão](https://github.com/rodrigogiraoserrao)

### Key components:
- docker
- makefile
- versioning
	- poetry
	- bump2version
- github actions
	- run tests
	- deploy to PyPI
	- dependabot
	- mkdocs/[readthedocs] (*TODO*)
- testing
	- black
	- tox
	- pytest
	- isort
	- mypy
	- flake8
- docs
	- bug report
	- feature request
	- questions
	- pull request
	- license
	- changelog
	- code of conduct
	- contributing
	- security

[readthedocs]: https://github.com/readthedocs/readthedocs.org

## Quick Start
- create github repo 
- clone locally & run cookiecutter
```bash
git clone git@github.com:william-cass-wright/<project_name>.git
cookiecutter https://github.com/william-cass-wright/cookiecutter-pypackage-slim.git _<project_name>
```
- create branch in cloned repo
- copy/paste cookiecutter contents
- setup with makefile
```bash
make poetry-download # if poetry isn't already installed
make install
make pre-commit-install
make test
make codestyle
```

- git add commit and push
	- this will automatically run `build` workflow
- add test [pypi token] to repo secrets

| Name | Value |
| ---- | ---- |
| TEST_PYPI_API_TOKEN | `pypi-<alphanumeric string>` |

- merge branch or manually trigger `stage & preview workflow` 

[pypi token]: https://pypi.org/help/#apitoken

## Background
- this project drew inspiration from previous work:
	- [TezRomacH/python-package-template]
	- [waynerv/cookiecutter-pypackage]
	- [wemake-services/wemake-python-package]
- a number of repos were analyzed: [REFERENCES.md]
- cool tool used to [search cookiecutter templates on github]

[TezRomacH/python-package-template]: https://github.com/TezRomacH/python-package-template
[waynerv/cookiecutter-pypackage]: https://github.com/waynerv/cookiecutter-pypackage
[wemake-services/wemake-python-package]: https://github.com/wemake-services/wemake-python-package
[REFERENCES.md]: /references/REFERENCES.md
[search cookiecutter templates on github]:http://cookiecutter-templates.sebastianruml.name/