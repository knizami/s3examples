import boto3
import sys
import os.path
from botocore.client import Config

print """
Will upload multiple files, skips a file that doesn't exist
"""

# Other valid options here are 'auto' (default) and 'virtual'

if len(sys.argv) < 3:
    print "usage: s3ex1.py <bucket> <files...>"
    exit(1)

session = boto3.Session(profile_name='dev')
s3 = session.client('s3', 'us-west-2',
                    config=Config(s3={'addressing_style': 'path'}))


response = s3.list_buckets()

for checkbuck in response['Buckets']:
    if checkbuck['Name'] == sys.argv[1]:
        break
else:
    print "Bucket ", sys.argv[1], " doesn't exist, exiting.."
    exit(1)


uploaded = list()
for fup in sys.argv[1:]:
    if not os.path.isfile(fup):
        print "file ", fup, " doesn't exist, skipping..."
        continue
    print "now uploading ", fup, "..."
    s3.upload_file(fup,
                   "s3examples", fup)
    print "upload complete"
    uploaded.append(fup)

print "uploaded ", len(uploaded), " files: ", ",".join(str(x) for x in uploaded)
