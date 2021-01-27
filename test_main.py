from main import get_client, list_buckets, create_bucket, call_everything
from moto import mock_s3

@mock_s3
def test_get_client():
    s3 = get_client()
    create_bucket(s3, "bucket")
    

@mock_s3
def test_list_buckets():
    s3 = get_client()
    
    bucketlist = list_buckets(s3)
    print(f"Nirus: {bucketlist}")  

@mock_s3
def test_call_everything():
    
    call_everything()    