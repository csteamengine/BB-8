import time
import serial
import pygame
import RPi.GPIO as GPIO
ser = serial.Serial('/dev/ttyACM0',9600)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
motor1 = GPIO.PWM(23,100)
motor1.start(0)
GPIO.setup(24, GPIO.OUT)
motor2 = GPIO.PWM(24,100)
motor2.start(0)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
done = False
LMA = 0
RMA = 0
motorOn = True
toArduino = 90
print("Script Loaded")
while done == False:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                 done = True
    controller = pygame.joystick.Joystick(0)
    controller.init()
    RU = controller.get_axis(3)
    RS = controller.get_axis(2)
    LU = controller.get_axis(1)
    LS = controller.get_axis(0)
    L2 = controller.get_button(8)
    R2 = controller.get_button(9)
    R1 = controller.get_button(11)
    L1 = controller.get_button(10)
    Up = controller.get_button(4)
    Down = controller.get_button(6)
    Start = controller.get_button(3)
    Select = controller.get_button(0)
    PS = controller.get_button(16)
    X = controller.get_button(14)
    if LU < 0:
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(17,GPIO.LOW)

        GPIO.output(27, GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)
    if LU > 0:
        GPIO.output(4, GPIO.LOW)
        GPIO.output(17,GPIO.HIGH)
        
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)

    if RMA > 100:
        RMA = 100
    if LMA > 100:
        LMA = 100
    if RMA < 40 and RMA != 0:
        RMA = 40
    if LMA < 40 and LMA !=0:
        LMA = 40
    
    LMA = 100 * abs(LU)
    RMA = 100 * abs(LU)
    if L1 == 1:
        LMA = 0
    if R1 == 1:
        RMA = 0

    if motorOn == True:
        motor1.ChangeDutyCycle(LMA)
        motor2.ChangeDutyCycle(RMA)
    if motorOn == False:
        motor1.ChangeDutyCycle(0)
        motor2.ChangeDutyCycle(0)
    RU = round(RU,2)
    ser.write(str(RU))
    print(ser.readline(), RU)
    if L1 ==1 and R1 == 1 and R2 == 1 and L2 ==1:
         done = True
         print("Done!")
    if X == 1:
        print "BEE BEE DOH"
    if Start == 1:
        motorOn = False
        print "motors Off"
    if Select == 1:
        motorOn = True
        print "motors On"
    clock.tick(30)
motor1.stop()
motor2.stop()
GPIO.cleanup()
pygame.quit()
