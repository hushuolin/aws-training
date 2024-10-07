# Kinesis Stream to Lambda Processing with S3 Storage

## Overview
This project sets up an AWS architecture to process data using a **Kinesis stream** that triggers a Lambda function, which processes the data and stores it in an **S3 bucket**. The steps below describe how to create the required resources using **AWS CloudFormation** and how to send mock data to Kinesis for processing.

### Prerequisites
- **AWS CLI**: To deploy CloudFormation stack.
- **Boto3**: For Python script to interact with Kinesis.

# Steps
### Step 1: Plan the Architecture
Before starting the implementation, plan the following components:

1. **Kinesis Stream**: Receives the incoming data.
2. **Lambda Function**: Triggered by Kinesis, it processes the incoming data and writes the results to an S3 bucket.
3. **S3 Bucket**: Stores the processed data in a structured format (e.g., JSON files).

#### Key Considerations:
- **IAM Roles**: Ensure the Lambda function has appropriate permissions to read from Kinesis and write to S3..
- **Lambda Timeout and Memory**: Adjust the memory and timeout based on the expected data size and processing needs.

### Step 2: Define the Infrastructure Using CloudFormation

Create a CloudFormation template (`kinesis-lambda-s3-template.json`) to define the resources:

- **IAM Role**: Granting permissions for Lambda to access Kinesis and S3.
- **Kinesis Stream**: Parameterized for flexibility in stream name and shard count.
- **Lambda Function**: Triggered by Kinesis stream and processes data to S3.
- **Event Source Mapping**: Link the Kinesis stream as a trigger to the Lambda function using event source mapping.

#### Define key parameters:
- **StreamName**: Kinesis stream name.
- **ShardCount**: Number of Kinesis shards.
- **BucketName**: The S3 bucket where processed data will be stored.
- **LambdaMemorySize**: Memory size for the Lambda function (in MB).
- **LambdaTimeout**: Timeout for the Lambda function (in seconds).

### Step 3: Write the Lambda Function Code
The Lambda function will process the data coming from the Kinesis stream and store it in the S3 bucket. This function needs to:

1. **Decode the Kinesis data** (since it's Base64 encoded).
2. **Convert the data** to JSON.
3. **Write the processed data** to the S3 bucket, using a unique key for each object.
  
#### Key Points:
- **Base64 Decoding**: Kinesis data is Base64-encoded by default, so the function must decode it before processing.
- **Error Handling**: Ensure that the function handles errors gracefully, logging any issues for troubleshooting.

### Step 4: Deploy the CloudFormation Stack

Use the AWS CLI to deploy the CloudFormation template. This will set up the Kinesis stream, Lambda function, and necessary IAM roles.

```bash
aws cloudformation create-stack --stack-name KinesisLambdaS3Stack --template-body file://kinesis-lambda-s3-template.json --parameters ParameterKey=StreamName,ParameterValue=kinesis-stream-hw-03 ParameterKey=BucketName,ParameterValue=s3-bucket-assignment-01 --capabilities CAPABILITY_IAM
```
> **Note**: `--capabilities CAPABILITY_IAM`: This flag tells AWS that you are aware the CloudFormation stack will create or modify IAM roles or policies.


### Step 5: Write the Python Script to Send Mock Data

Create a Python script (`send_mock_data.py`) to send mock data to the Kinesis stream. The script will:

- **Generate sample data** (e.g., JSON objects).
- **Send the data** to the specified Kinesis stream using Boto3.

### Step 6: Trigger Lambda and Verify Data in S3

- **Send mock data** to the Kinesis stream by running the Python script.
  ```
  python send_mock_data.py
   ```
- **Verify that the Lambda function is triggered** when data is pushed to the Kinesis stream.
- **Check the S3 bucket** to confirm that processed data is stored correctly in the format `data/<id>.json`.

### Step 7: Monitor and Debug
1. **Monitor CloudWatch Logs**: CloudWatch will capture logs from the Lambda function. Use these logs to ensure that the function is processing the data correctly.
2. **Troubleshooting**:
- If data is not appearing in S3, check the Lambda logs for any errors.
- After debug the code, update the stack
  ```
  aws cloudformation update-stack --stack-name KinesisLambdaS3Stack --template-body file://kinesis-lambda-s3-template.json --parameters ParameterKey=StreamName,ParameterValue=kinesis-stream-hw-03 ParameterKey=BucketName,ParameterValue=s3-bucket-assignment-01 --capabilities CAPABILITY_IAM
  ```
