# How to contribute

This is a how-to-contribute guide for the template itself.
This guide is not about contributing to the project that is created
using this template.

## Dependencies

We use `poetry` to manage the [dependencies](https://github.com/python-poetry/poetry).
If you dont have `poetry` installed, you should run the command below.

```bash
make poetry-download
```

To install dependencies and prepare [`pre-commit`](https://pre-commit.com/) hooks you would need to run `install` command:

```bash
make install
make pre-commit-install
```

To activate your `virtualenv` run `poetry shell`.

## Codestyle

After you run `make install` you can execute the automatic code formatting.

```bash
make codestyle
```

### Checks

Many checks are configured for this project. Command `make check-codestyle` will check black, isort and darglint.
The `make check-safety` command will look at the security of your code.

### Before submitting

Before submitting your code please do the following steps:

1. Add any changes you want
1. Add tests for the new changes
1. Edit documentation if you have changed something significant
1. Update `CHANGELOG.md` with a quick summary of your changes
1. Run `make codestyle` to format your changes.
1. Run `make check-codestyle` to ensure that types and docs are correct
1. Run `make check-safety` to ensure that security of your code is correct

## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
