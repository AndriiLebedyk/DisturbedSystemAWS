import json
import boto3
import time
from datetime import datetime

def lambda_handler(event, context):
    message = json.loads(event["Records"][0]["body"])
    
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('Dashboard')
    
    ssm_client = boto3.client('ssm')
    
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    item={
        "Name": message["Name"],
        "Description": message["Description"],
        "Author": message["Author"],
        "Date": date
    }
    AddItem(table, item)
    
    items = table.scan()
    result = json.dumps(items["Items"], indent=2, sort_keys=True)
    print(result)
    
    command = f'#!/bin/bash\nyum -y update\nyum -y install httpd\necho "<html><body><h3>Items</h3><h4>{result}</h4></body></html>" > var/www/html/index.html\nsudo service httpd start'
    response = ssm_client.send_command(
            InstanceIds=['i-044f55d7757f3c2c5'],
            DocumentName="AWS-RunShellScript",
            Parameters={'commands': [command]}, )

    command_id = response['Command']['CommandId']
    time.sleep(2)
    
    output = ssm_client.get_command_invocation(CommandId=command_id, InstanceId='i-044f55d7757f3c2c5')
    return output
def AddItem(table,item):
    table.put_item(Item=item)