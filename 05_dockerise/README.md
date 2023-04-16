# DISTROLESS

Demonstrates dockerising python tools.  

TODO:

* Work out how to build a smaller image
* Get the tests running in the image
* Make the build multistage to slim down installation

NOTE:

* It seems that `distroless` images are experimental.  

## Install

```sh
export PIPENV_VENV_IN_PROJECT=1
pipenv install --dev
```

## Run

```sh
pipenv run test

pipenv run start 

pipenv run build:docker
pipenv run start:docker
```

## Resources

* Distroless repo [here](https://github.com/GoogleContainerTools/distroless)  
* Documentation for gcr.io/distroless/python3 [here](https://github.com/GoogleContainerTools/distroless/blob/main/experimental/python3/README.md)  

https://github.com/GoogleContainerTools/distroless/issues/1296
https://www.chainguard.dev/unchained/minimal-container-images-towards-a-more-secure-future

https://iximiuz.com/en/posts/containers-making-images-better/

https://www.infoq.com/news/2022/10/distroless-slsa-level-two/

https://slsa.dev/spec/v0.1/levels
