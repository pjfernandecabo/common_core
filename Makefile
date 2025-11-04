test:
	pytest -v --maxfail=1 --disable-warnings

run:
	python main.py

lint:
	black --check .
	mypy .

format:
	black .
