import gpiozero
from time import sleep
import json
import requests
import sys

#Set up GPIO pins
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
        try:
            #get city and state data from user
            print("Please enter a city name: ")
            city = raw_input()
            print("Please input the corresponding state: ")
            state = raw_input()
        
            URL="https://api.openweathermap.org/data/2.5/weather"
            PARAMS = {'q':[city,state],'appid':'745774c81d84372e1972cab0a2bdc2c2'}
            response = requests.get(url = URL, params = PARAMS)
            data = response.json()
            rawSpeed= data["wind"]["speed"]
            direction = data["wind"]["deg"]

        
            #convert speed from m/s to mph
            convertedSpeed = rawSpeed * 2.237
            #highest ever wind speed = 231 used 240 as a buffer
            speedFlag = convertedSpeed / 240
            #set speed for motor
            SpeedPWM.value = speedFlag

        except:
            print("No data for {}, {}".format(city,state))
            exit()

        #each direction gets 45 degrees on the compass
        if direction > 337.5 or direction <= 22.5:
            North.on()
            print("In {}, {} the wind is blowing North at a speed of {} mph.\n".format(city,state,convertedSpeed))
            sleep(5)
            North.off()
        if direction > 67.5 and direction <=112.5:
            East.on()
            print("In {}, {} the wind is blowing East at a speed of {} mph.\n".format(city,state,convertedSpeed))
            sleep(5)
            East.off()
        if direction > 167.5 and direction <= 202.5:
            South.on()
            print("In {}, {} the wind is blowing South at a speed of {} mph.\n".format(city,state,convertedSpeed))
            sleep(5)
            South.off()
        if direction > 247.5 and direction <= 292.5:
            West.on()
            print("In {}, {} the wind is blowing West at a speed of {} mph.\n".format(city,state,convertedSpeed))
            sleep(5)
            West.off()
        if direction > 22.5 and direction <= 67.5:
            North.on()
            East.on()
            print("In {}, {} the wind is blowing Northeast at a speed of {} mph.\n".format(city,state,convertedSpeed))
            sleep(5)
            North.off()
            East.off()
        if direction > 112.5 and direction <= 167.5:
            South.on()
            East.on()
            print("In {}, {} the wind is blowing Southeast at a speed of {} mph.\n".format(city,state,convertedSpeed))
            sleep(5)
            South.off()
            East.off()
        if direction > 202.5 and direction <= 247.5:
            South.on()
            West.on()
            print("In {}, {} the wind is blowing Southwest at a speed of {} mph.\n".format(city,state,convertedSpeed))
            sleep(5)
            South.off()
            West.off()
        if direction > 292.5 and direction <= 337.5:
            North.on()
            West.on()
            print("In {}, {} the wind is blowing Northwest at a speed of {} mph.\n".format(city,state,convertedSpeed))
            sleep(5)
            North.off()
            West.off()
        #Ask user if they would like to go again
        print("Would you like to enter another city, Enter Y for yes or N for no")
        goAgain = raw_input()

except KeyboardInterrupt:
    #if exited using keyboard 
    print("exiting")
    gpiozero.close()


