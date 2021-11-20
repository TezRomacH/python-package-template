#!/bin/bash
find . -name 'safety.txt' -delete
find . -name 'vulnerabilities.svg' -delete
poetry run safety check -o .logs/safety.txt
export vulnerabilities=$(grep 'vulnerabilities' .logs/safety.txt | cut -d\  -f2)
echo "vulnerabilities:" $vulnerabilities
rm -rf assets/images/vulnerabilities.svg
poetry run python3 -m pybadges --left-text="vulnerabilities" --right-text=${vulnerabilities} --left-color="#40aef9" --right-color="#0c2739" --logo=assets/images/safety.png --embed-logo >>assets/images/vulnerabilities.svg
