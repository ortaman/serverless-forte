import os
import boto3

from config import db_config


class Boto3:

    bucket_name = None
    client = None

    def __init__(self):

        boto_settings = db_config.BotoSettings

        try:

            if os.environ.get("AWS_EXECUTION_ENV"):
                self.client = self.client = boto3.client('s3')
                self.bucket_name = boto_settings.S3_DEV_NAME

            else:
                self.client = boto3.client(
                    's3',
                    aws_access_key_id=boto_settings.B3_LOCAL_ACC,
                    aws_secret_access_key=boto_settings.B3_LOCAL_SEC
                )
                self.bucket_name = boto_settings.S3_LOCAL_NAME

        except Exception as exception:
            print(f"Error: {exception}")


    def upload_file(self, xlsx_file, content_type):
        self.client.put_object(
            Body=xlsx_file,
            Bucket=self.bucket_name,
            Key=xlsx_file.filename,
            ContentType=content_type
        )

        presigned_url = self.client.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.bucket_name, 'Key': xlsx_file.filename},
            ExpiresIn=3600
        )
    
        return presigned_url
