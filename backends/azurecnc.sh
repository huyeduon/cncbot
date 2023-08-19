#!/bin/bash 
echo "Starting Cloud Azure Cloud Controller and C8000V"
account=hcloud
rg=infra

az account set -s $account

echo "Start cAPIC Azure"
az vm start -g $rg -n capic --no-wait &

echo "Start C8KV-1"
az vm start -g $rg -n ct_routerp_australiaeast_0_0 --no-wait &

echo "Start C8KV-2"
az vm start -g $rg -n ct_routerp_australiaeast_1_0 --no-wait &

echo "Done...please wait few minutes."