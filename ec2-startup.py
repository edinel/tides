#!/usr/bin/env python3
import boto3
#import pprint

ec2 = boto3.client('ec2')
response = ec2.describe_regions()
active_instances = []
inactive_instances = []


 
#print (active_instances)       
print('Active Instances:')
for x in active_instances:
    print (x)
print ('Inactive Instances:')
for x in inactive_instances:
    print (x)



    #active_instances.extend([i['Instances'][0]['InstanceId'] for i in new_client.describe_instances() ['Reservations'] if i['Instances'][0]['State']['Code'] == 16]) #parse through a mile of dict to find the instance ID 
    
    #print ([i['Instances'][0]['InstanceId'] for i in new_client.describe_instances() ['Reservations'] if i['Instances'][0]['State']['Code'] == 16]) #parse through a mile of dict to find the instance ID
    #inactive_instances.extend([i['Instances'][0]['InstanceId'] for i in new_client.describe_instances() ['Reservations'] if i['Instances'][0]['State']['Code'] != 16]) #parse through a mile of dict to find the instance ID
    
    
       
#
#for y in inactive_instances:
#    print ("inactive", y)


#ec2_west_2 = boto3.client('ec2', region_name="us-west-2") #Get a client for each region
#ec2_east_2 = boto3.client('ec2', region_name="us-east-2") #Get a client for each region

#active_instances_west_2 = [i['Instances'][0]['InstanceId'] for i in ec2_west_2.describe_instances() ['Reservations'] if i['Instances'][0]['State']['Code'] == 16] #parse through a mile of dict to find the instance ID
#active_instances_east_2 = [i['Instances'][0]['InstanceId'] for i in ec2_east_2.describe_instances() ['Reservations'] if i['Instances'][0]['State']['Code'] == 16] #parse a mile of dict to find the instance ID

#inactive_instances_west_2 = [i['Instances'][0]['InstanceId'] for i in ec2_west_2.describe_instances() ['Reservations'] if i['Instances'][0]['State']['Code'] != 16]
#inactive_instances_east_2 = [i['Instances'][0]['InstanceId'] for i in ec2_east_2.describe_instances() ['Reservations'] if i['Instances'][0]['State']['Code'] != 16]

#active_instances = active_instances_west_2
#active_instances.extend(active_instances_east_2) #if you append() you end up adding the array object into the array, which isn't what you want.
#inactive_instances = inactive_instances_east_2
#inactive_instances.extend(inactive_instances_west_2)


#instance_ids = [i['Instances'][0]['InstanceId'] for i in response_dict["Reservations"]]
#for x in instance_ids:
#    print (x)
#

#response_str = str(response_dict)
#response_json = json.loads (response_str)
#json_response = json.dumps(response, indent=2)
#print(json_response)



#pp=pprint.PrettyPrinter(indent=1)
#pp.pprint(response_dict)
#print ("\n\n\n")

#pp.pprint(response_dict['Reservations'][0]['Instances'][0]['InstanceId'])
#print(response_dict['Reservations'][0]['Instances'][0]['InstanceId'])


#for i in response_dict ['Reservations']:
#    if i['Instances'][0]['State']['Code'] == 16:
#        print ("running:", i['Instances'][0]['InstanceId'])
#    else:
#        print ("not running:",i['Instances'][0]['InstanceId'])
#print ("done double looping")