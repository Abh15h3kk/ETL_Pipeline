"""
File to store constants
"""
from enum import Enum

class S3FileTypes(Enum):
    """
    supported file types for S3BucketConnector
    """
    CSV = 'csv'
    PARQUET = 'parquet'