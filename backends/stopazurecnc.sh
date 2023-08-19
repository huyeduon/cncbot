#!/bin/bash
echo "Stopping Cloud Controller Azure and C8000V"
account=hcloud
rg=infra

az account set -s $account
sleep 1

echo "Stop cAPIC Azure"
az vm deallocate -g $rg -n capic --no-wait &

echo "Stop C8KV-1"
az vm deallocate -g $rg -n ct_routerp_australiaeast_0_0 --no-wait &

echo "Stop C8KV-2"
az vm deallocate -g $rg -n ct_routerp_australiaeast_1_0 --no-wait &

echo "Stop ecomWeb"
az vm deallocate -g vrf1 -n ecomWeb --no-wait &
echo "Done!"