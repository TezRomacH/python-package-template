#!/bin/bash
echo start
sh .shell/pylint.sh
sh .shell/mypy.sh
sh .shell/safety.sh
sh .shell/complexity.sh
sh .shell/maintainability.sh
sh .shell/cov.sh
sh .shell/dependencies.sh
sh .shell/docstring.sh
