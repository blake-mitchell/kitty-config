# kitty cheat sheet — build & preview (run from this directory)
#
# Sources (committed):   generate.py  serve.py  Makefile
# Generated (ignored):   out/*.html  out/pdf/*.pdf

CHROME  ?= google-chrome
OUT     := out
PDF      := $(OUT)/pdf
PORT    ?= 7045

# headless Chrome -> PDF (suppress its own header/footer)
render = $(CHROME) --headless --disable-gpu --no-pdf-header-footer \
         --print-to-pdf="$(PDF)/$(2)" "file://$(CURDIR)/$(OUT)/$(1)" >/dev/null 2>&1

.PHONY: all html pdf serve open clean help

all: pdf ## Generate HTML and both PDFs (default)

html: ## Regenerate all HTML from generate.py
	@python3 generate.py

pdf: html ## Render light (print) + dark (screen) PDFs into out/pdf/
	@mkdir -p $(PDF)
	@$(call render,kitty-cheatsheet.html,kitty-cheatsheet.pdf)      # light, print media
	@$(call render,b-terminal-pdf.html,kitty-cheatsheet-dark.pdf)   # dark, full-bleed
	@for f in $(PDF)/*.pdf; do \
	  echo "$$f: $$(pdfinfo "$$f" | awk '/^Pages/{print $$2}') page(s)"; done

serve: html ## Run the live-reload preview server in the foreground (Ctrl+C to stop)
	@echo "live preview: http://127.0.0.1:$(PORT)/kitty-cheatsheet.html"
	@python3 serve.py

open: ## Open the live preview in the default browser (needs `make serve` running)
	@xdg-open http://127.0.0.1:$(PORT)/kitty-cheatsheet.html

clean: ## Remove all generated output
	@rm -rf $(OUT)
	@echo "removed $(OUT)/"

help: ## Show this help
	@grep -hE '^[a-z]+:.*##' $(MAKEFILE_LIST) | \
	  awk -F':.*## ' '{printf "  \033[36m%-9s\033[0m %s\n", $$1, $$2}'
