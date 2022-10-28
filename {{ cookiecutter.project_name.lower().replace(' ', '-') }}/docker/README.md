# Docker for {{ cookiecutter.project_name }}

## Installation

To create Docker you need to run:

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

You may provide name and version for the image.
Default name is `IMAGE := {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}`.
Default version is `VERSION := latest`.

```bash
make docker-build IMAGE=some_name VERSION={{ cookiecutter.version }}
```

## Usage

```bash
docker run -it --rm \
   -v $(pwd):/workspace \
   {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} bash
```

## How to clean up

To uninstall docker image run `make docker-remove` with `VERSION`:

```bash
make docker-remove VERSION={{ cookiecutter.version }}
```

you may also choose the image name

```bash
make docker-remove IMAGE=some_name VERSION=latest
```

If you want to clean all, including `build` and `pycache` run `make cleanup`
