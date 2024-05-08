
variable "TAG" {
  default = "latest"
}
variable "REGISTRY" {
  default = "hello/"
}
#***********************************************
# Build images
#***********************************************

target "lambda-container-python" {
  args       = { "baseimage" : "" }
  context    = "."
  dockerfile = "Dockerfile"
  labels = {
    "org.opencontainers.image.title" = "lambda-container-python:${TAG}"
  }
  tags = ["${REGISTRY}lambda-container-python:${TAG}"]
}

group "default" {
  targets = [
    "lambda-container-python",
  ]
}
