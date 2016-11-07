#coding=utf-8

#Run_pwm intelligent control
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

#wheels control
class wheel:
  pins={'lt':[35,37],'rt':[33,31]}#wheels IO ports +\-
  def __init__(self,name):#initalize
    self.name=name
    self.pin=wheel.pins[self.name]
    gpio.setmode(gpio.BOARD)
    gpio.setup(self.pin[0],gpio.OUT)
    gpio.setup(self.pin[1],gpio.OUT)
    gpio.output(self.pin[0],0)
    gpio.output(self.pin[1],0)
    self.stop()
  def fowd(self):
    gpio.output(self.pin[0],gpio.HIGH)
    gpio.output(self.pin[1],gpio.LOW)
  def stop(self):
    gpio.output(self.pin[0],False)
    gpio.output(self.pin[1],False)
  def back(self):
    gpio.output(self.pin[0],gpio.LOW)
    gpio.output(self.pin[1],gpio.HIGH)

#car operator 
class Car:
  wheels=[wheel('lt'),wheel('rt')]
  @staticmethod
  def init():
    gpio.setmode(gpio.BOARD)
    for wheel in Car.wheels: wheel.stop()
  @staticmethod
  def stop():
    for wheel in Car.wheels: wheel.stop()
  @staticmethod
  def fowd():
    Car.stop()
    for wheel in Car.wheels: wheel.fowd()
    time.sleep(0.5)  #time for moving forward
    Car.stop()
  @staticmethod
  def back():
    Car.stop()
    for wheel in Car.wheels: wheel.back()
  @staticmethod
  def left():
    Car.stop()
    Car.wheels[1].fowd()
    Car.wheels[0].back()
    time.sleep(0.3)  #time for turning left 
    Car.stop()
  @staticmethod
  def right():
    Car.stop()
    Car.wheels[0].fowd()
    Car.wheels[1].back()
    time.sleep(0.3)  #time for turning right
    Car.stop()
    
