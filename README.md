# An online shop
This is an online shop running on prestashop - for electronic business class.

## Used software

Prestashop 1.7.8

mariadb (latest)

memcached (latest)

## Generating SSL certificate

In order to use SSL encryption for prestashop, SSL certificate must be generated using the following commands:
```
openssl genrsa -aes256 -passout pass:password -out server.pass.key 4096

openssl rsa -passin pass:password -in server.pass.key -out server.key

rm server.pass.key

openssl req -new -key server.key -out server.csr \
-subj "/C=PL/ST=Pomerania/L=Gdansk/O=Test/OU=Test/CN=localhost"

openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt
```

Generated files should be placed under website/apache-config/ssl.

Generated certificate can be stored in a public version control solution, however the private key should never be shared.

For simplicity, this repository contains already generated SSL certificate and key, as no real private data will be transferred at this stage of the project.

## Running shop locally

Before starting shop database.zip must be extracted inside website directory.

You can put this file inside installer directory and run

```
sh installer.sh
```

to install automatically.

You also have to create a temporary name resolution for domain `prestashop`.

On linux edit `/etc/hosts` to contain:

```
prestashop  127.0.0.1
```

To start a new instance of the shop use:

```
cd website
docker compose up -d
```

To stop running instance use:
```
docker compose down
```

## Running shop on production cluster

1.Make sure installer folder contains:
- A file named script.sql containing newest database dump.
- A file named sshpass containing ssh password for intermediate and swarm server

2.Make sure `website/storage/vpn` contains files required to create connection to vpn network (extensions ovpn,crt,conf,key).

3.Run `installer/setenv.sh` to forward appropriate ports and initialize vpn connection

<font size=7, color=red>**WARNING!!!** </font>

Command listed in next step will execute queries in `script.sql` on production server (database BE_184663). 

This **will** cause data loss on the target database in case of standard presta db dump (`DROP TABLE IF EXISTS`). 

Before running next step make sure both `script.sql` and `sqlloader.sh` have not been tampered with and contain appropriate commands.

4.Run `installer/runprod.sh` to start production server.



## Team
Błażej Szutenberg

Oskar Wilda

Kacper Skarżyński

Kuba Wojtalewicz

Piotr Wesołowski