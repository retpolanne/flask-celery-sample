.PHONY: lint test-unit test-behave

install:
	pipenv install
# TODO fix lint
#test: lint test-unit test-behave

test: test-unit test-behave

test-unit:
	pipenv run pytest -s

test-behave:
	pipenv run behave

test-e2e:

test-e2e-local:

lint:
	find . -type f -name "*.py" -exec pipenv run pylint --load-plugins pylint_flask {} \;

run-server:
	pipenv run flask run

run-worker: