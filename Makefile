.PHONY: test

all: install lint todo

install: 
	pip3 install -r requirements.txt

lint:
	-./build/lint.sh

todo:
	./build/build-todo.sh

test:
	python3 -m unittest discover -v
