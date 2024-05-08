resource "aws_ecr_repository" "this" {
  name                 = var.lambda_name
  image_tag_mutability = "MUTABLE"

  force_delete = true
  
  image_scanning_configuration {
    scan_on_push = true
  }

  encryption_configuration {
    encryption_type = "AES256"
  }
  
  tags = local.tags
}