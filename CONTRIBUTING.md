# How to contribute

This is a how-to-contribute guide for the template itself.
This guide is not about contributing to the project that is created
using this template.

## Dependencies

We use `poetry` to manage the [dependencies](https://github.com/python-poetry/poetry).
If you dont have `poetry` installed, you should run the command below.

```bash
make download-poetry
```

To install dependencies and prepare [`pre-commit`](https://pre-commit.com/) hooks you would need to run `install` command:

```bash
make install
```
