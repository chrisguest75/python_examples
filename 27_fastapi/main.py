import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
from typing import Union
from fastapi import FastAPI


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


@app.get("/")
def read_root():
    logger.info(f"read_root")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    logger.info(f"read_item", extra={"item_id": item_id, "q": q})
    return {"item_id": item_id, "q": q}
