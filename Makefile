SHELL := /bin/bash

PROJECT_NAME = yatmos
ENVIRONMENT = testing

.PHONY = test build push clean hooks

run: venv
	$(VENV)/uvicorn yatmos.main:app --reload

install: venv

seed:
	ENVIRONMENT=testing $(VENV)/python yatmos/seed.py

test: venv
	ENVIRONMENT=testing $(VENV)/pytest \
		--cov=$(PROJECT_NAME) --cov-report=html --cov-report=term \
		--junit-xml=report.xml \
		tests/

image:
	docker build -t $(PROJECT_NAME) .

build: venv clean
	$(VENV)/python setup.py sdist bdist_wheel

clean:
	rm -rf build dist *.egg-info .pytest_cache htmlcov .coverage sqlite.db
	find . | grep -E '(/__pycache__$$|\.pyc$$|\.pyo$$)' | xargs rm -rf

clean-all: clean clean-venv

include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2020.08.14/Makefile.venv"
	echo "5afbcf51a82f629cd65ff23185acde90ebe4dec889ef80bbdc12562fbd0b2611 *Makefile.fetched" \
		| sha256sum --check - \
		&& mv Makefile.fetched Makefile.venv
