pi:
	python3 -m pip install --user --force dist/*.whl

install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 gendiff

test-install:
	pip install pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

pytest:
	poetry run pytest

