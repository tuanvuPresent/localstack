import logging
import boto3
import watchtower


def sample_cloudwatch():
    client = boto3.client(
        'logs',
        endpoint_url='http://localhost:4566',
        region_name='us-east-1',
        aws_access_key_id='test',
        aws_secret_access_key='test'
    )

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    cloudwatch_handler = watchtower.CloudWatchLogHandler(
        boto3_client=client,
        log_group='my-log-group',
        stream_name='my-log-stream'
    )
    logger.addHandler(cloudwatch_handler)
    logger.info("This is an info log!")
    logger.error("This is an error log!")


def sample_storage():
    s3 = boto3.client(
        's3',
        endpoint_url="http://localhost:4566",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1"
    )

    bucket_name = "my-test-bucket"
    file_name = "color_test_800x600_118kb.jpg"
    with open(file_name, 'rb') as f:
        s3.put_object(Bucket=bucket_name, Key='color_test_800x600_118kb.jpg', Body=f)

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        print("Files in bucket:")
        for obj in response.get('Contents', []):
            print(f" - {obj}")
    except Exception as e:
        print(f"Error listing files: {e}")
