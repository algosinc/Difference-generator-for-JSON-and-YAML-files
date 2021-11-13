install:
	poetry install

test:
	poetry run coverage run --source=gendiff -m pytest

cc-coverage:
	poetry run coverage xml

lint:
	# stop the build if there are Python syntax errors or undefined names
    poetry run flake8 --count --select=E9,F63,F7,F82 --show-source --statistics gendiff
    # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
    poetry run flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics gendiff

selfcheck:
	poetry check

check:
	selfcheck test lint

build: check
	poetry build

run-json:
	poetry run gendiff tests/fixtures/json/file1.json tests/fixtures/json/file2.json

.PHONY: install test lint selfcheck check build
