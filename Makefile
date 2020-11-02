PKG_NAME := src
PYTHONPATH := $(shell pwd)

run_all:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}"python main.py