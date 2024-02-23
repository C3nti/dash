FROM ta01eampnacr01.azurecr.io/mpn:0.1.5

EXPOSE 80 443 8050


COPY ./ports.conf /etc/apache2
COPY ./app.py /var/www/html/Dash/
COPY ./wsgi.py /var/www/html/Dash/
COPY ./dash.conf /etc/apache2/sites-available
COPY ./gapminder_unfiltered.csv /var/www/html/Dash/

RUN openssl req -x509 -nodes -subj "/CN=ta01eampnaci01.ajgrhrewa9gtbqc0.westeurope.azurecontainer.io" -days 3650 -newkey rsa:2048 -keyout /etc/ssl/private/dash.key -out /etc/ssl/certs/dash.pem


RUN pip3 install -r requirements.txt
RUN a2dissite 000-default.conf
RUN a2ensite dash
RUN a2enmod headers
RUN a2enmod ssl


CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]

