set dotenv-load := true

# default lists actions
default:
  @just -f justfile --list

generate-uv:
  #!/usr/bin/env bash
  set -xeufo pipefail
  cookiecutter $(pwd)/01_simple_cli_cookiecutter_uv -f

generate-pipenv:
  #!/usr/bin/env bash
  set -xeufo pipefail
  cookiecutter $(pwd)/01_simple_cli_cookiecutter -f
  