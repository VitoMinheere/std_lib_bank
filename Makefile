PYTHON = python3
APP = app
TEST_DIR = test

.PHONY: all test clean lint

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run: ## Run the application
	${PYTHON} -m app.main

test: ## Run tests and display coverage overview
	coverage run -m unittest discover
	coverage report

lint: ## Run black, flake8 and mypy on code and tests
	black ${APP} ${TEST}
	isort  ${APP} ${TEST}
	flake8 ${APP} ${TEST}
	pylint ${APP} ${TEST}
