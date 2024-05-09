
variable "TAG" {
  default = "latest"
}
variable "REGISTRY" {
  default = "hello/"
}

variable "CODEARTIFACT_URL" {
}

#***********************************************
# Build images
#***********************************************

target "lambda-container-python" {
  args       = { "baseimage" : "", "CODEARTIFACT_URL" : "${CODEARTIFACT_URL}" }
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
