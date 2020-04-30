import gpiozero
from time import sleep
import json
import requests

#Set up pins
Forward = gpiozero.OutputDevice(23)
SpeedPWM = gpiozero.PWMOutputDevice(24)

North = gpiozero.LED(2)
East = gpiozero.LED(3)
South = gpiozero.LED(17)
West = gpiozero.LED(27)
try:
   
    while True:
        Forward.on()
        ##set up API Call
        print("Please enter a city name: ")
        city = raw_input()
        print("Please input the corresponding state: ")
        state = raw_input()
        URL="https://api.openweathermap.org/data/2.5/weather"
        #make call with url
        PARAMS = {'q':[city,state],'appid':'745774c81d84372e1972cab0a2bdc2c2'}
        response = requests.get(url = URL, params = PARAMS)
        data = response.json()
        rawSpeed= data["wind"]["speed"]
        print("raw speed = {} ".format(rawSpeed))
        rawDeg = data["wind"]["deg"]
        print("raw deg = {}".format(rawDeg))
        direction = 'N'
        #convert speed from m/s to mph
        convertedSpeed = rawSpeed * 2.237
        #highest ever wind speed = 231 used 240 as a buffer
        speedFlag = convertedSpeed / 240
        
        #set speed for motor
        SpeedPWM.value = speedFlag
        
        if direction == 'N':
            North.on()
            sleep(5)
            North.off()
        if direction == 'E':
            East.on()
            sleep(5)
            East.off()
        if direction == 'S':
            South.on()
            sleep(5)
            South.off()
        if direction == 'W':
            West.on()
            sleep(5)
            West.off()
        if direction == 'NE':
            North.on()
            East.on()
            sleep(5)
            North.off()
            East.off()
        if direction == 'SE':
            South.on()
            East.on()
            sleep(5)
            South.off()
            East.off()
        if direction == 'SW':
            South.on()
            West.on()
            sleep(5)
            South.off()
            West.off()
        if direction == 'NW':
            North.on()
            West.on()
            sleep(5)
            North.off()
            West.off()
        if direction == 'exit':
            exit()

except KeyboardInterrupt:
    print("exiting")
    gpiozero.close()


