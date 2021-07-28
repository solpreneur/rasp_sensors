# rasp_sensors
Django Web app-Display data from sensors store in AWD dB.

This is a simple django web application that is connected to an AWS database (PostrgeSQL) and reads data collected from sensors connected to a raspberry pi zero w.


# Run on Docker

Simply create a docker container and run the following lines of command from the terminal.



1 - Create Docker contianer 

Make sure to cd into the cloned repo on your dekstop before creating the container
```
docker build -t rasp_sensors .
``` 

you can  create the contianer directly from the github link by using this command
(this command was not tested)
```
$ docker build https://github.com/solpreneur/rasp_sensors.git#master  
``` 



2 - Run container in Background 

```
docker run -it -dp 8020:8020 rasp_sensors
````

3 - Website running at 
http://localhost:8020/

login details
username: admin
password: solution20


# Note
Django uses the gunicorn and Nginx web server to run on a docker container. You can 
always change this if you want but you need to create a separate docker container/file
