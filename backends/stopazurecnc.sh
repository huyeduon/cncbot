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

echo "Stop fw1"
az vm deallocate -g infraSvc -n fw1 --no-wait &

echo "Stop azEpg1"
az vm deallocate -g azvrf1 -n azEpg1 --no-wait &

echo "Stop azEpg2"
az vm deallocate -g azvrf2 -n azEpg2 --no-wait &

echo "Stop ecomWeb"
az vm deallocate -g vrf1 -n ecomWeb --no-wait &
echo "Done!"