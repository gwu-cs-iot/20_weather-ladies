import gpiozero
from time import sleep


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

        speedFlag = float(input("set input speed 0-240: "))
        print("Please input a direction, ex: N or SW, exit to end")
        direction = raw_input()

        if speedFlag > 240 or speedFlag < 0:
            speedFlag = float(input("set input speed 0-240: "))
        
        SpeedPWM.value = speedFlag/240
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


