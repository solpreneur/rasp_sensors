# rasp_sensors
Django Web app-Display data from sensors store in AWD dB.

This is a simple django web application that is connected to an AWS database (PostrgeSQL) and reads data collected from sensors connected to a raspberry pi zero w.


#Run on Docker

Simply create a docker container and run (Terminal) it using the following lines of code. 

1 - Create Docker contianer 
```
docker build -t rasp_sensors .

``` 

2 - Run container in Background 

```
docker run -it -dp 8020:8020 rasp_sensors

````


#Note
Django uses the gunicorn and Nginx web server to run on a docker container. You can 
always change this if you want but you need to create a separate docker container/file
