test:
	pipenv run python -m unittest discover tests
fmt:
	pipenv run autopep8 --in-place --aggressive --aggressive --recursive .
