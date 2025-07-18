import boto3
import os
import pathlib

 # lambda function that acts as an helper in reading files while deploying

s3 = boto3.client("s3")
def handler(event, context):
    bucket_name = os.environ["BUCKET_NAME"]
    folder = os.environ["LOCAL_FOLDER"]

    print(f"Uploading files from {folder} to bucket {bucket_name}") # easier to track

    base_path = pathlib.Path(__file__).parent /  "sample_files" # grab the files

    print("BASE PATH:", base_path)
    print("FILES FOUND:")

    for file_path in base_path.glob("*"): # for every file in sample_files
        print("-", file_path)
        if file_path.is_file():
            s3.upload_file(str(file_path), bucket_name, file_path.name)
            print(f"Uploaded {file_path.name}")

    return {"status": "done"}
