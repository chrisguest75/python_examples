import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import platform
from importlib.metadata import distributions
import time
import rtmidi
from rtmidi.midiutil import open_midioutput
from rtmidi.midiconstants import NOTE_OFF, NOTE_ON
from rtmidi.midiutil import open_midiinput

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
    """return details about python version and platform as a dict"""

    platform_details = {
        "python_version": sys.version,
        "platform": sys.platform,
        "platform_details": platform.platform(),
    }

    installed_packages = [(dist.metadata["Name"], dist.version) for dist in distributions()]
    for package in installed_packages:
        platform_details[package[0]] = package[1]

    return platform_details


def str2bool(value: str) -> bool:
    """ converts strings representing truth to bool """ ""
    return value.lower() in ("yes", "true", "t", "1")


def test() -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")
    logger.info(f"details={details()}")

    platform_details = details()
    for key in platform_details.keys():
        logger.info(f"{key}: {platform_details[key]}")


def producer(port_name: str) -> int:
    logger = logging.getLogger()
    midiout = None
    try:
        midiout, port_name = open_midioutput(0)
    except (EOFError, KeyboardInterrupt, rtmidi.NoDevicesError):
        logger.error("Error opening MIDI output port")

    if midiout is None:
        midiout = rtmidi.MidiOut() 
        midiout.open_virtual_port(port_name)
        logger.info(f"Opened virtual MIDI output port '{port_name}'")

    available_ports = midiout.get_ports()
    logger.info(f"Available MIDI ports: {available_ports}")

    with midiout:
        while True:
            note_on = [NOTE_ON, 60, 112]  # channel 1, middle C, velocity 112
            note_off = [NOTE_OFF, 60, 0]
            midiout.send_message(note_on)
            time.sleep(0.5)
            midiout.send_message(note_off)
            time.sleep(0.1)
            time.sleep(1.0)
            logger.info(f"Note sent {note_on}")  # Sleep for a bit before sending the next note

    del midiout

    return 0

def consumer(port_name: str) -> int:
    logger = logging.getLogger()
    midiin = None

    try:
        midiin, port_name = open_midiinput(0)
    except (EOFError, KeyboardInterrupt, rtmidi.NoDevicesError):
        logger.error("Error opening MIDI output port")

    if midiin is None:
        midiin = rtmidi.MidiIn() 
        available_ports = midiin.get_ports()
        logger.info(f"Available MIDI ports: {available_ports}")
        midiin.open_virtual_port(port_name)
        logger.info(f"Opened virtual MIDI output port {port_name}")

    logger.info("Entering main loop. Press Control-C to exit.")
    try:
        timer = time.time()
        while True:
            msg = midiin.get_message()

            if msg:
                message, deltatime = msg
                timer += deltatime
                logger.info("[%s] @%0.6f %r" % (port_name, timer, message))

            time.sleep(0.01)
    except KeyboardInterrupt:
        logger.info('')
    finally:
        logger.info("Exit.")
        midiin.close_port()
        del midiin

    return 0


def main() -> int:
    """
    main function

    returns 0 on success, 1 on failure

    configures logging and processes command line arguments
    """
    with io.open(f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml") as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="CLI Skeleton")
    parser.add_argument("--producer", dest="producer", action="store_true")
    parser.add_argument("--consumer", dest="consumer", action="store_true")
    args = parser.parse_args()

    success = 0
    
    test()

    port_name = "mymidi"
    if args.producer:
        success = producer(port_name)
    elif args.consumer:
        success = consumer(port_name)
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
