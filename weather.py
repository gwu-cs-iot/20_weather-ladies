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
    goAgain = 'Y'
   
    while goAgain == 'Y':
        Forward.on()
        ##set up API Call
        print("Please enter a city name: ")
        city = raw_input()
        print("Please input the corresponding state: ")
        state = raw_input()
        
        URL="https://api.openweathermap.org/data/2.5/weather"
        PARAMS = {'q':[city,state],'appid':'745774c81d84372e1972cab0a2bdc2c2'}
        response = requests.get(url = URL, params = PARAMS)
        data = response.json()
        rawSpeed= data["wind"]["speed"]
        print("raw speed = {} ".format(rawSpeed))
        direction = data["wind"]["deg"]
        print("raw deg = {}".format(direction))
        
        #convert speed from m/s to mph
        convertedSpeed = rawSpeed * 2.237
        #highest ever wind speed = 231 used 240 as a buffer
        speedFlag = convertedSpeed / 240
        
        #set speed for motor
        SpeedPWM.value = speedFlag
        
        #each direction gets 45 degrees on the compass
        
        if direction > 337.5 or direction <= 22.5:
            North.on()
            print("The wind is blowing North at a speed of {} mph.\n".format(convertedSpeed))
            sleep(5)
            North.off()
        if direction > 67.5 and direction <=112.5:
            East.on()
            print("The wind is blowing East at a speed of {} mph.\n".format(convertedSpeed))
            sleep(5)
            East.off()
        if direction > 167.5 and direction <= 202.5:
            South.on()
            print("The wind is blowing South at a speed of {} mph.\n".format(convertedSpeed))
            sleep(5)
            South.off()
        if direction > 247.5 and direction <= 292.5:
            West.on()
            print("The wind is blowing West at a speed of {} mph.\n".format(convertedSpeed))
            sleep(5)
            West.off()
        if direction > 22.5 and direction <= 67.5:
            North.on()
            East.on()
            print("The wind is blowing Northeast at a speed of {} mph.\n".format(convertedSpeed))
            sleep(5)
            North.off()
            East.off()
        if direction > 112.5 and direction <= 167.5:
            South.on()
            East.on()
            print("The wind is blowing Southeast at a speed of {} mph.\n".format(convertedSpeed))
            sleep(5)
            South.off()
            East.off()
        if direction > 202.5 and direction <= 247.5:
            South.on()
            West.on()
            print("The wind is blowing Southwest at a speed of {} mph.\n".format(convertedSpeed))
            sleep(5)
            South.off()
            West.off()
        if direction > 292.5 and direction <= 337.5:
            North.on()
            West.on()
            print("The wind is blowing Northwest at a speed of {} mph.\n".format(convertedSpeed))
            sleep(5)
            North.off()
            West.off()
        print("Would you like to enter another city, Enter Y for yes or N for no")
        goAgain = raw_input()

except KeyboardInterrupt:
    print("exiting")
    gpiozero.close()


