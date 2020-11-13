#!/usr/bin/env python3

from aws_cdk import core

from stacks.ec2_stack import Ec2Stack

# the account here is just a dummy
env_singapore = core.Environment(account="101234019520", region="us-east-1")

app = core.App()
Ec2Stack(app, "ec2", env=env_singapore)

app.synth()
