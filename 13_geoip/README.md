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
pipenv run start --whoisxmlapi --timeout 4 --ip 193.248.57.140 | jq .
```

## MaxMind

Download the geolite2 db.  

```sh
# use
pipenv run start --maxminddb --ip 193.248.57.140 | jq .
pipenv run start --maxmindws --ip 193.248.57.140 | jq .
```

## Resources

* MaxMind [here](https://www.maxmind.com/en/home)  
* WhoIsXMLApi [here](https://ip-geolocation.whoisxmlapi.com/api/documentation)  
* maxmind/GeoIP2-python [repo](https://github.com/maxmind/GeoIP2-python)  
