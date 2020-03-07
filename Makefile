.PHONY: lint test-unit test-behave

install:
	pipenv install

test: lint test-unit test-behave

test: test-unit test-behave

test-unit:
	pipenv run pytest -s

test-behave:
	pipenv run behave

test-e2e:

test-e2e-local:

lint:
	pipenv run flake8

fix-lint:
	./scripts/fix-lint.sh

coverage:
	pipenv run coverage run -m pytest

run-server:
	pipenv run flask run

run-worker: