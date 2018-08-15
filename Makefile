.PHONY: clean

all: clean test

install:
	env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install -r requirements.txt
	pip install git+https://$(GITHUB_TOKEN)@github.com/datacamp/sqlbackend.git/@v1.0.3
	pip install -e .

clean:
	find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -exec rm -rf {} +
	rm -rf sqlwhat.egg-info

test: clean
	pytest --cov=sqlwhat
	codecov
