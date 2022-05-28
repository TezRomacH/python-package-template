#!/bin/bash
find . -name 'coverage.txt' -delete
poetry run pytest --cov-report term --cov hooks tests/ >>.logs/coverage.txt
