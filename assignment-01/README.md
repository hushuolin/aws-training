# AWS S3 Bucket Creation using CloudFormation

## Steps:

### 1. Create IAM User:
- In the AWS Console, create an IAM user named `training` with **Programmatic access**.
- Attach the `AdministratorAccess` policy or relevant permissions.
- Save the **Access Key ID** and **Secret Access Key**.

### 2. Configure AWS CLI Profile:
Run the following command to configure the `training` profile:
```
aws configure --profile training
```

### 3. Create CloudFormation Template
Create a simple JSON template (s3-bucket-template.json) to define an S3 bucket:
```
{
    "Resources": {
        "S3Bucket": {
            "Type": "AWS::S3::Bucket",
            "DeletionPolicy": "Retain",
            "Properties": {
                "BucketName": "s3-bucket-assignment-01"
            }
        }
    }
}
```

### 4. Deploy the Stack
Use the following command to deploy the CloudFormation stack:
```
aws cloudformation create-stack \
    --stack-name my-simple-s3-stack \
    --template-body file://s3-bucket-template.json \
    --profile training
```

### 5. Check the Stack Status
To check the stack status, run:
```
aws cloudformation describe-stacks --stack-name my-simple-s3-stack --profile training
```


