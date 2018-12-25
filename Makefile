.PHONY: test

all: install lint todo

install: 
	python3 install.py

lint:
	-./build/lint.sh

todo:
	./build/build-todo.sh

test:
	python3 -m unittest discover -v
