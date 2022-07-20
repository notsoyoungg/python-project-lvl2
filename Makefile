lint:
	poetry run flake8 gendifff

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

tests:
	poetry run pytest

test-cov:
	poetry run pytest --cov=gendifff tests/ --cov-report xml