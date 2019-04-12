#!/usr/bin/env python2.7
import keyboard
import os
import time

capsActive = False

def capsPressed():
  keyboard.wait('capslock')
  return True

def main():
  while capsPressed():
    capsActive = not capsActive
    if capsActive:
      os.system("eject")
      os.system("notify-send \"Alarm! Some one pressed CAPSLOCK!\"")

try:
  main()
except KeyboardInterrupt:
  print(" <- I can't believe u done this")
  quit()
