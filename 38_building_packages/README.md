# BUILDING PACKAGES

Demonstrate building packages from source including ones with native compliation.

NOTES:

- Packages might not be available on pypy so we'll build them.

## Builds

## Troubleshooting

```sh
# print out egg details for the packages.
pip inspect

pipenv graph
```

## Wheels

```sh
# unpack the wheel to see what is inside
pipenv run wheel ./packages/dist/ctranslate2-4.4.0-pp310-pypy310_pp73-linux_x86_64.whl --dest ./ctran2
```

## ManyLinux

```sh
# get image
docker pull quay.io/pypa/manylinux2014_x86_64

# run vanilla manylinux
docker run -it  quay.io/pypa/manylinux2014_x86_64
```

## Resources

- github.com/pypa/manylinux repo [here](https://github.com/pypa/manylinux)
- Build with many linux [here](https://github.com/OpenNMT/CTranslate2/issues/1654)
- Building manylinux Python wheels [here](https://opensource.com/article/19/2/manylinux-python-wheels)
- What is manylinux? [here](https://dev.to/icncsx/what-is-manylinux-4ojd)
- Manually building manylinux python wheels [here](http://www.martin-rdz.de/index.php/2022/02/05/manually-building-manylinux-python-wheels/)
