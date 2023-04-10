import keyboard
import math as m
import json
import time


Turn = 0
YMov = 0
xMov = 0


Key = True
TRotL = 0
AutoShoot = 0

while True:
    start = time.time()
    Rbot = open('myRobot.txt', 'rt')
    Gme = open('GameElements.txt', 'rt')
    try:
        Robot = json.load(Rbot)
        Game = json.load(Gme)
    except:
        continue

    Controls = open('Controls.txt', 'w')

    #grabs positions
    RPos = Robot['myrobot'][0]['global pos']
    RVol = Robot['myrobot'][0]['velocity']
    RAngle = Robot['myrobot'][0]['global rot']
    RRotV = Robot['myrobot'][0]['rot velocity']

    '''
    #Writes to the controls text file
    Controls.write()
    '''
    #Prints for debugging
    '''print()  '''

    if keyboard.is_pressed('`'):
        break

    #Keeps fps at 60
    time.sleep(max(1./60 - (time.time() - start), 0))
#cheat sheet
'''
a=0
b=0
x=0
y=0
dpad_left=0
dpad_right=0
bumper_l=0
bumper_r=0
stop=0
restart=0
right_y=0
right_x=0
left_y=0
left_x=0
trigger_l=0
trigger_r=0
'''
