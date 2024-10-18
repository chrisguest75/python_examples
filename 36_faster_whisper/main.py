import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import platform
import timeit
from functools import partial
from faster_whisper import WhisperModel
from pynvml import nvmlInit, nvmlSystemGetDriverVersion, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetName
import ctranslate2

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


def details() -> str:
    """ return details aout python version and platform as a dict """
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "platform_details": platform.platform(),
    }


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def test(gpu: bool, compute_type: str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f'Invoked test function - TEST_CONFIG={test_config!r}')
    logger.info(f"details={details()}")
    ctranslate2.set_log_level(logging.INFO)

    # model_size = "large-v3"
    model_size = "medium"

    # Run on GPU with FP16
    logger.info(f'GPU={gpu!r}')

    if gpu:
        nvmlInit()
        print(f"Driver Version: {nvmlSystemGetDriverVersion()}")
        deviceCount = nvmlDeviceGetCount()

        for i in range(deviceCount):
            handle = nvmlDeviceGetHandleByIndex(i)
            print(f"Device {i} : {nvmlDeviceGetName(handle)}")
                
        if not compute_type:
            compute_type = "int8_float16"

        logger.info(f'compute_type={compute_type!r}')
        supported_types = ctranslate2.get_supported_compute_types("cuda")
        model = WhisperModel(model_size, device="cuda", compute_type=compute_type, num_workers=1)
    else:
        if not compute_type:
            compute_type = "float32"

        logger.info(f'compute_type={compute_type!r}')
        supported_types = ctranslate2.get_supported_compute_types("cpu")
        model = WhisperModel(model_size, device="cpu", compute_type=compute_type, num_workers=1)
    
    logger.info(f"supported_compute_types={supported_types}")

    segments, info = model.transcribe("./sources/LNL301_1mins.mp3", beam_size=5, word_timestamps=True)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
        for word in segment.words:
            print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))

    return 0


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="Faster Whisper Testing")
    parser.add_argument("--test", dest="test", action="store_true")
    parser.add_argument("--gpu", dest="gpu", action="store_true")
    parser.add_argument("--compute_type", dest="compute_type", default="")
    args = parser.parse_args()

    success = 0
    if args.test:
        test_partial = partial(test, args.gpu, args.compute_type)
        execution_time = timeit.timeit(test_partial, globals=globals(), number=1)
        logger = logging.getLogger()
        logger.info(f"Execution time: {execution_time:.4f} seconds")
        success = True
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
