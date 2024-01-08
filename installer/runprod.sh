#!/bin/bash
sh sqlloader.sh

wait

sshpass -f sshpass ssh hdoop@localhost -p 5243 \
"cd /opt/storage/actina15-20/block-storage/students/projects/students-swarm-services/BE_184663 &&\
docker stack deploy -c docker-compose.yml BE_184663 --with-registry-auth"