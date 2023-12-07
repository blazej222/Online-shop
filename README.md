# An online shop
This is an online shop running on prestashop - for electronic business class.

## Used software

Prestashop 1.7.8

mariadb (latest)

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

## Running shop

Before starting shop database.zip must be extracted inside website directory.

You can put this file inside installer directory and run

```
sh installer.sh
```

to install automatically.

To start a new instance of the shop use:

```
cd website
docker compose up -d
```

To stop running instance use:
```
docker compose down
```

## Team
Błażej Szutenberg

Oskar Wilda

Kacper Skarżyński

Kuba Wojtalewicz

Piotr Wesołowski