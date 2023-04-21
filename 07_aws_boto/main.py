import argparse
import io
import logging
import logging.config
import sys
import traceback
import yaml
import os
import boto3
from boto3.session import Session


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


def upload(local_path: str, bucket_name: str, s3_key: str):
    logger = logging.getLogger()

    # Replace the following with your own values
    profile_name = os.environ['AWS_PROFILE']
    file_path = local_path

    # Create a session with the specified profile
    session = Session(profile_name=profile_name)

    # Create an S3 client using the session
    s3 = session.client('s3')

    # Upload the file to S3
    with open(file_path, 'rb') as file:
        s3.upload_fileobj(file, bucket_name, s3_key)

    print(f"File '{file_path}' successfully uploaded to S3 bucket '{bucket_name}' as '{s3_key}'.")


def signedupload(bucket_name: str, s3_key: str):
    logger = logging.getLogger()

    # Replace the following with your own values
    profile_name = os.environ['AWS_PROFILE']

    # Create a session with the specified profile
    session = Session(profile_name=profile_name)

    # Create an S3 client using the session
    s3 = session.client('s3')

    presigned_url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': bucket_name,
            'Key': s3_key,
            'ContentType': "application/octet-stream",
        },
        ExpiresIn=3600,
    )

    print(f"{presigned_url}")


def delete(bucket_name: str, s3_key: str):
    logger = logging.getLogger()

    # Replace the following with your own values
    profile_name = os.environ['AWS_PROFILE']

    # Create a session with the specified profile
    session = Session(profile_name=profile_name)

    # Create an S3 resource using the session
    s3 = session.resource('s3')

    # Get a reference to the bucket
    bucket = s3.Bucket(bucket_name)

    print(f"Deleting S3 objects from 's3://{bucket_name}/{s3_key}' recursively...")
    # Iterate through objects with the specified prefix and delete them
    for obj in bucket.objects.filter(Prefix=s3_key):
        obj.delete()
        print(f"Deleted file: {obj.key}")



def main():
    with io.open(
        f"{os.path.dirname(os.path.realpath(__file__))}/logging_config.yaml"
    ) as f:
        logging_config = yaml.load(f, Loader=yaml.FullLoader)

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger()

    sys.excepthook = log_uncaught_exceptions

    parser = argparse.ArgumentParser(description="AWS BOTO")
    parser.add_argument("--upload", dest="upload", action="store_true")
    parser.add_argument("--delete", dest="delete", action="store_true")
    parser.add_argument("--signed", dest="signed", action="store_true")
    parser.add_argument("--file", dest="file", type=str)
    parser.add_argument("--bucket", dest="bucket", type=str)
    parser.add_argument("--prefix", dest="prefix", type=str)
    args = parser.parse_args()

    if args.upload:
        logger.info(f"Upload {args.file} -> s3://{args.bucket}/{args.prefix}")
        if args.signed:
            logger.info(f"Signed upload")
            signedupload(args.bucket, args.prefix)
        else:
            upload(args.file, args.bucket, args.prefix)
    elif args.delete:
        logger.info(f"Delete s3://{args.bucket}/{args.prefix}")
        delete(args.bucket, args.prefix)
    else:
        parser.print_help()

if __name__ == "__main__":
    print(f"Enter {__name__}")
    main()
    exit(0)
