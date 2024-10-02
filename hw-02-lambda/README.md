# AWS Lambda Function with S3 Integration
This assignment is to create a Lambda Function using CloudFormation and use this Lambda Function to read and write from the S3 bucket you created from the last assignment.

**Create IAM Role and Permissions**

   - Create a permission policy
   - Create an execution role
   - Create the lambda function

The role and policies are defined in `lambda-s3-template.json`.

**Deploy the CloudFormation Stack**

   ```bash
   aws cloudformation create-stack \
       --stack-name lambda-s3-stack \
       --template-body file://lambda-s3-template.json \
       --capabilities CAPABILITY_IAM
   ```


**Test the Lambda Function**
- Go to the Lambda Console.
- Create a test event and run the function.
- Verify that it writes example-object.txt to S3.


