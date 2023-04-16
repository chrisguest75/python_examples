# REQUESTS

Demonstrate examples of using `requests` package  

## Reason

The requests library is a popular Python library for making HTTP requests. It abstracts the complexities of making requests behind a simple and user-friendly API, allowing you to send HTTP requests using various methods like GET, POST, PUT, DELETE, and others. The library offers many features and functionalities, including:  

* Simplified HTTP methods: Easily send HTTP requests using methods like requests.get(), requests.post(), requests.put(), requests.patch(), and requests.delete().  

* URL handling: Automatically handle URL encoding and decoding, and join URL components seamlessly.  

* Request customization: Customize your requests with headers, query parameters, and other options like timeout, proxies, and authentication.  

* Form data and file uploads: Send form data or upload files using multipart file uploads.  

* JSON support: Easily send and receive JSON data with built-in JSON encoding and decoding.  

* Handling redirects: Automatically follow redirects (with a configurable maximum number of redirects) and handle relative URLs.  

* Cookies: Automatically store and send cookies during a session using requests.Session().  

* Authentication: Support for various authentication mechanisms like Basic, Digest, and OAuth.  

* Timeouts: Set timeouts for requests to prevent them from waiting indefinitely.  

* Error handling: Raise specific exceptions for various error types, making it easier to handle errors in your code.  

* Connection pooling: Reuse existing connections to improve performance, especially for multiple requests to the same server.  

* Proxy support: Send requests via a proxy server, with support for HTTP and SOCKS proxies.  

* SSL/TLS: Verify SSL/TLS certificates and configure SSL settings.  

* Customizable: Extend the library with custom adapters and middleware to modify its behavior.  

## 🏠 Start

```sh
pipenv run start:docker  

# quick test
curl 0.0.0.0:9001
```

## Run

```sh
pipenv run test

pipenv run start --simple --url http://0.0.0.0:9001

pipenv run start --timeout 5 --url http://0.0.0.0:9001/delay/200 | jq .

pipenv run start --timeout 5 --url http://0.0.0.0:9001/headers | jq .  

pipenv run start --post '{"user":"bob","pass":"123"}' --url http://0.0.0.0:9001/echo | jq .
```

## 🧼 Cleanup

```sh
# bring it down and delete the volume
pipenv run start:docker  
```

## 👀 Resources

* stefanprodan/podinfo including API [here](https://github.com/stefanprodan/podinfo)  
* How to Use pytest-mock to Simulate Responses [here](https://medium.com/analytics-vidhya/how-to-use-pytest-mock-to-simulate-responses-1ea41e964161)  
* pytest-dev/pytest-mock [here](
https://github.com/pytest-dev/pytest-mock/)  
