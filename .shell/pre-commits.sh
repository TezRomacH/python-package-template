#!/bin/bash
find . -name 'pre-commit.txt' -delete
rm -rf .logs/pre-commit.txt
pre-commit run --all-files
pre-commit run --all-files >>.logs/pre-commit.txt
