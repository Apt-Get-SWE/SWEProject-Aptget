LINTER = flake8
API_DIR = server
DB_DIR = db
REQ_DIR = .
PYTESTFLAGS = -vv --verbose --tb=short

.DEFAULT_GOAL := all

.PHONY: build run clean prod github all_tests unit lint dev_env docs 

all: dev_env build

build:
	cd $(API_DIR) && npm install --prefix frontend && cd frontend && npm run build

run:
	gunicorn server.app:app

clean:
	rm -rf $(API_DIR)/frontend/build

prod: all_tests github

github:
	- git commit -a
	git push origin master

all_tests: lint unit

unit:
	cd $(API_DIR); pytest $(PYTESTFLAGS)

lint:
	autopep8 --in-place --recursive $(API_DIR)/.
	autopep8 --in-place --recursive $(DB_DIR)/.
	$(LINTER) $(API_DIR)/*.py
	$(LINTER) $(DB_DIR)/*.py

dev_env:
	pip install -r $(REQ_DIR)/requirements-dev.txt

docs:
	cd $(API_DIR); make docs