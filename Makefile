lint:
	poetry run flake8 gendifff

install:
	poetry install

build:
	poetry build

tests:
	poetry run pytest