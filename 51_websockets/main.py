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
import asyncio
import websockets
import av
from av.audio.resampler import AudioResampler
import wave

SAMPLE_RATE = 22050
CHANNELS = 1
SAMPLE_WIDTH = 2  # 16-bit PCM

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


def pcm_generator(file_path, pcm_format='s16'):
    #av.logging.set_level(av.logging.VERBOSE)
    logger = logging.getLogger()    

    container = av.open(file_path)
    audio_stream = next(s for s in container.streams if s.type == 'audio')

    logger.info(f"Loading audio {file_path} converting to sample rate {SAMPLE_RATE}, channels {CHANNELS}, sample width {SAMPLE_WIDTH}")
    resampler = AudioResampler(
            format='s16',
            layout='mono',
            rate=SAMPLE_RATE
    )

    for packet in container.demux(audio_stream):
        for frame in packet.decode():
            # Resample audio frame
            resampled_frame = resampler.resample(frame)
            # Extract PCM bytes directly from resampled frame
            pcm_bytes = resampled_frame[0].to_ndarray()[0]
            # Write PCM bytes to WAV file
            #logger.info(f"Received: {frame} Resampled: {resampled_frame} PCM: {len(pcm_bytes)} bytes")

            yield pcm_bytes

    container.close()


async def server(bind: str, port: int, out_file: str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")
    logger.info(f"details={details()}")

    platform_details = details()
    for key in platform_details.keys():
        logger.info(f"{key}: {platform_details[key]}")

    out_path = os.path.join("./recording", "recorded_audio.wav")
    if not os.path.exists(os.path.dirname(out_path)):
        os.mkdir(os.path.dirname(out_path))
        logger.info(f"Created directory for recording: {os.path.dirname(out_path)}")

    with wave.open(out_path, 'wb') as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(SAMPLE_WIDTH)
        wav_file.setframerate(SAMPLE_RATE)
        logger.info(f"Recording audio to {out_path}")

        async def save_audio(websocket):
            async for message in websocket:
                logging.info(f"Server received: {len(message)} bytes")
                wav_file.writeframes(message)  

        async with websockets.serve(save_audio, bind, port):
            logging.info(f"Server started at ws://{bind}:{port}")
            await asyncio.Future()  # run forever


    return 0

async def client(uri: str, audio_file: str) -> int:
    """test function"""
    logger = logging.getLogger()
    test_config = os.environ["TEST_CONFIG"]
    logger.info(f"Invoked test function - TEST_CONFIG={test_config!r}")
    logger.info(f"details={details()}")

    platform_details = details()
    for key in platform_details.keys():
        logger.info(f"{key}: {platform_details[key]}")


    async with websockets.connect(uri) as websocket:
        for chunk in pcm_generator(audio_file):
            # chunk is a NumPy array of shape (samples, channels)
            #logger.info(chunk.shape)
            await websocket.send(chunk.tobytes())
        
        #response = await websocket.recv()
        #logger.info(f"Client received: {response}")

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
    parser.add_argument("--client", dest="client",  action="store_true")
    parser.add_argument("--uri", dest="uri", type=str, default="ws://localhost:8765", help="WebSocket URI for client")

    parser.add_argument("--server", dest="server", action="store_true")
    parser.add_argument("--bind", dest="bind", type=str, default="localhost", help="Bind address for server")
    parser.add_argument("--port", dest="port", type=int, default=8765, help="Port for server")

    parser.add_argument("--file", dest="file", type=str)

    args = parser.parse_args()

    if args.client and args.server:
        parser.error("Cannot specify both --client and --server")
        return 1
    
    success = 0
    if args.client:
        success = asyncio.run(client(args.uri, args.file))
    elif args.server:
        success = asyncio.run(server(args.bind, args.port, args.file))
    else:
        parser.print_help()

    return success


if __name__ == "__main__":
    # print(f"Enter {__name__}")
    exit(main())
