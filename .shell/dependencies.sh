#!/bin/bash
find . -name 'dependencies.txt' -delete
poetry install -n >>.logs/dependencies.txt
