###################
# HTTP API Gateway
###################

resource "aws_cloudwatch_log_group" "logs" {
  name = var.lambda_name
}

module "api_gateway" {
  source  = "terraform-aws-modules/apigateway-v2/aws"
  version = "2.2.1"

  name          = join("", [var.lambda_name, "-http"])
  description   = "My awesome HTTP API Gateway"
  protocol_type = "HTTP"
  create_api_domain_name = false

  cors_configuration = {
    allow_headers = ["content-type", "x-amz-date", "authorization", "x-api-key", "x-amz-security-token", "x-amz-user-agent"]
    allow_methods = ["*"]
    allow_origins = ["*"]
  }

  default_stage_access_log_destination_arn = aws_cloudwatch_log_group.logs.arn
  default_stage_access_log_format          = "$context.identity.sourceIp - - [$context.requestTime] \"$context.httpMethod $context.routeKey $context.protocol\" $context.status $context.responseLength $context.requestId $context.integrationErrorMessage"

  default_route_settings = {
    detailed_metrics_enabled = true
    throttling_burst_limit   = 100
    throttling_rate_limit    = 100
  }

  integrations = {

    "ANY /" = {
      lambda_arn             = module.lambda_function_from_container_image.lambda_function_arn
      payload_format_version = "2.0"
      timeout_milliseconds   = 12000
    }

    /*
    "GET /some-route" = {
      lambda_arn               = module.lambda_function.lambda_function_arn
      payload_format_version   = "2.0"
      authorization_type       = "JWT"
      authorizer_id            = aws_apigatewayv2_authorizer.some_authorizer.id
      throttling_rate_limit    = 80
      throttling_burst_limit   = 40
      detailed_metrics_enabled = true
    }

    "POST /start-step-function" = {
      integration_type    = "AWS_PROXY"
      integration_subtype = "StepFunctions-StartExecution"
      credentials_arn     = module.step_function.role_arn

      # Note: jsonencode is used to pass argument as a string
      request_parameters = jsonencode({
        StateMachineArn = module.step_function.state_machine_arn
      })

      payload_format_version = "1.0"
      timeout_milliseconds   = 12000
    }
    */
    
    "$default" = {
      lambda_arn = module.lambda_function_from_container_image.lambda_function_arn
      /*tls_config = jsonencode({
        server_name_to_verify = local.domain_name
      })*/

      response_parameters = jsonencode([
        {
          status_code = 500
          mappings = {
            "append:header.header1" = "$context.requestId"
            "overwrite:statuscode"  = "403"
          }
        },
        {
          status_code = 404
          mappings = {
            "append:header.error" = "$stageVariables.environmentId"
          }
        }
      ])
    }

  }

  body = templatefile("api.yaml", {
    example_function_arn = module.lambda_function_from_container_image.lambda_function_arn
  })

  tags = local.tags
}