#!/bin/bash
find . -name 'docstring.txt' -delete
interrogate -v {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} >>.logs/docstring.txt
poetry run interrogate {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}
