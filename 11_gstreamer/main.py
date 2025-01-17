import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import json
import math

import gi
gi.require_version("Gst", "1.0")
from gi.repository import GLib, Gst

global samples
samples = []
global mainloop

Gst.init([])
mainloop = GLib.MainLoop()

WAVE_LEVEL = "wavelevel"

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


def message_callback(bus, message):
    logger = logging.getLogger()
    if message.src.name == WAVE_LEVEL:
        try:
            p = message.get_structure().get_value("rms")
            # invert the decibel value, get the natural log of the inversion and then invert back again
            level = (math.log(-p[0]) * -1)
            samples.append(level)
            logger.debug(f"Message: {message.src.name} {level}")

        except TypeError:
            pass

    if message.type == Gst.MessageType.EOS:
        logger.info(f"Message Type: {str(message.type)}")
        mainloop.quit()
        write_points()

    elif message.type == Gst.MessageType.ERROR:
        bus.disconnect_by_func(message_callback)
        error, message = message.parse_error()
        logger.error(f"{error}: {message}")
        mainloop.quit()

def write_points():
    logger = logging.getLogger()

    minSample = min(samples)
    normalized = []

    for i in samples:
        sample = minSample / float(i)
        if math.isnan(sample) == False:
            normalized.append(minSample / float(i))

    logger.info(f"Samples: {len(normalized)}")
    f = open("./out/samples.txt", "w")
    for i in normalized:
        f.write(f"{i}\n")

    f = open("./out/samples.json", "w")
    f.write(json.dumps(normalized))


def process(filepath: str, num_samples: int) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG='{test_config}'")

    logger.info(f"{Gst.version()[0]}.{Gst.version()[1]}")
    logger.info(f"Filepath: {filepath} Samples: {num_samples}")
    uri = filepath
    pipeline = Gst.parse_launch(f'uridecodebin uri={uri} ! fakesink')

    # Set pipeline to PAUSED to get media information
    pipeline.set_state(Gst.State.PAUSED)
    pipeline.get_state(Gst.CLOCK_TIME_NONE)

    # Query duration
    duration = pipeline.query_duration(Gst.Format.TIME)[1]

    duration_sec = duration / 1e9
    logger.info(f"GST Duration: {duration} Duration: {duration_sec} seconds")

    # Clean up
    pipeline.set_state(Gst.State.NULL)
    # 10 samples per second
    interval = 100_000_000 

    #interval = int((duration_sec / num_samples) * 1000_000_000)

    gstLaunch = "uridecodebin name=decode uri={0} ! audioconvert ! level name={1} interval={2} post-messages=true ! fakesink qos=false name=nullsink".format(uri, WAVE_LEVEL, interval)

    pipeline = Gst.parse_launch(gstLaunch)
    bus = pipeline.get_bus()
    bus.add_signal_watch()
    bus.connect("message", message_callback)
    pipeline.set_state(Gst.State.PLAYING)
    mainloop.run()
    pipeline.set_state(Gst.State.NULL)

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

    parser = argparse.ArgumentParser(description="CLI Skeleton")
    parser.add_argument("--process", dest="process", action="store_true", help="Enable processing")
    parser.add_argument("--file", dest="filepath", type=str, help="A fullpath to the source audio")
    parser.add_argument("--samples", dest="samples", type=int, help="Number of points to sample", default=1000)
    args = parser.parse_args()

    success = 0
    if args.process:
        success = process(args.filepath, args.samples)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
