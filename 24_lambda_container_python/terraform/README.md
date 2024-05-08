# README

Demonstrate creation of a container-lambda.  

## Create Lambda

```sh
# config aws profile
. ./.env 

# init
terraform init

# plan 
terraform plan -var-file=./terraform.dev.tfvars

# create state
terraform apply -auto-approve -var-file=./terraform.dev.tfvars

# show decrypted state
terraform show -json | jq   
```

## Cleanup

```sh
terraform destroy

# NOTE: To be able to destroy ECR with images you have to have deployed it with force_delete=true
terraform destroy --target module.typescript_service.aws_ecr_repository.this
```

## Resources

* Terraform AWS modules [here](https://github.com/terraform-aws-modules)
* hashicorp/terraform releases [here](https://github.com/hashicorp/terraform/releases)  
* Serverless.tf - Serverless Application & Infrastructure Lifecycle Management using Terraform and friends! [here](https://serverless.tf/)
https://github.com/antonbabenko/serverless.tf
* terraform-aws-modules registry[here](https://registry.terraform.io/modules/terraform-aws-modules/lambda/aws/latest)
* terraform-aws-modules container-image example [here](https://github.com/terraform-aws-modules/terraform-aws-lambda/tree/master/examples/container-image)
* terraform-aws-apigateway-v2 complete-http example [here](https://github.com/terraform-aws-modules/terraform-aws-apigateway-v2/blob/v2.2.1/examples/complete-http/main.tf)

### Issues

* InvalidParameterValueException: We currently do not support adding policies for $LATEST. #36 [here](https://github.com/terraform-aws-modules/terraform-aws-lambda/issues/36)  
