clean:
	rm -rf ./build ./dist

build: clean
	python3 setup.py sdist bdist_wheel

upload-test: build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload: build
	twine upload dist/*
