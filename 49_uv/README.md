# UV

A little example of using UV.

NOTES:

- It is very quick at installing packages.

## Install

```sh
just nix
```

## Start

```sh
just lint

just format

just test

just start --test
```

## Created

When installing a fresh UV project.

```sh
# create a basic skeleton
uv init .

# add packages
uv add pyyaml

# add dev
uv add --dev flake8-2020
```

## Resources

- An extremely fast Python package and project manager, written in Rust. [here](https://docs.astral.sh/uv/)
- https://github.com/astral-sh/uv
- https://www.datacamp.com/tutorial/python-uv
  https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile
