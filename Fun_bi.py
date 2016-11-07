#coding=utf-8

#Fun_bi.py calculating distance for supersonic
import RPi.GPIO as gpio
import time

def shot(op,ip):
  gpio.setmode(gpio.BOARD)
  gpio.setup(op,gpio.OUT)
  gpio.setup(ip,gpio.IN)
  n=2#starting times 
  bj=400#counting 
  k=0
  for i in range(n):
    gpio.output(op,1)
    time.sleep(0.2)
    gpio.output(op,0)
    tt=0
    while gpio.input(ip)==0:
      tt+=1
      continue
    s=time.time()
    tt=0
    while gpio.input(ip)==1:
      tt+=1
      if tt>=bj : break
      continue
    t=time.time()
    ds=(t-s)*34300/2
    k+=ds
    #print ds,"   ",tt
    while gpio.input(ip)==1: continue
  k=k//n
  return k
