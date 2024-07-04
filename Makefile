.PHONY: virtualenv activate install main

venv:
	@test -d venv || virtualenv venv

freeze: 
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Please activate the virtualenv first"; \
		echo "by running command: source venv/bin/activate"; \
		exit 1; \
	else \
		venv/bin/pip freeze > requirements.txt; \
	fi

install:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Please activate the virtualenv first"; \
		echo "by running command: source venv/bin/activate"; \
		exit 1; \
	else \
		venv/bin/pip install -r requirements.txt; \
	fi

main:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Please activate the virtualenv first"; \
		echo "by running command: source venv/bin/activate"; \
		exit 1; \
	else \
		./venv/bin/python main.py; \
	fi