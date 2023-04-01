 
# If there is a file/folder with the same name as a make command,
# add the command name to .PHONY (separated by spaces)
# so make will ignore the file/folder and always run the command
.PHONY: tests

example:
	python vizcurse -i example.py

fix-subdependencies:
	pipenv lock --pre --clear

install:
	pipenv install

lint:
	pipenv run black ./vizcurse ./tests

profile:
	# pipenv run python tests/performance || python tests/performance
	make setup
	python3 tests/performance

setup:
	ln -s ../../vizcurse/ tests/performance || true

tests:
	pipenv run black --check ./vizcurse ./tests
	#TESTING=1 pipenv run pytest -s --disable-warnings tests/unit_test.py
	#TESTING=1 pipenv run pytest -s --disable-warnings tests/integration_test.py
	#TESTING=1 pipenv run pytest --disable-warnings tests/test.py

viz-c:
	clear && gcc vizcurse.c -lm && ./a.out
