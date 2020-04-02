import json
import boto3
import time
import datetime

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')
    message = json.loads(event["Records"][0]["body"])
    html = ""
    command = f'#!/bin/bash\nyum -y update\nyum -y install httpd\necho "<html><body><h3>Your item added successfully! Name: {message["Name"]}, Description: {message["Description"]}, Author: {message["Author"]}, Date: {datetime.datetime.now()}</h3></body></html>" > var/www/html/index.html\nsudo service httpd start'
    response = ssm_client.send_command(
            InstanceIds=['i-07f40dc57d009e0fc'],
            DocumentName="AWS-RunShellScript",
            Parameters={'commands': [command]}, )

    command_id = response['Command']['CommandId']
    time.sleep(2)
    output = ssm_client.get_command_invocation(CommandId=command_id, InstanceId='i-07f40dc57d009e0fc')
    print(output)
    return output
