#!/bin/sh
# This scripts creates vpn connection and tunnels required to work with production environment

init_connections(){
    #Init vpn tunnel
    cd ../website/storage/vpn/
    sudo openvpn --config vpnWETI.ovpn &
    openvpn_pid=$!
    sleep 5
    echo "OpenVPN connected (PID:$openvpn_pid)"
    cd ../../../installer/

    #Create tunnel for sql webadmin
    sshpass -f sshpass ssh -S sockets/webadmin -M -N -f -L 0.0.0.0:5242:student-swarm01.maas:9099 rsww@172.20.83.101
    echo "Webadmin tunnel created"

    #Create tunnel for sql database
    sshpass -f sshpass ssh -S sockets/sql -M -N -f -L 0.0.0.0:3306:student-swarm01.maas:3306 rsww@172.20.83.101
    echo "SQL tunnel created"

    #Create tunnel for prestashop website
    sshpass -f sshpass ssh -S sockets/website -M  -N -f -L 0.0.0.0:18466:student-swarm01.maas:18466 rsww@172.20.83.101
    echo "Website tunnel created "

    #Create tunnel for prestashop website port 80
    sshpass -f sshpass ssh -S sockets/websitehttp -M  -N -f -L 0.0.0.0:18863:student-swarm01.maas:18863 rsww@172.20.83.101
    echo "Website http tunnel created "

    #Create tunnel for prestashop website port 80
    sshpass -f sshpass ssh -S sockets/ssh -M  -N -f -L 0.0.0.0:5243:student-swarm01.maas:22 rsww@172.20.83.101
    echo "SSH tunnel created "
}

close_connections(){
    ssh -S sockets/webadmin -O exit rsww@172.20.83.101
    ssh -S sockets/sql -O exit rsww@172.20.83.101
    ssh -S sockets/website -O exit rsww@172.20.83.101
    ssh -S sockets/websitehttp -O exit rsww@172.20.83.101
    ssh -S sockets/ssh -O exit rsww@172.20.83.101
    sleep 3
    sudo kill $openvpn_pid
    wait
    cd sockets
    rm -rf *
}

init_connections

echo "Press CTRL+C to kill connections"

trap close_connections INT

wait

