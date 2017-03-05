import boto3
from botocore.client import Config

# Other valid options here are 'auto' (default) and 'virtual'
session = boto3.Session(profile_name='dev')
s3 = session.client('s3', 'us-west-2',
                    config=Config(s3={'addressing_style': 'path'}))
s3.upload_file("/Users/khurramnizami/tmp.txt",
               "s3examples", "/test/tmp_file")
print "upload complete"
