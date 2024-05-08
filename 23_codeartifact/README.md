# CODEARTIFACT

Use AWS CodeArtifact for publishing and sourcing packages.  

TODO:

* Create Domain
* Create Repository

## Create CodeArtifact

```sh
export AWS_PROFILE=my-profile
export AWS_REGION=us-east-1 
export PAGER=
```

```sh
# get name, domainname and domainowner for login
aws codeartifact list-repositories
```

## Publish Package

Goto [codeartifact_test_package/README.md](./codeartifact_test_package/README.md)  

## Use Package

Goto [codeartifact_use_package/README.md](./codeartifact_use_package/README.md)  

## Resources

* Configure and use twine with CodeArtifact [here](https://docs.aws.amazon.com/codeartifact/latest/ug/python-configure-twine.html)  
