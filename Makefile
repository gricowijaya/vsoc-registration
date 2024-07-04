.PHONY: virtualenv activate install main

venv:
	@test -d venv || virtualenv venv

freeze: 
	venv/bin/pip freeze > requirements.txt

install:
	venv/bin/pip install -r requirements.txt

main:
	./venv/bin/python main.py
