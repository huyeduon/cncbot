#!/bin/bash

echo "Stopping AWS Controller"
aws ec2 stop-instances --instance-ids i-0dceb8dd21afc3ac2 --region us-east-1 --profile htduong02 > /dev/null 2>&1

echo "Stopping C8KV-1"
aws ec2 stop-instances --instance-ids i-0238337982c275d9d --region us-east-1 --profile htduong02 > /dev/null 2>&1

echo "Stopping C8KV-2"

aws ec2 stop-instances --instance-ids i-0cc5a5a87e3875892 --region us-east-1 --profile htduong02 > /dev/null 2>&1

echo "Stop workload in user tenant"
aws ec2 stop-instances --instance-ids i-06e31368c58d15f51 --region us-east-1 --profile htduong04 > /dev/null 2>&1
aws ec2 stop-instances --instance-ids i-0e7a9d85445d3f32d --region us-east-1 --profile htduong04 > /dev/null 2>&1
aws ec2 stop-instances --instance-ids i-063ef13f837caa222 --region us-east-1 --profile htduong04 > /dev/null 2>&1

echo "Done!"