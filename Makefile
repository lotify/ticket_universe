clean:
	rm -rf ./build ./dist

build: clean
	python3 setup.py sdist bdist_wheel

upload: build
	twine upload dist/*