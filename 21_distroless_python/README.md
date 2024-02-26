# DISTROLESS

## 🏠 Build example

Build with the default distroless python version.

```sh
# python with requirements file
cd ./21_distroless_python/with_requirements

docker build --progress=plain -f Dockerfile.python3 -t python3_distroless .
docker run -it --rm python3_distroless
dive python3_distroless


docker run -it --entrypoint /busybox/sh --rm python3_distroless
```

## 👀 Resources

- Distroless repo [here](https://github.com/GoogleContainerTools/distroless)
- Python 3 with requirements.txt [here](https://github.com/GoogleContainerTools/distroless/tree/main/examples/python3-requirements)
- What's Inside Of a Distroless Container Image: Taking a Deeper Look [help](https://iximiuz.com/en/posts/containers-distroless-images/)
- Publish :nonroot versions of images [here](https://github.com/GoogleContainerTools/distroless/issues/306)
- Using unprivileged users [here](https://github.com/GoogleContainerTools/distroless/issues/277)
- Creating an up-to-date Python Distroless Container Image [here](https://alex-moss.medium.com/creating-an-up-to-date-python-distroless-container-image-e3da728d7a80)
* https://stackoverflow.com/questions/77175636/building-multi-stage-docker-image-with-a-distroless-base-image-results-in-no-su
