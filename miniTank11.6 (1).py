#set GPIO numbering mode and define output pins.
from os import system
import RPi.GPIO as GPIO
import time 
import curses
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)   #left motor coil A 
GPIO.setup(11,GPIO.OUT)  #left motor coil B
GPIO.setup(13,GPIO.OUT)  #right motor coil A
GPIO.setup(15,GPIO.OUT)  #right motor coil B
GPIO.setup(35,GPIO.OUT)  #left LED
GPIO.setup(37,GPIO.OUT)  #right LED

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()          # do not show keystrokes on screen
curses.cbreak()
screen.keypad(True)      #enable keystrokes
 
my_pwm1=GPIO.PWM(7,100)  #assign Pulse Width Modulation
my_pwm2=GPIO.PWM(11,100)
my_pwm3=GPIO.PWM(13,100)
my_pwm4=GPIO.PWM(15,100)

my_pwm1.start(0)
my_pwm2.start(0)
my_pwm3.start(0)
my_pwm4.start(0)
                         #variables
distance=.01
distanceCM=1
speed=100
speedSetting = 100
lights=False
lightSetting = ("off")                      
                         #init pin state
GPIO.output(35,False)
GPIO.output(37,False)

# define clear function 
def clear():  
        _ = system('clear')  
  
# now call function defined above 
def robotSetting():
	clear()
	print ("                 Speed = {0:3}%  Distance = {1:3} CM  Lights = {2}  ".format(speedSetting,distanceCM, lightSetting))
	
try:
        while True:  
            
            char = screen.getch()             #request keystroke

            if char == ord('p'):              #quit
                break
            elif char == ord('l'):            #light toggle
                if (lights) == False:
               		GPIO.output(35,True)
                        GPIO.output(37,True)
                        lights = True
			lightSetting = ("on")
			robotSetting()
	        else:
                        GPIO.output(35,False)
                        GPIO.output(37,False)
                        lights = False
			lightSetting = ("off")
			robotSetting()
            elif char == ord('='):            #increase distance variable
                if (distance) < 3.0:
                         distance = distance * 2
			 distanceCM = distance * 100
                         robotSetting()
		else:
                         robotSetting()
                    
            elif char == ord('-'):            #decrease distance variable 
                if (distance) > .01:
                         distance = distance / 2
                         distanceCM = distance * 100 
                         robotSetting()
                else:
			 robotSetting()
  
            elif char == ord('1'):              #speed control variable
                speed = 60
		speedSetting = 25
                robotSetting()
            elif char == ord('2'):
                speed = 70
		speedSetting = 50
                robotSetting()
            elif char == ord('3'):
                speed = 80
		speedSetting = 75
                robotSetting()
            elif char == ord('4'):
                speed = 100
		speedSetting = 100
                robotSetting()
            elif char == ord('w'):              #precise forward
                my_pwm1.ChangeDutyCycle(speed)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(speed)
                my_pwm4.ChangeDutyCycle(0)
                time.sleep(distance)
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(0)
               
            elif char == ord('s'):              #precise backward
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(speed)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(speed)
                time.sleep(distance)
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(0)
            elif char == ord('a'):              #precise left
                my_pwm1.ChangeDutyCycle(speed)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(speed)
                time.sleep(distance)
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(0)
                
            elif char == ord('q'):              #acute left
                my_pwm1.ChangeDutyCycle(speed)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(speed)
                time.sleep(distance/2)
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(0)
                
 
            elif char == ord('d'):              #precise right
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(speed)
                my_pwm3.ChangeDutyCycle(speed)
                my_pwm4.ChangeDutyCycle(0)
                time.sleep(distance)
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(0)
                time.sleep(.1)
            elif char == ord('e'):              #acute right
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(speed)
                my_pwm3.ChangeDutyCycle(speed)
                my_pwm4.ChangeDutyCycle(0)
                time.sleep(distance/2)
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(0)
   
            elif char == curses.KEY_UP:         #continious forward
                my_pwm1.ChangeDutyCycle(speed)
                my_pwm2.ChangeDutyCycle(0)
		my_pwm3.ChangeDutyCycle(speed)
		my_pwm4.ChangeDutyCycle(0)
            elif char == curses.KEY_DOWN:       #continious backward
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(speed)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(speed)
            elif char == curses.KEY_LEFT:       #continious left
                my_pwm1.ChangeDutyCycle(speed)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(speed)
            elif char == curses.KEY_RIGHT:      #continious right
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(speed)
                my_pwm3.ChangeDutyCycle(speed)
                my_pwm4.ChangeDutyCycle(0)
            elif char == 10:                    #stop motors
                my_pwm1.ChangeDutyCycle(0)
                my_pwm2.ChangeDutyCycle(0)
                my_pwm3.ChangeDutyCycle(0)
                my_pwm4.ChangeDutyCycle(0)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    my_pwm1.stop()
    my_pwm2.stop()
    my_pwm3.stop()
    my_pwm4.stop()
    GPIO.cleanup()
    
