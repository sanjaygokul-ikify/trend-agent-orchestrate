dev:
	python -m venv env && . env/bin/activate && pip install -e .[dev]
test:
	tpython -m pytest tests/
lint:
	noqa linter
format:
	black .
deploy:
	poetry publish