# Kinesis Stream to Lambda Processing with S3 Storage
This project sets up an AWS architecture using **CloudFormation** to create a **Kinesis Stream** that triggers a **Lambda function** to process incoming data. The processed data is stored in an existing **S3 bucket**. A Python script is provided to send mock data to the Kinesis stream. The following steps describe the development process.

### Prerequisites
- **AWS CLI**: To deploy CloudFormation stack.
- **Boto3**: For Python script to interact with Kinesis.
- **Existing S3 Bucket**: To store the processed data.


### Step 1: Plan the Architecture

1. **Kinesis Stream**: Receives the incoming data.
2. **Lambda Function**: Processes the Kinesis data and writes it to the existing S3 bucket.
3. **S3 Bucket**: Stores the processed data.

Consider:
- **IAM Roles** for secure access.
- **Scaling** (adjusting shard count in Kinesis).
- **Monitoring and logging** via CloudWatch.

> **Note**: The role and policies are defined in `lambda-s3-template.json`.

### Step 2: Create the CloudFormation Template

Create a CloudFormation template (`kinesis-lambda-s3-template.json`) to define the resources:
- **Kinesis Stream**: Parameterized for flexibility in stream name and shard count.
- **Lambda Function**: Triggered by Kinesis stream and processes data to S3.
- **IAM Role**: Granting permissions for Lambda to access Kinesis and S3.

Define key parameters:
- **StreamName**: Kinesis stream name.
- **ShardCount**: Number of Kinesis shards.
- **BucketName**: The S3 bucket where processed data will be stored.

### Step 3: Deploy the CloudFormation Stack

Use the AWS CLI to deploy the CloudFormation template. This will set up the Kinesis stream, Lambda function, and necessary IAM roles.

```bash
aws cloudformation create-stack --stack-name KinesisLambdaS3Stack --template-body file://kinesis-lambda-s3-template.json --parameters ParameterKey=StreamName,ParameterValue=kinesis-stream-hw-03 ParameterKey=BucketName,ParameterValue=s3-bucket-assignment-01 --capabilities CAPABILITY_IAM
```
> **Note**: `--capabilities CAPABILITY_IAM`: This flag tells AWS that you are aware the CloudFormation stack will create or modify IAM roles or policies.


### Step 4: Write the Python Script to Send Mock Data

Create a Python script (`send_mock_data.py`) to send mock data to the Kinesis stream. The script will:

- Generate random data.
- Base64-encode the data.
- Send the data to the specified Kinesis stream using Boto3.

### Step 5: Trigger Lambda and Verify Data in S3

- **Send mock data** to the Kinesis stream by running the Python script.
  ```
  python send_mock_data.py
   ```
- **Verify that the Lambda function is triggered** when data is pushed to the Kinesis stream.
- **Check the S3 bucket** to confirm that processed data is stored correctly in the format `data/<id>.json`.

### Step 6: Monitoring and Logging
Update the stack
```
aws cloudformation update-stack --stack-name KinesisLambdaS3Stack --template-body file://kinesis-lambda-s3-template.json --parameters ParameterKey=StreamName,ParameterValue=kinesis-stream-hw-03 ParameterKey=BucketName,ParameterValue=s3-bucket-assignment-01 --capabilities CAPABILITY_IAM
```
