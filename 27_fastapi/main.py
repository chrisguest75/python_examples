import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from typing import Union
from fastapi import FastAPI
import random
import time
from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse

def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    """catches unhandled exceptions and logs them"""

    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.critical("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    logging.critical(
        "Unhandled Exception {0}: {1}".format(exc_type, exc_value),
        extra={"exception": "".join(traceback.format_tb(exc_traceback))},
    )


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")

    return 0


logger = logging.getLogger()
test_config = os.environ["TEST_CONFIG"]

with io.open(f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml") as f:
    logging_config = yaml.load(f, Loader=yaml.FullLoader)

logging.config.dictConfig(logging_config)

sys.excepthook = log_uncaught_exceptions

# parser = argparse.ArgumentParser(description="CLI Skeleton")
# parser.add_argument("--help", dest="help", action="store_true")
# args = parser.parse_args()

# if args.help:
#     parser.print_help()

app = FastAPI()

# Define a custom exception handler
@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception):
    logger.info(f"custom_exception_handler", extra={ 'request': request.json(), 'exception': exc})
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error"},
    )


@app.get("/")
def get_root():
    random_number = random.randint(1, 100)
    response = {"root": "toor", "random": random_number}
    logger.info(f"get_root", extra=response)
    return  JSONResponse(
        status_code=200,
        content=response,
    )


@app.get("/items/{item_id}")
def get_items(item_id: int, q: Union[str, None] = None):
    response = {"item_id": item_id, "q": q}
    logger.info(f"get_items", extra=response)
    return  JSONResponse(
        status_code=200,
        content=response,
    )    


@app.get("/echo")
def get_echo():
    random_number = random.randint(1, 100)
    response = {"ping": "pong", "random": random_number}
    logger.info(f"get_echo", extra=response)
    return  JSONResponse(
        status_code=200,
        content=response,
    )


@app.get("/sleep/{sleep_time}")
def get_sleep(sleep_time: int):
    random_number = random.randint(1, 100)
    response = {"sleep": sleep_time, "random": random_number}
    logger.info(f"get_sleep", extra=response)

    time.sleep(sleep_time)

    return  JSONResponse(
        status_code=200,
        content=response,
    )


@app.get("/status/{status}")
def get_status(status: int):
    random_number = random.randint(1, 100)
    response = {"status": status, "random": random_number}
    logger.info(f"get_status", extra=response)

    return  JSONResponse(
        status_code=status,
        content=response,
    )


@app.get("/throw")
def get_throw():
    random_number = random.randint(1, 10)
    response = {"random": random_number}
    logger.info(f"get_throw", extra=response)

    if random_number % 3 == 0: 
        raise FileNotFoundError("FileNotFoundError")
    if random_number % 3 == 1: 
        raise Exception("Exception")

    logger.info(f"get_throw success", extra=response)
    return  JSONResponse(
        status_code=200,
        content=response,
    )