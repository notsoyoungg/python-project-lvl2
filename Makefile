lint:
	poetry run flake8 gendifff

install: # установить зависимости
	poetry install

build:
	poetry build