import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
# MaxCount = defines the no of instances to launch
# ImageID = dont forget to add image id

instances = ec2.create_instances(
     ImageId='ami-0994975f92b8520bc',
     MinCount=1,
     MaxCount=3,
     InstanceType='t2.micro',
     KeyName='testing123'
 )
