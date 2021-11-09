install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run coverage run --source=gendiff -m pytest

cc-coverage:
	poetry run coverage xml

run-json:
	poetry run gendiff tests/fixtures/json/file1.json tests/fixtures/json/file2.json

.PHONY: install test lint selfcheck check build
