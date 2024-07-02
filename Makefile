# init:
# 	pip install -r requirements.txt

lint:
    ruff format .
	ruff check . --fix