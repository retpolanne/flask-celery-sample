.PHONY: lint test-unit test-behave

install:
	pip3 install -r requirements.txt

#test: lint test-unit test-behave
#test: lint test-unit

test:

test-unit:
	 python3 -m pytest -s

test-behave:
	 python3 -m behave

test-e2e:

test-e2e-local:

lint:
	 python3 -m flake8

fix-lint:
	./scripts/fix-lint.sh

coverage:
	 python3 -m coverage run -m pytest

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
