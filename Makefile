.PHONY: test

all: install lint

install: 
	pip3 install -r requirements.txt

lint:
	-./build/lint.sh

test:
	python3 -m unittest discover -v

executable:
	pyinstaller run.py --onefile --noconsole
