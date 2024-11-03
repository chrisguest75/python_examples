# BUILD CUSTOM PACKAGE

Build the custom package package from source.

## Manylinux

Build using `manylinux` for different versions of python.

```sh
just build

just start
```

### Troubleshoot

```sh
just debug

# inside container
manylinux-interpreters list

manylinux-interpreters ensure-all
```

## Resources

- https://github.com/pypa/python-manylinux-demo
- https://github.com/math-atlas/math-atlas/tree/master
- https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py
- https://python.readthedocs.io/en/v2.7.2/extending/building.html
