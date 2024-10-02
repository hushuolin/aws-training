# AWS Lambda Function with S3 Integration
This assignment is to create a Lambda Function using CloudFormation and use this Lambda Function to read and write from the S3 bucket you created from the last assignment.

**Create IAM Role and Permissions**

   - Create a permission policy
   - Create an execution role
   - Create the lambda function

> **Note**: The role and policies are defined in `lambda-s3-template.json`.

**Deploy the CloudFormation Stack**

   ```
   aws cloudformation create-stack \
    --stack-name lambda-s3-stack \
    --template-body file://lambda-s3-template.json \
    --parameters ParameterKey=BucketName,ParameterValue=s3-bucket-assignment-01 \
    --capabilities CAPABILITY_IAM
   ```

> **Note**: Replace the ParameterValue with your destination bucket name


**Test the Lambda Function**
- Go to the Lambda Console.
- Create a test event and run the function.
- Verify that it writes example-object.txt to S3.


