PY_VERSION=3.8.10
PYENV_NAME=adventofcode
PYENV=~/.pyenv/versions/${PY_VERSION}/envs/${PYENV_NAME}/bin

build-dev:
	pyenv uninstall -f ${PYENV_NAME}
	pyenv install -s ${PY_VERSION}
	pyenv virtualenv -f ${PY_VERSION} ${PYENV_NAME}
	${PYENV}/pip install --no-cache-dir -U pip
	${PYENV}/pip install --no-cache-dir -U pip-tools
	${PYENV}/pip install --no-cache-dir -e ".[dev]"

install-dev:
	pip install -U pip
	pip install -U pip-tools
	PIP_CONFIG_FILE=pip.conf pip install -e ".[dev]"

lint:
	python -m flake8 src/ tests/

coverage:
	python -m coverage run --source=src --branch -m pytest -sv tests/ --junitxml=build/test.xml -v
	python -m coverage xml -i -o build/coverage.xml
	python -m coverage report --omit=*/main.py

test: lint coverage
