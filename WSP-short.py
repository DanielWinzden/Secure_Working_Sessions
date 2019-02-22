#!/usr/bin/python
import subprocess, time

#installation
subprocess.call(['sudo','apt-get','install','ccrypt','-y'])

print("		\033[1;31;40mWorking session provider\033[0m\n")
subprocess.call(['mplayer','./ressources/declaration.wav'])

sequence = input('\nenter the name of the sequence ?\n')
time = input('\nenter the time you plan for it to be achieved (unit: minutes)\n')
