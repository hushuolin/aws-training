import json
import base64
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode Base64-encoded Kinesis data
        try:
            payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            
            # Log the payload for debugging
            print(f"Decoded payload: {payload}")
            
            # Convert the decoded payload to JSON
            data = json.loads(payload)
            
            # Log the data for debugging
            print(f"Data: {data}")
            
            # Store the processed data in S3
            bucket_name = 's3-bucket-assignment-01'  # Replace with your actual bucket name
            key = f"data/{data['id']}.json"
            
            # Upload the JSON object to S3
            s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))
            print(f"Uploaded to S3: {bucket_name}/{key}")
            
        except Exception as e:
            print(f"Error processing record: {str(e)}")

    return {'statusCode': 200, 'body': 'Success'}
