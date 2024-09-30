# AWS S3 Bucket Creation using CloudFormation

This project sets up a basic S3 bucket using CloudFormation. The project requirements are not fully defined, so the current setup is simple and flexible. IAM permissions and the CloudFormation template will be refined as the project evolves.

## Steps:

### 1. Create IAM User:
- In the AWS Console, create an IAM user `training` with **Programmatic access**.
- Attach the `AdministratorAccess` policy or relevant permissions.
- Save the **Access Key ID** and **Secret Access Key**.
> **Note**: Permissions will later be adjusted to follow the **Least Privilege Principle**.

### 2. Configure AWS CLI Profile:
```
aws configure --profile training
```
Enter your Access Key ID, Secret Access Key, region, and output format (json).

### 3. Create CloudFormation Template
Save this as s3-bucket-template.json:
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
> **Note:** This basic template will be updated later as needed.

### 4. Deploy the Stack
```
aws cloudformation create-stack \
    --stack-name my-simple-s3-stack \
    --template-body file://s3-bucket-template.json \
    --profile training
```

### 5. Check the Stack Status
```
aws cloudformation describe-stacks --stack-name my-simple-s3-stack --profile training
```


