docker:
	docker build -t tabinv-test .

test: clean
	docker run -v ${PWD}:/tabinv -w /tabinv --name tabinv-test \
		tabinv-test /tabinv/tests/runtests

clean:
	-docker rm tabinv-test

