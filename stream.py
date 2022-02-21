import boto3
from s3streaming import s3_open

with s3_open('s3://group14-miniproject/lob-data/Tst2022-01-04LOBs.txt', boto_session=boto3.session.Session(aws_access_key_id="ASIA5IWSWOLRSFND6MMV", aws_secret_access_key="DdBogzFG08IoPyWgrSdO0aeH4SBkhb/4IS5TDZJ7", aws_session_token="FwoGZXIvYXdzEP3//////////wEaDEuV8HOfXIMXG8tFRSK5AbFjED9vm+bavbVouC5lzTXSrf1nhVKo10HCGmM1X0lazZpvUoMrnKnO1a3PBQurC5gyR3TeIOzMrpf/2fN4TCBKbBL76zvRTCnKQuu89LVOFciwWDBW9VBAymjjN7z6x6vdnYikTQmDVDelTptGUpsisa9HcOHSfLPXiQ5a/ysDzUJDr1ZgoRvfokoMeaH+1ruzLvGCT61bU5EROLHxs/Sv/AZPk5vv6kNfVG8un0HGgJTc0greYSKLKOrqzZAGMi07uO7RXK8iVY+8f9qec/E+6S/vMI+xfXqvTqG3xmZUSeKXe+bdmUW/6xUJvYI=", region_name='us-east-1')) as f:
    for next_line in f:
        print(next_line)
