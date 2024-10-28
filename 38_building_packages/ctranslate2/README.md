# BUILD CTRANSLATE2 PACKAGE

Build the CTranslate2 package from source.

NOTES:

- Use manylinux to build the packages
- This builds a `pypy` bound package.
- You must be careful that the `python_version` in `Pipfile` must match the python version of the custom package.
- The native dependencies such as `libomp.so` are package with the wheel

## Manylinux

Build using `manylinux` for different versions of python.

```sh
just build manylinux

just start manylinux
```

### Troubleshoot

```sh
just debug manylinux

# inside container
manylinux-interpreters list

manylinux-interpreters ensure-all
```

## Custom Build

Building without manylinux

```sh
just build custom

just start custom
```

## Troubleshooting

```sh
just debug custom
```

## Resources

- github.com/OpenNMT/CTranslate2 [here](https://github.com/OpenNMT/CTranslate2)
- Writing extension modules for pypy [here](https://doc.pypy.org/en/latest/extending.html)
- github.com/qingfengxia/python_wrap [here](https://github.com/qingfengxia/python_wrap)
- CTranslate2 documentation [here](https://opennmt.net/CTranslate2)
- Install from sources [here](https://opennmt.net/CTranslate2/installation.html#install-from-sources)
- Build with many linux https://github.com/OpenNMT/CTranslate2/issues/1654
- https://github.com/pypa/manylinux
- https://www.intel.com/content/www/us/en/developer/tools/oneapi/onemkl-download.html
- https://github.com/pypa/auditwheel
- https://pkgs.org
