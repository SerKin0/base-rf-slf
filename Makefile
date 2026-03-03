all:
	pip install -r docs/requirements.txt
	sphinx-build -b html docs/source build/html