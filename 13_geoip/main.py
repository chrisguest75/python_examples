import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from timeout import timeout_get
import json
import geoip2.webservice
import geoip2.database


def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical(
        "Unhandled Exception {0}: {1}".format(exc_type, exc_value),
        extra={"exception": "".join(traceback.format_tb(exc_traceback))},
    )


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def timeout(url: str, timeout_seconds: int = 5):
    logger = logging.getLogger()
    logger.debug(f"Timeout: {timeout_seconds}")
    response = timeout_get(url, timeout_seconds)
    # logger.info(response)
    return response


def main():
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="GeoIP")
    parser.add_argument(
        "--timeout",
        type=int,
        help="Timeout in seconds",
    )
    parser.add_argument(
        "--ip",
        type=str,
        help="IP Address to check",
    )
    parser.add_argument("--whoisxmlapi", dest="whoisxmlapi", action="store_true", help="whoisxmlapi webservice")
    parser.add_argument("--maxmindws", dest="maxmindws", action="store_true", help="maxmind webservice")
    parser.add_argument("--maxminddb", dest="maxminddb", action="store_true", help="maxmind database")

    args = parser.parse_args()
    if not args.ip or args.ip == "":
        parser.print_help()
        exit(1)

    if args.whoisxmlapi:
        ip_address = args.ip
        apikey = os.getenv("GEOIP_API_KEY")
        url = f"https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey={apikey}&ipAddress={ip_address}"
        logging.debug(url)
        response = timeout(url, args.timeout)

        print(json.dumps(response, indent=1))

    if args.maxmindws:
        license_key = os.getenv("MAXMIND_LICENSE")
        account_id = os.getenv("MAXMIND_ACCOUNTID")
        #logging.info(license_key)
        #logging.info(account_id)

        with geoip2.webservice.Client(int(account_id), license_key) as client:
            response = client.city(args.ip)
            print(str(response))
            
    if args.maxminddb:
        with geoip2.database.Reader('./GeoLite2-City_20231017/GeoLite2-City.mmdb') as reader:
            response = reader.city(args.ip)
            print(str(response))

if __name__ == "__main__":
    main()
    exit(0)
