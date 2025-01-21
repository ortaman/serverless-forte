import boto3

from infra import db_infra


class Boto3:

    bucket_name = None
    client = None

    def __init__(self):

        boto_settings = db_infra.BotoSettings

        try:
            self.client = boto3.client(
                's3',
                aws_access_key_id=boto_settings.ACC,
                aws_secret_access_key=boto_settings.SEC
            )
            self.bucket_name = boto_settings.S3_NAME

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
