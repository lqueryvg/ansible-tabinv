docker:
	docker build -t tabinv-test .

test: clean
	docker run -v ${PWD}:/tabinv -w /tabinv/tests \
		--name tabinv-test tabinv-test ./runtests

clean:
	-docker rm tabinv-test

