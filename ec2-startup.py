#!/usr/bin/env python3
import boto3
import pprint
pp=pprint.PrettyPrinter(indent=1)

ec2_us_west_2 = boto3.client('ec2', region_name='us-west-2')

template_name='tide_web_service'
instance_spec = {
    'KeyName': 'tides',
    'MaxCount': 1,
    'MinCount': 1,
    'LaunchTemplate': {
        'LaunchTemplateName': template_name,
        'Version': '$Latest'
    }
}


print ("Instance Spec\n")
pp.pprint(instance_spec)

tide_instance = ec2_us_west_2.run_instances (**instance_spec);

print ("\n\n")
print ("Returned Instance\n")
pp.pprint (tide_instance)

#print (active_instances)       
#print('Active Instances:')
#for x in active_instances:
#    print (x)
#print ('Inactive Instances:')
#for x in inactive_instances:
#    print (x)