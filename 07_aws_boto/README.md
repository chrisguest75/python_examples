# AWS BOTO EXAMPLE

Demonstrate a simple aws client for testing.  

TODO:

* transparent and tls proxy https://earthly.dev/blog/mitmproxy/3* use wireshark to drop connections and throttle.
* test mitm proxy with boto
* add some tests to mock boto.
* https://www.twoistoomany.com/exploring-boto3-events-with-mitmproxy/ 
* https://github.com/micktwomey/exploring-boto3-events-with-mitmproxy 

## Reason

Using boto3 for AWS access with python is a useful set of tools to have.  
Weirdly signed PUT urls cannot be generated with the AWS cli.  So there's a very quick example here.  

## Start

```sh
# install
pyenv install

export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev

pipenv run lint
pipenv run test

pipenv shell
```

## Usage

```sh
# file with random data
dd if=/dev/urandom of=random.bin bs=1024 count=1024

# set AWS_PROFILE or default will be used.
export AWS_PROFILE=myprofile

# upload files
BUCKET_NAME=mybucket
pipenv run start --upload --file ./random.bin --bucket ${BUCKET_NAME} --prefix random.bin            
pipenv run start --upload --file ./README.md --bucket ${BUCKET_NAME} --prefix README.md 

# download files
export BUCKET_NAME=mybucket
pipenv run start --download --bucket ${BUCKET_NAME} --prefix myfile.m4a --file ./myfile.m4a      

# delete files
pipenv run start --delete --bucket ${BUCKET_NAME} --prefix README.md

# generate signed put urls 
SIGNEDURL1=$(pipenv run start --upload --signed --bucket ${BUCKET_NAME} --prefix random4.bin | jq -r -s '.[].url' | grep https --color=no)
echo $SIGNEDURL1
# upload file
curl -v -X PUT -T "./random.bin" -H "Content-Type: application/octet-stream" $SIGNEDURL1
# list files
AWS_PROFILE=myprofile aws s3 ls ${BUCKET_NAME}
```

## Wireshark Packet Capture (tls decode)

REF: [31_packet_capture/README.md](https://github.com/chrisguest75/sysadmin_examples/blob/master/31_packet_capture/README.md)  

```sh
mkdir -p ./captures

export SSLKEYLOGFILE=$(pwd)/captures/.ssl-key.log
echo $SSLKEYLOGFILE

# open termminal and run 
sudo tcpdump -vvv -i any port 443 -w ./captures/aws.pcap

# run a test
pipenv run start --upload --file ./random.bin --bucket ${BUCKET_NAME} --prefix random.bin

# configure Wireshark to decrypt using the SSLKEYLOGFILE:  
# copy full path of .ssl-key.log add to the preferences->protocols->tls->pre-master-secret-log-filename
# in packet view filter by tls
wireshark -r ./captures/aws.pcap
```

## MITM interception (not-working)

Try and recreate failing network scenarios.  

REF: [23_mitmproxy/README.md](https://github.com/chrisguest75/sysadmin_examples/blob/master/23_mitmproxy/README.md)  

## 🏠 Start

```sh
# start 
docker compose -f ./docker-compose.mitmproxy.yaml up -d
open http://0.0.0.0:8081    
curl -vvv --proxy 0.0.0.0:8080 -i http://www.google.com
curl -vvv --proxy 0.0.0.0:8080 -i https://www.google.com


export HTTP_PROXY=0.0.0.0:8080
export HTTPS_PROXY=0.0.0.0:8080

# failing with tls issue.
pipenv run start --upload --file ./random.bin --bucket ${BUCKET_NAME} --prefix random.bin            
```

## 🧼 Clean up

```sh
docker compose -f ./docker-compose.mitmproxy.yaml down
```

## Created

```sh
# install
pipenv install --dev flake8 flake8-bugbear flake8-2020 black
pipenv install --dev pytest 

pipenv install pyyaml python-json-logger
```

## 👀 Resources

* Boto3 documentation [here](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  
* https://www.twoistoomany.com/exploring-boto3-events-with-mitmproxy/ 
* https://github.com/micktwomey/exploring-boto3-events-with-mitmproxy 