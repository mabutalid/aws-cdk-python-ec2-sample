from aws_cdk import aws_ec2 as ec2, core

# ==================Creating a simple ec2 instance==================

# BACKGROUND INFORMATION:
# there are 3 required parameters in creating a ec2 instance which are = (instance_type, machine_image, and vpc)
# so before creating the instance you must first create the following: ami(for machine image) and vpc

# Documentations from AWS for cdk python:
# creating ec2 instance ( documentation = https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/Instance.html )
# creating the ami ( documentation = https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/MachineImage.html )
# creating the vpc ( documentation = https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/Vpc.html )

# Reminders:
# dont forget to call this stack in the app.py or check the app.py of this project to see how this was called
# the vpc configured below will get the vpc of where this stack will be deployed so make sure to set the environment(account and region) in the app.py file there is already format there


class Ec2Stack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes below here

        # creating the ami
        amazon_linux = ec2.MachineImage.latest_amazon_linux(
            cpu_type=ec2.AmazonLinuxCpuType.X86_64,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
        )

        # creating the vpc
        vpc = ec2.Vpc.from_lookup(self, "vpc", is_default=True)

        # creating the security group and this is optional
        skull_sg = ec2.SecurityGroup(
            self,
            "myec2sg",
            vpc=vpc,
            security_group_name="skull-sg",
            description="sg for ec2 cdk example",
            allow_all_outbound=True,
        )

        skull_sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "SSH Access")

        # creating the ec2 instance
        instance = ec2.Instance(
            self,
            "Instance",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amazon_linux,
            vpc=vpc,
            security_group=skull_sg,
            instance_name="skull_instance",
        )
