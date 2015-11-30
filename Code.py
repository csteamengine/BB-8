import time
import serial
import pygame


pygame.init()
pygame.joystick.init()
ser = serial.Serial('/dev/ttyACM0',9600)
clock = pygame.time.Clock()
Side = False
Forw = False
done = False
TiltAmount = 50
AutoPilot = False
#StartEngines = False
Rup = 0
Lright = 0
YawLeft = 0
Lleft = 0
hover = 1000
time.sleep(10)
YawRight = 0
Lfor = 0
Lback = 0
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


    if AutoPilot == False:# and StartEngines ==True:
         if RU < 0:
             Rup = (2000 - hover) * abs(RU)
         elif RU > 0:
             Rup = 0 - (hover - 800) * abs(RU)
         else:
             Rup = 0

         if RS < 0:
             YawLeft = 0- TiltAmount*abs(RS)
         elif RS > 0:
             YawRight =0- TiltAmount*abs(RS)
         else:
             YawRight = 0
             YawLeft = 0

         if LU < 0:
             Lfor =0- TiltAmount*abs(LU)
             Forw = True
             Lback =0
         elif LU > 0:
             Lback = 0-TiltAmount*abs(LU)
             Forw = True
             Lfor = 0
         else:
             Lfor = 0
             Lback = 0
             Forw = False

         if LS < 0:
             Lright =0- TiltAmount*abs(LS)
             Side = True
             Lleft = 0
         elif LS > 0:
             Lleft = 0-TiltAmount*abs(LS)
             Side = True
             Lright = 0
         else:
             Lleft = 0
             Lright = 0
             Side = False

         #if Side == False:
                 #if GYSide > 0:
                     #GyLeft = TiltAmount*GYSide
                 #if GYSide < 0:
                     #GyRight = TiltAmount*abs(GYSide)
                 #if GYSide == 0:
                     #GyRight = 0
                     #GyLeft = 0
         #if Front == False:
             #if GYFor <0:
                     #GyFront = TiltAmount*abs(GYFor)
             #if GYFor >0:
                     #GyBack = TiltAmount*GYFor
             #if GYFor == 0:
                     #GyFront = 0
                     #GyBack = 0
    RMA = hover + Rup + Lleft + YawLeft#  +GyRight
    LMA = hover + Rup + Lright + YawLeft# + GyLeft
    BMA = hover + Rup + Lback + YawRight# + GyBack
    FMA = hover + Rup + Lfor + YawRight#  + GyFront
    if AutoPilot == True:
         RMA = hover # + gyro
         FMA = hover # + gyro
         LMA = hover # + gyro
         BMA = hover # + gyro
    ser.write(str(FMA) + ',' + str(BMA) + ',' + str(BMA) + ',' + str(LMA))
    if L1 ==1 and R1 == 1 and R2 == 1 and L2 ==1:
         done = True
         print("Done!")
         ser.write('700,700,700,700')
    if Up == 1:
         if hover < 2000:
             hover = hover + 50
             print("Hover Increased: {}".format(hover))
    if Down == 1:
         if hover >= 750:
             hover = hover - 50
             print("Hover Decreased")
    if Select == 1:
         AutoPilot = False
         print("AutoPilot Disengaged")
    if PS == 1:
         AutoPilot = True
         print("AutoPilot Engaged")
    #if Start ==1:
         #StartEngines == True
    if X == 1:
         hover = 1000
         print("Hover reset: 1000")
    clock.tick(30)
pygame.quit()
