#!/bin/bash

#default mongodb daemon stop
systemctl stop mongod

#stop
systemctl stop mongod

#remove data directory
if [ -d data ]; then
    rm -rf ./data
fi

#config Server
mkdir -pv /shard/data/configdb
mkdir -pv /shard/data/logs
touch /shard/data/logs/configsvr.log

mongod --config /shard/mongodConfig.conf &
sleep 3s

# Router Server
touch /shard/data/logs/mongorouter.log

mongos --config /shard/mongodRouter.conf &
sleep 3s

# Shard1
mkdir -pv /shard/data/shard1db
touch /shard/data/logs/shard1.log

mongod --config /shard/mongodShard1.conf &
sleep 2s

# Shard2
mkdir -pv /shard/data/shard2db
touch /shard/data/logs/shard2.log

mongod --config /shard/mongodShard2.conf &
sleep 2s


#process status
ps -ef | grep mongo
sleep 2s

#netstatus
netstat -ntlp
