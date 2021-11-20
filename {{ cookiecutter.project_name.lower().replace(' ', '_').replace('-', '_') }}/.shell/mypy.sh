#!/bin/bash
find . -name 'mypy.txt' -delete
find . -name 'mypy.svg' -delete
poetry run mypy --config-file pyproject.toml ./ | tee .logs/mypy.txt
export mypy_result=$(grep 'Success' .logs/mypy.txt | cut -d\  -f1 | tr -d ':')
echo "mypy_result:" $mypy_result
rm -rf assets/images/mypy.svg
poetry run python3 -m pybadges --left-text="mypy" --right-color="brightgreen" --right-text=${mypy_result} >>assets/images/mypy.svg
