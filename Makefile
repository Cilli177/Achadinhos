.PHONY: install lint test check run

install:
	python -m pip install --upgrade pip
	python -m pip install -e .[dev]

lint:
	ruff check .

test:
	pytest

check: lint test

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
