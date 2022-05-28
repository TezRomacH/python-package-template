#!/bin/bash
find . -name 'docstring.txt' -delete
interrogate -v hooks >>.logs/docstring.txt
poetry run interrogate hooks
