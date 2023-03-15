#!/usr/bin/env python3
import boto3
#import pprint

ec2 = boto3.client('ec2')
response = ec2.describe_regions()
active_instances = []
inactive_instances = []


for regio in ec2.describe_regions()['Regions']:
    regio_name=(regio['RegionName'])
    print ("scanning region: ", regio_name)
    new_client = boto3.client('ec2', region_name=regio_name)
    for reservation_i in new_client.describe_instances()['Reservations']:
        if (reservation_i ['Instances'][0]['State']['Code'] == 16):
            text_to_append = "region is "+regio_name+", instance is "+reservation_i['Instances'][0]['InstanceId']
            active_instances.append(text_to_append)
        else:
            text_to_append = "region is "+regio_name+", instance is "+reservation_i['Instances'][0]['InstanceId']
            inactive_instances.append (text_to_append)

 
#print (active_instances)       
print('Active Instances:')
for x in active_instances:
    print (x)
print ('Inactive Instances:')
for x in inactive_instances:
    print (x)
    
    
