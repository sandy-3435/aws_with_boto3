import boto3

#Creates Ec2 instace
ami_id="ami-0ba259e664698cbfc"
instancetype="t2.micro"
key_name="boto"
region="ap-south-1"
#you can use client too for low level interface
ec2=boto3.resource('ec2',region_name=region)
instance=ec2.create_instances(
    ImageId=ami_id,
    InstanceType=instancetype,
    #ensure that you created key pair in aws console before
    KeyName=key_name,
    MinCount=1,
    MaxCount=1
)
print(instance)
print("instace-id-{}".format(instance[0].id))