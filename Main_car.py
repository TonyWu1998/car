#coding=utf-8

#Main_car.py 
import Mode_remote
import Mode_intelligence

mode="Hi"

while mode[0]<>'4':
  
  print "Creducation"
  print "Car V1.5 for motor car"
  print "---MODE---"
  print "1.Remote control"
  print "2.Intelligence"
  print "4.Exit"
  print "Please choose a mode with a num"
  mode=raw_input()

  if mode[0]=='1':
    Mode_remote.Main()
  elif mode[0]=='2':
    Mode_intelligence.Main()
