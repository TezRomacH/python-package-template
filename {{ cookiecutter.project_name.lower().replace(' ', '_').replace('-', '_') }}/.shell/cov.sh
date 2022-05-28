#!/bin/bash
find . -name 'coverage.txt' -delete
poetry run pytest --cov-report term --cov {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} tests/ >>.logs/coverage.txt
