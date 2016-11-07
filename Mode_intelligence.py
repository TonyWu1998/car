#coding=utf-8

#intelligence.py main program for car 
import time
import Run_pwm
import RPi.GPIO as gpio
import Fun_bi
import Fun_motor

#global setting 
max=320#map size 
MP=[[0 for X in range(max)] for y in range(max)]#map initialize 
DIR=1#intial direction 1
JD=13#warning distance of supersonic module
XX=0; YY=0

class pin:#supersonic IO
  ip=36  #Echo
  op=32   #Trig


class Auto:
  @staticmethod
  #running algorithm 
  def Map(x,y):
    global MP,DIR
    global JD

    #Direction  get position from direction 
    if DIR==1:
      fx=x; fy=y-1
      lx=x-1; ly=y
      rx=x+1; ry=y
    if DIR==2:
      fx=x+1; fy=y
      lx=x; ly=y-1
      rx=x; ry=y+1
    if DIR==3:
      fx=x; fy=y+1
      lx=x+1; ly=y
      rx=x-1; ry=y
    if DIR==4:
      fx=x-1; fy=y
      lx=x; ly=y+1
      rx=x; ry=y-1

    #calculating distance 
    s=Fun_bi.shot(pin.op,pin.ip)
    if s<JD: MP[fx][fy]=2
    if MP[fx][fy]==0: return 2
    else:
      Fun_motor.turn(0,90)
      s=Fun_bi.shot(pin.op,pin.ip)
      Fun_motor.turn(90,180)
      if s<JD: MP[rx][ry]=2
      if MP[rx][ry]==0: return 1

      Fun_motor.turn(180,90)
      s=Fun_bi.shot(pin.op,pin.ip)
      Fun_motor.turn(90,0)
      if s<JD: MP[lx][ly]=2
      if MP[lx][ly]==0: return 1
      if MP[fx][fy]==1: return 1
      if MP[rx][ry]==1: return 2
      if MP[lx][ly]==1: return 2
      return 1

  #alter direction 
  @staticmethod
  def cd(cds):
    global DIR
    if cds==1: DIR+=1
    if cds==2: DIR-=1
    if DIR>4: DIR=4
    if DIR<1: DIR=1
    return dir
  #map input 

  @staticmethod
  def mapout(kx):
    for i in range(kx):
      s=""
      for j in range(kx):
        s+=str(MP[160-kx2+j][160-kx2+i])
      print s

#main 
def Main():
  global JD
  global MODE
  Run_pwm.Car.stop()#pause 
  #speed setup
  gpio.setmode(gpio.BOARD)
  gpio.setup(12,gpio.OUT)
  gpio.setup(16,gpio.OUT)
  pr=gpio.PWM(12,50); pr.start(92)
  pl=gpio.PWM(16,50); pl.start(100)

  x=max//2; y=max//2
  MP[x][y]=1#ports 11
  #kx=1#step counting 
  while 1:
    d=Auto.Map(x,y)#algorithm
    if d==1:
      #kx+=1
      Run_pwm.Car.fowd()
      #alter coordinates 
      if DIR==1: y-=1
      if DIR==2: x+=1
      if DIR==3: y+=1
      if DIR==4: x-=1
    if d==2:
      Run_pwm.Car.right()
      Auto.cd(1)
    if d==3:
      Run_pwm.Car.left()
      Auto.cd(2)
    MP[x][y]=1#ports 11
    print "Run mode:",d,"  Direction:",DIR
    #Auto.mapout(10)
    time.sleep(0.2)#sleep time for each action

