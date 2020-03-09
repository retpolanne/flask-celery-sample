.PHONY: lint test-unit test-behave

install:
	pip install -r requirements.txt

#test: lint test-unit test-behave
test: lint test-unit

test-unit:
	 pytest -s

test-behave:
	 behave

test-e2e:

test-e2e-local:

lint:
	 flake8

fix-lint:
	./scripts/fix-lint.sh

coverage:
	 coverage run -m pytest

run-server:
	 flask run

run-server-prod:
	 uwsgi --http 0.0.0.0:${PORT} --module sample_app:app

run-worker:

docker-build:
	docker build . -t ${TAG}

docker-run:
	docker run ${TAG} ${COMMAND}

docker-push:
	docker push ${TAG}

deploy-k8s:
	kubectl apply -k kustomize
