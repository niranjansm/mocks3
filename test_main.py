from main import get_client, list_buckets, create_bucket
from main import upload_file, download_file, list_bucket_objects, call_everything
from moto import mock_s3
import os


@mock_s3
def test_list_buckets():
    s3 = get_client()
    bucketlist = ["testbucket1", "testbucket2"]
    create_bucket(s3, bucketlist[0])
    create_bucket(s3, bucketlist[1])
    response = list_buckets(s3)
    assert response == bucketlist


@mock_s3
def test_upload_file():

    s3 = get_client()
    bucket_name = "testbucket"
    create_bucket(s3, bucket_name)
    upload_file(s3, bucket_name)

    objects = list_bucket_objects(s3, bucket_name)

    assert ["hello.txt"] == objects


@mock_s3
def test_download_file():

    s3 = get_client()
    bucket_name = "testbucket"
    create_bucket(s3, bucket_name)
    upload_file(s3, bucket_name)
    download_file(s3, bucket_name)
    assert os.path.exists("downloadedhello.txt")


@mock_s3
def test_call_everything():

    call_everything()
