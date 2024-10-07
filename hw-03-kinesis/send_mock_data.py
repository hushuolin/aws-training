import boto3
import json
import random
import time

kinesis = boto3.client('kinesis')

stream_name = 'kinesis-stream-hw-03'

def send_mock_data():
    for i in range(10):
        data = {
            "id": i,
            "message": f"Sample message {i}",
            "timestamp": time.time()
        }
        # No need to manually Base64 encode the data
        response = kinesis.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),  # Send data as JSON string
            PartitionKey=str(random.randint(1, 100))
        )
        print(f"Data sent: {data}")

if __name__ == '__main__':
    send_mock_data()
