import boto3


ec2_create = boto3.client('ec2', 'us-east-2', aws_access_key_id='xxxxxxxxxxxxxxx', aws_secret_access_key='xxxxxxxxxxxxxxx')


conn = ec2_create.run_instances(InstanceType="t2.micro",
                         MaxCount=2,
                         MinCount=1,
                         keyName = 'MyKeyPair',
                         ImageId="ami-00399ec92321828f5")
print(conn)

