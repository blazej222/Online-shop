FROM prestashop/prestashop:1.7.8-apache
RUN rm -rf /var/www/html/* && ls -la /var/www/html
COPY src/ /var/www/html/
COPY apache-config/ /etc/apache2/sites-available/
RUN chown -R www-data /var/www/html/
RUN chown -R www-data /etc/apache2/sites-available/
RUN apt-get update && apt-get install -y libz-dev libmemcached-dev && \
    apt-get install -y memcached libmemcached-tools && \
    pecl install memcached && \
    docker-php-ext-enable memcached
CMD /bin/sh /etc/apache2/sites-available/starter.sh