# BUILD CTRANSLATE2 PACKAGE

Build the CTranslate2 package from source.

TODO:

* The generated wheel does not contain the native libs (investigate manylinux).  

NOTES:

* This builds a `pypy` bound package.  

## Build

```sh
# build container and build the code
docker build --progress=plain -t 38_build_ctranslate2 .

# generate the package
mkdir -p ./out
docker run -it --rm -v ./out:/out 38_build_ctranslate2 
```

## Troubleshooting

```sh
docker run -it --rm --entrypoint /bin/bash 38_build_ctranslate2 
```

## Resources

- github.com/OpenNMT/CTranslate2 [here](https://github.com/OpenNMT/CTranslate2)
- Writing extension modules for pypy [here](https://doc.pypy.org/en/latest/extending.html)
- github.com/qingfengxia/python_wrap [here](https://github.com/qingfengxia/python_wrap)
- CTranslate2 documentation [here](https://opennmt.net/CTranslate2)
- Install from sources [here](https://opennmt.net/CTranslate2/installation.html#install-from-sources)
- Build with many linux https://github.com/OpenNMT/CTranslate2/issues/1654
- https://github.com/pypa/manylinux