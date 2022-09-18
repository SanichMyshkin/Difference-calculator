pi:
	python3 -m pip install --user --force dist/*.whl

install:
	poetry install

build:
	poetry build