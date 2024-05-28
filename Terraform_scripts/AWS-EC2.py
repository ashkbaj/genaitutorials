from python_terraform import *
import os


# Define the Terraform configuration
config = {
    'provider': {
        'aws': {
            'access_key': 'none',
            'secret_key': 'none',
            'region': 'ap-south-1'
        }
    },
    'resource': {
        'aws_instance': {
            'example_instance': {
                'ami': 'ami-0c94855ba95c71c99',
                'instance_type': 't2.micro',
                'tags': {
                    'Name': 'example-instance'
                }
            }
        }
    }
}


# Initiate Terraform
tf = Terraform(working_dir="terraform/")
tf.init()
tf.apply(vars=config)


