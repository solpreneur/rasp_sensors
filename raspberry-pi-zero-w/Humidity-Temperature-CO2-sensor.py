import RPi.GPIO as GPIO
from time import sleep
import board
import busio
import adafruit_ccs811
import smbus
import psycopg2
from datetime import datetime
from psycopg2 import Error

    
def databaseConn(state="open"):
    connection = 0
    if state == "open":
        
        try:
            connection = psycopg2.connect(user="solution",
                                          password="solution20",
                                          host="raspberry3.c19jcpai2ylq.us-east-2.rds.amazonaws.com",
                                          port="5432",
                                          database="postgres")
            
            return  {"connection":connection}
        
        except (Exception ,Error) as error:
             print("Error connecting",error)            
    else:
        if(connection):
            cursor.close()
            connection.close()
            print("connection is closed")
        else: pass
        

      
#get temp and humidity data
def getHumTemp():
    bus = smbus.SMBus(1)
    bus.write_byte(0x40, 0xF5)

    sleep(1)

    # si7021 address, 0x40 Read data 2 bytes , Humidity
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)

    #Convert the data
    humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6

    sleep(1)
    bus.write_byte(0x40, 0xF3)
    sleep(1)

    # si7021 address, 0x40 Read data 2 bytes , Temperature
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)

    #Convert the data and output it
    celsTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
    fahrTemp = celsTemp * 1.8 + 32
    
    return {'humidity':humidity,'temperature':celsTemp}

def getCO2():
    i2c = board.I2C() # uses board.scl and board.sda
    ccs811 = adafruit_ccs811.CCS811(i2c)
    
    #Wait for the sensor to be ready
    while not ccs811.data_ready:
        pass
    
    co2Value = ccs811.eco2
  #  while True:
      #  print("CO2: %1.0f PPM" % ccs811.eco2)
       # sleep(10)
    return {'co2':co2Value}

#phyiscal quant detailts
def getTypeDetails(ptype,connection) :
    
    select_query = """ SELECT id FROM reading_types WHERE reading_type=%s """
    cursor = connection.cursor()
    cursor.execute(select_query,(ptype,))

    return cursor.fetchone()

def insertData(typeId,value,connection):
    cursor = connection.cursor()
    query = "INSERT INTO reading(date_time,value,read_type_id) VALUES(%s,%s,%s)"
    #queryFake =""" INSERT INTO reading_types (reading_type) values('solute') """
    data = (datetime.now(),value,typeId)
    
    cursor.execute(query,data)
    connection.commit()
    
    count = cursor.rowcount
    
    if count == 1 :
        return count
    else :
        print(f"data {typeId} not saved")
        return 0

def saveData(phys_quant,connection):
    
    affected = 0 #data rows affected
     
    if "temperature" in phys_quant:
        tempTypeId = getTypeDetails("Temperature",connection)[0]
        results =  insertData(tempTypeId,phys_quant['temperature'],connection)
        affected = affected + results if results > 0 else 0
        
    if "humidity" in phys_quant:
        humTypeId = getTypeDetails("Humidity",connection)[0]
        affected = affected + insertData(humTypeId,phys_quant['humidity'],connection)
        
    if "co2" in phys_quant:
        co2TypeId = getTypeDetails("Co2",connection)[0]
        affected = affected + insertData(co2TypeId,phys_quant['co2'],connection)
        
    return affected
        

    
def main():
    connection =  databaseConn("open")['connection']
   # getCO2()
    
    while True :
        
        humTemp = getHumTemp()
        co2     =getCO2() #functions return dicts
        phys_quants = {**humTemp, **co2} #stores all sensor data
        
        results = saveData(phys_quants,connection)
        if results > 0:
            print (f"data has been saved:{results} ")
            print (f"sRelative Humidity is : {humTemp['humidity']}")
            print (f"sTemperature in Celcius is : {humTemp['temperature']}")
            print (f"sCo2 in PPM is :  {co2['co2']}")
            print("\n")
        else:
            print("data not saved")
            
        sleep(295)
  
    
    databaseConn("close")
    
    

if __name__ =="__main__":
    main()
        

