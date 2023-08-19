#!/bin/bash
source .env
echo "Stopping AWS Controller"
aws ec2 stop-instances --instance-ids $cnc_instance_id --region us-east-1 --profile htduong02 > /dev/null 2>&1

echo "Stopping C8KV-1"
aws ec2 stop-instances --instance-ids $c8k1_instance_id --region us-east-1 --profile htduong02 > /dev/null 2>&1

echo "Stopping C8KV-2"

aws ec2 stop-instances --instance-ids $c8k2_instance_id  --region us-east-1 --profile htduong02 > /dev/null 2>&1

echo "Stop workload in user tenant"
aws ec2 stop-instances --instance-ids $awsweb_instance_id --region us-east-1 --profile htduong04 > /dev/null 2>&1

echo "Done!"