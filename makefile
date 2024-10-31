APP_NAME = fast-api-rest-todos

PYTHON = python3
PIP = pip
MAIN_APP = main:server

venv:
	$(PYTHON) -m venv venv

activate:
	@echo "source venv/bin/activate" > .env

install: venv
	. venv/bin/activate; $(PIP) install -r requirements.txt

run:
	. venv/bin/activate; uvicorn $(MAIN_APP) --reload

clean:
	rm -rf __pycache__
	rm -rf venv
