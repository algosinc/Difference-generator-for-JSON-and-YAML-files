install:
	poetry install

test:
	poetry run coverage run --source=gendiff -m pytest tests

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml  tests/

cc-coverage:
	poetry run coverage xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check:
	selfcheck test lint

build: check
	poetry build

run-json:
	poetry run gendiff tests/fixtures/json/file1.json tests/fixtures/json/file2.json

.PHONY: install test lint selfcheck check build
