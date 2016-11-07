#coding=utf-8

#Mode_remote.py 
import RPi.GPIO as gpio
import time
import prt
import Run_mt
#import Fun_buzz


def Main():
  
  commands={'w':Run_mt.Car.fowd,
    'a':Run_mt.Car.left,
    's':Run_mt.Car.back,
    'd':Run_mt.Car.right,
    'j':Run_mt.Car.stop,
    
  }


  print "<w> - Forward    <s> - Back"
  print "<a> - Turn left  <d> - Turn right"
  print "<k> - Buzz       <p> - Exit"


  gpio.setmode(gpio.BOARD)
  gpio.setup(12,gpio.OUT)
  gpio.setup(16,gpio.OUT)
  pr=gpio.PWM(12,50); pr.start(92)
  pl=gpio.PWM(16,50); pl.start(100)


  commands['j']()#Init
  wd=prt.getchar()
  while wd<>'p':
    if wd in commands: commands[wd]()
    time.sleep(0.05)
    wd=prt.getchar()
  Run_mt.Car.stop()
  pr.stop(); pl.stop()
  print "Now you exit the remote MODE"

