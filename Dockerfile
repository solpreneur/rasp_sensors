# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.9-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
#holds app code
RUN mkdir -p /opt/app/sensors
#copy req files
COPY requirements.txt start-server.sh /opt/app/
#copy files from local machine to docker image
COPY . /opt/app/sensors/
WORKDIR /opt/app
#install app requirements
RUN pip3 install -r requirements.txt --cache-dir /opt/app/pip_cache

#access mode confg
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]