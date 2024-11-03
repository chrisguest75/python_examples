import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import platform
import importlib.metadata
from importlib.metadata import distributions
import av

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


def audio_speedup(file: str, output: str) -> None:
    av.logging.set_level(av.logging.VERBOSE)

    input_file = av.open(file)
    output_file = av.open(output, mode="w")

    input_stream = input_file.streams.audio[0]
    output_stream = output_file.add_stream("pcm_s16le", rate=input_stream.rate)

    graph = av.filter.Graph()
    graph.link_nodes(
        graph.add_abuffer(template=input_stream),
        graph.add("atempo", "2.0"),
        graph.add("abuffersink"),
    ).configure()

    for frame in input_file.decode(input_stream):
        graph.push(frame)
        while True:
            try:
                for packet in output_stream.encode(graph.pull()):
                    output_file.mux(packet)
            except (av.BlockingIOError, av.EOFError):
                break

    # Flush the stream
    for packet in output_stream.encode(None):
        output_file.mux(packet)

    input_file.close()
    output_file.close()


def write_frames(file: str, output:str) -> None:
    av.logging.set_level(av.logging.VERBOSE)
    container = av.open(file)

    for index, frame in enumerate(container.decode(video=0)):
        frame.to_image().save(f"{output}/frame-{index:04d}.jpg")

def export_hls_audio(file: str, output:str) -> None:
    logger = logging.getLogger()
    input_container = av.open(file)

    # Create an audio resampler to convert the audio format
    resampler = av.AudioResampler(format='s16', layout='mono', rate=22050)

    # Duration limit in seconds (2 minutes)
    duration_limit = 1 * 60
    cumulative_duration = 0.0  # Initialize cumulative duration

    # Open the output raw PCM file
    with open(output, 'wb') as pcm_file:
        # Iterate through the audio frames
        for frame in input_container.decode(audio=0):
            # Add the frame duration to the cumulative duration (in seconds)
            cumulative_duration += frame.time_base * frame.samples

            # Stop processing if we reach or exceed 2 minutes of audio
            if cumulative_duration >= duration_limit:
                break
            else:
                logger.info(f"cumulative_duration: {cumulative_duration}, frame.time_base: {frame.time_base}, frame.samples: {frame.samples}")

            # Resample the frame to the desired format
            resampled_frames = resampler.resample(frame)

            # Write each resampled frame to the PCM file
            for resampled_frame in resampled_frames:
                pcm_file.write(resampled_frame.planes[0])

    input_container.close()
    logger.info("Raw PCM file has been written with mono, s16le format at 22 kHz for 2 minutes of audio.")


def test(file: str, operation: str, output: str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f'Invoked test function - TEST_CONFIG={test_config!r}')
    logger.info(f"details={details()}")

    platform_details = details()
    for key in platform_details.keys():
        logger.info(f"{key}: {platform_details[key]}")
    
    if operation == "audio_speedup":
        audio_speedup(file, output)
    elif operation == "write_frames":
        write_frames(file, output)
    elif operation == "export_hls_audio":
        export_hls_audio(file, output)
    else:
        logger.error(f"Invalid operation: {operation}")
    
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
    parser.add_argument("--file", dest="file", type=str)
    parser.add_argument("--operation", dest="operation", type=str)
    parser.add_argument("--output", dest="output", type=str)

    args = parser.parse_args()

    success = test(args.file, args.operation, args.output)

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
