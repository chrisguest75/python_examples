# BUILD FASTER-WHISPER PACKAGE

Build the faster-whisper package from source.

## Build

```sh
# dependencies
docker build --progress=plain --build-arg PYTHON_VERSION=3.11.9 -t 38_build_fasterwhisper .

# export the dist
mkdir -p ./out
docker run -it --rm -v ./out:/out 38_build_fasterwhisper
```

## Examine

```sh
dive docker.io/library/38_build_fasterwhisper
```

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

- SYSTRAN/faster-whisper repo [here](https://github.com/SYSTRAN/faster-whisper)
- github.com/pypa/manylinux repo [here](https://github.com/pypa/manylinux)
