package-install:
	python3 -m pip install --user --force dist/*.whl

install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

tests:
	poetry run pytest

