import time
import serial
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
motor1 = GPIO.PWM(4,100)
motor1.start(0)
GPIO.setup(17, GPIO.OUT)
motor2 = GPIO.PWM(17,100)
motor2.start(0)
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
done = False
LMA = 0
RMA = 0
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
    if LU <= 0:
        LMA = 20 * abs(LU)
        RMA = 20 * abs(LU)
        if LS < 0:
            RMA += 10 * abs(LS)
        if LS > 0:
            LMA += 10 * abs(LS)

    motor1.ChangeDutyCycle(RMA)
    motor2.ChangeDutyCycle(LMA)
    if L1 ==1 and R1 == 1 and R2 == 1 and L2 ==1:
         done = True
         print("Done!")
    if X == 1:
        print "BEE BEE DOH"
    clock.tick(30)
motor1.stop()
motor2.stop()
GPIO.cleanup()
pygame.quit()
