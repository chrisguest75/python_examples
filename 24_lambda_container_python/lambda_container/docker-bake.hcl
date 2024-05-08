
variable "TAG" {
  default = "latest"
}
variable "REGISTRY" {
  default = "hello/"
}
#***********************************************
# Build images
#***********************************************

target "lambda-container" {
  args = {"baseimage":""}
  context = "."
  dockerfile = "Dockerfile"
  labels = {
    "org.opencontainers.image.title"= "lambda-container:${TAG}"
  }
  tags = ["${REGISTRY}lambda-container:${TAG}"]
}

group "default" {
  targets = [
    "lambda-container", 
    ]
}
