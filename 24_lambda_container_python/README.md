# README

Demonstrate how to build a Lambda Container.  

NOTES:

* Deploy the terraform
* Bake the image with push

* terraform [here](./terraform/README.md)  
* lambda_container [here](./lambda_container/README.md)  

## Tests

```sh
cd ./terraform
curl -vvv $(terraform output --json gateway_api_endpoint | jq -r .)/\?url\=https://www.google.com
```

## Resources

* New for AWS Lambda – Container Image Support [here](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/)  

