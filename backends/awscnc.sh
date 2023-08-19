#!/bin/bash
source .env

echo "Start cAPIC AWS"
aws ec2 start-instances --instance-ids $cnc_instance_id --region us-east-1 --profile htduong02 > /dev/null 2>&1

sleep 1
echo "Start C8KV-1"
aws ec2 start-instances --instance-ids $c8k1_instance_id --region us-east-1 --profile htduong02 > /dev/null 2>&1

sleep 1 
echo "Start C8KV-2"
aws ec2 start-instances --instance-ids $c8k2_instance_id --region us-east-1 --profile htduong02 > /dev/null 2>&1

sleep 1 
echo "Start ecomWeb"
aws ec2 start-instances --instance-ids $awsweb_instance_id --region us-east-1 --profile htduong04 > /dev/null 2>&1

echo "Done...please wait few minutes."