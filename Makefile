# Makefile for installing Pygame and running main.py


.PHONY: all install run clear

VENV_DIR = venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip


all: install run


install: 
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install pygame

run:
	$(PYTHON) main.py

clean: 
	rm -rf $(VENV_DIR)
	rm -rf __pycache__
