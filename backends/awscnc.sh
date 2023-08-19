#!/bin/bash
now=$(date +"%T")
echo "Start time: $now"

echo "Start cAPIC AWS"
aws ec2 start-instances --instance-ids i-0dceb8dd21afc3ac2 --region us-east-1 --profile htduong02 > /dev/null 2>&1

sleep 1
echo "Start C8KV-1"
aws ec2 start-instances --instance-ids i-0238337982c275d9d --region us-east-1 --profile htduong02 > /dev/null 2>&1

sleep 1 
echo "Start C8KV-2"
aws ec2 start-instances --instance-ids i-0cc5a5a87e3875892 --region us-east-1 --profile htduong02 > /dev/null 2>&1

sleep 1 
echo "Start ecomWeb"
aws ec2 start-instances --instance-ids i-06e31368c58d15f51 --region us-east-1 --profile htduong04 > /dev/null 2>&1

sleep 1 
echo "Start awsEpg1"
aws ec2 start-instances --instance-ids i-0e7a9d85445d3f32d --region us-east-1 --profile htduong04 > /dev/null 2>&1

sleep 1 
echo "Start awsEpg1-a"
aws ec2 start-instances --instance-ids i-063ef13f837caa222 --region us-east-1 --profile htduong04 > /dev/null 2>&1

echo "Done...please wait few minutes."