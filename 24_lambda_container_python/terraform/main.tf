terraform {
  required_version = "=1.4.4"

  backend "local" {
    path = "./state/terraform.tfstate"
  }
}

provider "aws" {
  region = var.lambda_region
  default_tags {
    tags = {
      "created_by"  = "terraform"
      "application" = "lambda-container"
      "owner"       = "chrisguest"
    }
  }
}
