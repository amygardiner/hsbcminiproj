import boto3
from s3streaming import s3_open

with s3_open('s3://group14-miniproject/lob-data/Tst2022-01-04LOBs.txt', boto_session=boto3.session.Session()) as f:
    for next_line in f:
        print(next_line)
