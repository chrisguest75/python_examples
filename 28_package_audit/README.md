# PACKAGE AUDITS

Demonstrate 28_package_audit

TODO:

- renovate/dependabot
- codeql https://github.com/github/codeql
- Bandit - https://github.com/PyCQA/bandit
- complete sonarqube https://github.com/SonarSource/sonarqube

## Contents

- [PACKAGE AUDITS](#package-audits)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Auditing](#auditing)
    - [Safety](#safety)
    - [pip-audit](#pip-audit)
    - [semgrep](#semgrep)
    - [sonarqube](#sonarqube)
  - [Debugging and Troubleshooting](#debugging-and-troubleshooting)
  - [Resources](#resources)

## Prepare

If using `vscode` remember to set your interpreter location to `.venv/bin/python`

## Start

```sh
export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev

# lint and test code
pipenv run format
pipenv run lint
pipenv run test

# enter venv
pipenv shell

# create .env file
cp .env.template .env

# run with arguments
pipenv run start --test
pipenv run start:test
```

## Auditing

### Safety

`pipenv` by default uses safety. By this is not free for commercial packages.

```sh
pipenv check

pipenv check --help

pipenv check --output json
```

### pip-audit

```sh
pipenv run pip-audit --help

pipenv run pip-audit
```

### semgrep

```sh
semgrep --config=r/all .
```

### sonarqube

```sh
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest

http://localhost:9000

username: admin
password: admin
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Resources

- Auditing your python environment [here](https://lewoudar.medium.com/auditing-your-python-environments-406163a59bd1)
- What is Safety DB? [here](https://github.com/pyupio/safety-db)
- Python Packaging Advisory Database [here](https://github.com/pypa/advisory-database)
