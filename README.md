# DisturbedSystemAWS
Individual task of Disturbed Systems course
### Cloudformation templete add next recources:
- EC2 instances
- VPC Networks
- DynamoDB table
- SQS queue
Thats what CloudFormer generate from my resources
### Also you should add manually:
- Lambda functions(you can get code from files in lambda_functions folder)
- API Gateway with POST method, which trigger your SQS (How to do this: https://medium.com/@pranaysankpal/aws-api-gateway-proxy-for-sqs-simple-queue-service-5b08fe18ce50)
- SSM service and install agent to EVERY EC2 instance(How to do this: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html)
- Configure IAM roles for lambdas to give them permissions work with SQS, DynamoDB, SSM, EC2 services
- Configure IAM roles for GatewayAPI to give those permissions send message to SQS
For cathing errors use CloudWatch logs.

### For testing system outside you can use "Postman" or web applications like this https://www.apirequest.io/ 

### Helpfull links:
- https://docs.aws.amazon.com/lambda/
- https://docs.aws.amazon.com/iam/
- https://docs.aws.amazon.com/apigateway
- https://docs.aws.amazon.com/sqs/
- https://docs.aws.amazon.com/systems-manager/
- https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/introduction.html

# I hope that will help to configure Disturbed system on AWS platform
