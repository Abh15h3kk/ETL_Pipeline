"""Connector and methods accessing S3"""
import os
import boto3

class S3BucketConnector():
    """
    Class for interacting with S3 Buckets
    """
    def __init__(self, access_key: str, secret_key: str, endpoint_url: str, bucket: str):
        self.endpoint_url = endpoint_url
        self.session = boto3.Session(aws_access_key_id = os.environ[access_key],
                                     aws_secret_access_key = os.environ[secret_key])
        self._s3 = self.session.resoure(service_name='s3', endpoint_url = endpoint_url)
        self._bucket = self._s3.Bucket(bucket)
    
    def list_files(self):
        pass

    def read_csv_to_df(self):
        pass

    def write_df_to_s3(self):
        pass

    
