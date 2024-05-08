
module "lambda_function_from_container_image" {
    source  = "terraform-aws-modules/lambda/aws"
    version = "4.7.1"

    function_name = var.lambda_name
    description   = "My container lambda test"

    create_package = false
    publish = true

    ##################
    # Container Image
    ##################
    image_uri     = join("", [aws_ecr_repository.this.repository_url, ":", var.lambda_container_tag])
    package_type  = "Image"
    architectures = ["x86_64"]

    allowed_triggers = {
        AllowExecutionFromAPIGateway = {
        service    = "apigateway"
        source_arn = "${module.api_gateway.apigatewayv2_api_execution_arn}/*/*"
        }
    }

    tags          = local.tags
}
