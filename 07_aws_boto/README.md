# AWS BOTO EXAMPLE

Demonstrate a simple aws client for testing.  

TODO:

* transparent and tls proxy https://earthly.dev/blog/mitmproxy/
 
## Reason

Using boto3 for AWS access with python is a useful set of tools to have.  

## Start

```sh
# install
pyenv install

pipenv run lint
pipenv run test

pipenv shell


# file with random data
dd if=/dev/urandom of=random.bin bs=1024 count=1024
# 

BUCKET_NAME=mybucket
pipenv run start --upload --file ./random.bin --bucket ${BUCKET_NAME} --prefix random.bin            
pipenv run start --upload --file ./README.md --bucket ${BUCKET_NAME} --prefix README.md 

pipenv run start --delete --bucket ${BUCKET_NAME} --prefix README.md 
```

## Wireshark Packet Capture (tls decode)

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

