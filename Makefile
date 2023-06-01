install:
	poetry install 

format:
	isort .
	blue .

lint:
	blue . --check
	isort . --check 
	prospector --with-tool pep257 --docs-warning

test:
	pytest