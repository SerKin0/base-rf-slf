all:
	pip install -r docs/requirements.txt
	python tables/create_table.py
	sphinx-build -b html docs/source build/html