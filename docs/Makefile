OPEN=$(word 1, $(wildcard /usr/bin/xdg-open /usr/bin/open))
.DEFAULT_GOAL := help

BUILD_DIR := _build/
API_DIR := api/

.PHONY: help
help: ## Print the help message
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%s\033[0m : %s\n", $$1, $$2}' $(MAKEFILE_LIST) | \
		sort | \
		column -s ':' -t

.PHONY: init
init:
	@mkdir -p $(BUILD_DIR) && \
		sphinx-apidoc --force --module-first --separate -o $(API_DIR) ../flask_fontawesome/

.PHONY: html
html: init ## Render the docs to HTML
	@sphinx-build -b html . $(BUILD_DIR)

.PHONY: serve
serve: init ## Run a server and serve the documentation
	@sphinx-autobuild -i '*~' -i '*.swp' -H 127.0.0.1 -p 8000 . $(BUILD_DIR)

.PHONY: open
open: ## Open the generated docs in your browser
	@$(OPEN) $(BUILD_DIR)/index.html
