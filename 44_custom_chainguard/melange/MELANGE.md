# MELANGE

Build apk packages using declarative pipelines.  

## Contents

- [MELANGE](#melange)
  - [Contents](#contents)
  - [Clone package definitions](#clone-package-definitions)
  - [Build custom image](#build-custom-image)
  - [Hello Wolfi Workshop Kit](#hello-wolfi-workshop-kit)
  - [Resources](#resources)

## Clone package definitions

```sh
git clone git@github.com:wolfi-dev/os.git wolfios

docker pull ghcr.io/wolfi-dev/sdk:latest
```

NOTES: When grabbing the configs you need to add the following block otherwise the builds will fail.  

```yaml
    repositories:
      - https://packages.wolfi.dev/bootstrap/stage3
      - https://packages.wolfi.dev/os
      - '@local /work/out'
    keyring:
      - https://packages.wolfi.dev/bootstrap/stage3/wolfi-signing.rsa.pub
      - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub  
```

## Build custom image

This builds a custom distroless image with ffmpeg.  

```sh
# pull required images
docker pull cgr.dev/chainguard/melange
docker pull cgr.dev/chainguard/apko

# generate a key
cd ./44_custom_chainguard/melange
mkdir -p ./out
docker run --rm -v ./out:/work cgr.dev/chainguard/melange keygen

# build packages (curl)
docker run --privileged --rm -v $(pwd):/work -- \
  cgr.dev/chainguard/melange build /work/curl.yaml --out-dir /work/out \
  --arch x86_64 --signing-key /work/out/melange.rsa --keyring-append /work/out/melange.rsa.pub

# build packages (ffmpeg)
docker run --privileged --rm -v $(pwd):/work -- \
  cgr.dev/chainguard/melange build /work/ffmpeg.yaml --out-dir /work/out \
  --arch x86_64 --signing-key /work/out/melange.rsa --keyring-append /work/out/melange.rsa.pub

# build image (ffmpeg)
docker run --rm -v $(pwd):/work cgr.dev/chainguard/apko build /work/image-ffmpeg.yaml chainguard-ffmpeg:latest /work/out/chainguard-ffmpeg.tar -k /work/out/melange.rsa.pub 

# load image
docker load < ./out/chainguard-ffmpeg.tar

# run built image (ffmpeg)
docker run --rm chainguard-ffmpeg:latest-amd64 -version

docker run --rm --entrypoint /usr/bin/ffmpeg chainguard-ffmpeg:latest-amd64 -version

# analyse
dive chainguard-ffmpeg:latest-amd64

# scan image
grype -o json chainguard-ffmpeg:latest-amd64
```

## Custom Python 3.11

```sh
# generate a key
cd ./44_custom_chainguard/melange
mkdir -p ./out
docker run --rm -v ./out:/work cgr.dev/chainguard/melange keygen

# build packages (python)
docker run --privileged --rm -v $(pwd):/work -- \
  cgr.dev/chainguard/melange build --log-level debug /work/python-3.11.yaml --out-dir /work/out \
  --arch x86_64 --signing-key /work/out/melange.rsa --keyring-append /work/out/melange.rsa.pub

# build image (python)
docker run --rm -v $(pwd):/work cgr.dev/chainguard/apko build /work/image-python-3.11.yaml chainguard-python-3-11:latest /work/out/chainguard-python-3-11.tar -k /work/out/melange.rsa.pub 

# load image
docker load < ./out/chainguard-python-3-11.tar

# run built image (ffmpeg)
docker run --rm chainguard-python-3-11:latest-amd64 --version

docker run --rm --entrypoint /usr/bin/python chainguard-python-3-11:latest-amd64 --version

# analyse
dive chainguard-python-3-11:latest-amd64

# scan image
grype -o json chainguard-python-3-11:latest-amd64
```

## Resources

- Community workshop kit about Wolfi for beginners [here](https://edu.chainguard.dev/open-source/wolfi/hello-wolfi/)  
- chainguard-dev/melange repo [here](https://github.com/chainguard-dev/melange)
- Creating Wolfi Images with Dockerfiles [here](https://edu.chainguard.dev/open-source/wolfi/wolfi-with-dockerfiles/)  
- wolfi-dev/os repo [here](https://github.com/wolfi-dev/os)
