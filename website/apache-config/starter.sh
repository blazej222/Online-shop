#!/bin/sh
a2enmod ssl
# echo "Restarting apache2"
# service apache2 restart 
echo "Modding user"
usermod -u 1000 www-data  
echo "Starting apache foreground"
apache2-foreground
# wait $!