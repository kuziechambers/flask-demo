SHELL = /bin/sh

define CLEAN
	@@find . -type f -name '*.coverage' -delete
endef

install:
	@ # Uses ---no-root to avoid poetry installing itself as a dependency
	@poetry install --no-root
	@poetry run pre-commit install

clean:
	@rm -vrf .eggs .pytest_cache ./*/__pycache__ ./build ./dist *.pyc *.tgz *.egg-info test-results/ htmlcov/ .pytest_cache
	$(CLEAN)

lint:
	@poetry run pre-commit run --all-files

pylint:
	@echo "Checking for code style. . ."
	@poetry run pylint flask_demo/ \
      --ignore="__main__.py" \
      --load-plugins=pylint.extensions.docparams \
      --accept-no-param-doc=n

mypy:
	@poetry run mypy flask_demo

run:
	@poetry run python -m flask_demo