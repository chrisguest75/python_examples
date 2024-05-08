################################################################################
# Lambda
################################################################################

output "gateway_api_endpoint" {
  description = "Url of the lambda"
  value       = module.api_gateway.apigatewayv2_api_api_endpoint
}

################################################################################
# Repository URL
################################################################################

output "repository_url" {
  description = "Repository of service image"
  value       = aws_ecr_repository.this.repository_url
}

