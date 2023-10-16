# GEOIP TOOLING

To create follow repository [README.md](../README.md)  

## 🏠 Start

```sh
pipenv install --dev
```

## WhoisXMLAPI

Goto [whoisxmlapi](https://ip-geolocation.whoisxmlapi.com/) to create an API key and set it in `.env` file.  

```sh
# use whoisxml
pipenv run start --timeout 4 --ip 193.248.57.140 | jq . 
```

## Resources

* MaxMind [here](https://www.maxmind.com/en/home)  
* WhoIsXMLApi [here](https://ip-geolocation.whoisxmlapi.com/api/documentation)  
