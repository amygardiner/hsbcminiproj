import boto3
from s3streaming import s3_open

with s3_open('s3://group14-miniproject/lob-data/Tst2022-01-04LOBs.txt', boto_session=boto3.session.Session(aws_access_key_id="ASIA5IWSWOLR7ZHY3YEH", aws_secret_access_key="QPKxht7aJXb7n8Z/SUZVpGnaIMZIFclJZccX1ry/", aws_session_token="FwoGZXIvYXdzEOr//////////wEaDK3gvI55FzWI+QFQTSK5AatTRC9q6Gi7g/8y19LhADvQuMnckUAePtJpW+9WJkdwZXLXbTBA50J28EPz6euG6GL62dRt04DKvFXFSQ/d2H9s7aoeGG8OYGQ6M2p0cB0sCy3bidphvf5vpGrUmaGmBfizhzCrmls255vXDwCb5VDWpY+EevPZStP+PtpOWWSXO18SzJkbvhaYXWTDH7D2MpeIA8qWq/bm/jjG0cpQIQABPDvU8wH+iU6oHyFD9EKa7HOCayfac3oGKMTiyZAGMi2qR596zBrb29TzZ5Yu9Wu1cPjdnBLNXo4dVM8zjK/G6w7DOJBkfF0JPjSjQ0c=", region_name='us-east-1')) as f:
    for next_line in f:
        print(next_line)
