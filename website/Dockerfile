FROM prestashop/prestashop:1.7.8-apache
COPY src/* /var/www/html
COPY apache-config/* /etc/apache2/sites-available
CMD /bin/sh /etc/apache2/sites-available/starter.sh