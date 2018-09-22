.DEFAULT_GOAL := help
OPEN=$(word 1, $(wildcard /usr/bin/xdg-open /usr/bin/open))

.PHONY: help
help: ## Print the help message
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%s\033[0m : %s\n", $$1, $$2}' $(MAKEFILE_LIST) | \
		sort | \
		column -s ':' -t

.PHONY: clean
clean: ## Clean all generated resources
	@git clean -X -d -f

.PHONY: lint
lint: ## Run the linters
	@flake8

.PHONY: test
test: ## Run the tests with any python3 interpreter
	@tox

.PHONY: docs
docs: ## Build the docs
	@$(MAKE) -C docs html

.PHONY: bandit
bandit: ## Run the static code analyzer
	@bandit -r flask_fontawesome

.PHONY: all
all: lint bandit docs test ## Run all lints and tests

.PHONY: publish
publish: clean all ## Upload the package to PyPI
	@python3 setup.py sdist bdist_wheel && \
		twine upload dist/*

.PHONY: open-coverage-report
open-coverage-report: ## Open the coverage report in your browser
	@$(OPEN) htmlcov/index.html

.PHONY: open-docs
open-docs: ## Open the generated docs in your browser
	@$(MAKE) -C docs open

.PHONY: run
run: ## Run the sample app
	@./run_example.py
