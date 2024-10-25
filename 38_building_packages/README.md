# BUILDING PACKAGES

Demonstrate building packages from source including ones with native compliation.  

NOTES:

* Packages might not be available on pypy so we'll build them.  

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

## Resources

- Build with many linux https://github.com/OpenNMT/CTranslate2/issues/1654
- https://github.com/pypa/manylinux