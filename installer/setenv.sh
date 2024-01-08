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
    sshpass -f sshpass ssh -S sockets/webadmin -M -N -f -L 0.0.0.0:5242:student-swarm01.maas:9099 rsww@172.20.83.101 &
    webadmin_pid=$!
    echo "Webadmin tunnel created (PID:$webadmin_pid)"

    #Create tunnel for sql database
    sshpass -f sshpass ssh -S sockets/sql -M -N -f -L 0.0.0.0:3306:student-swarm01.maas:3306 rsww@172.20.83.101 &
    sql_pid=$!
    echo "SQL tunnel created (PID:$sql_pid)"

    #Create tunnel for prestashop websiteB
    sshpass -f sshpass ssh -S sockets/website -M  -N -f -L 0.0.0.0:5244:student-swarm01.maas:3306 rsww@172.20.83.101 &
    website_pid=$!
    echo "Website tunnel created (PID:$website_pid)"
}

close_connections(){
    ssh -S sockets/webadmin -O exit rsww@172.20.83.101
    ssh -S sockets/sql -O exit rsww@172.20.83.101
    ssh -S sockets/website -O exit rsww@172.20.83.101
    # kill $sql_pid
    # kill $website_pid
    # kill $webadmin_pid
    sleep 3
    sudo kill $openvpn_pid
}

init_connections

echo "Press CTRL+C to kill connections"

# while true: do
#     read -rsn1 key
#     if [[ $key == $'\e']]: then
#         echo "Killing environment"
#         break
#     fi
# done

trap close_connections INT

wait

