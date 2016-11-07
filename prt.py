#coding=utf-8

#Prt.py 
import sys
import os,sys
import termios

def getchar():
  fd=sys.stdin.fileno()
  if os.isatty(fd):
    old=termios.tcgetattr(fd)
    new=termios.tcgetattr(fd)
    new[3]=new[3]& ~termios.ICANON& ~termios.ECHO
    new[6][termios.VMIN]=1
    new[6][termios.VTIME]=0
    try:
      termios.tcsetattr(fd,termios.TCSANOW,new)
      termios.tcsendbreak(fd,0)
      ch=os.read(fd,7)
    finally:
      termios.tcsetattr(fd,termios.TCSAFLUSH,old)
  else:
    ch=os.read(fd,7)
  return(ch)
