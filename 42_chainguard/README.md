# CHAINGUARD

Use chainguard to build images.  

REF: Dockerexamples

TODO:

* Use pipenv to install

NOTES:

* Distroless images
* Use the `-dev` images to include shell `/bin/sh`

## Build

```sh
docker build . -t octo-facts
```

## Run

```sh
docker run --rm octo-facts
```

## Troubleshooting

```sh
docker run -it --rm --entrypoint /bin/sh octo-facts
```

## Resources

* <https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/python/>
* <https://edu.chainguard.dev/chainguard/chainguard-images/how-to-use-chainguard-images/>
