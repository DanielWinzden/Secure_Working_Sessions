#!/usr/bin/python
#!encoding=UTF-8
import subprocess, time, os, sys

#installation
if not os.path.isdir('/home/.ressources'):
        os.makedirs('/home/.ressources')
	print("               +--------------+")
	print("               | Installation |")
	print("               +--------------+\n")
	subprocess.call(['sudo','apt-get','install','ccrypt','-y'])
	subprocess.call(['sudo','apt-get','install','mplayer','-y'])
	subprocess.call(['sudo','apt-get','install','python3.7','-y'])
	subprocess.call(['sudo','apt-get','install','git','-y'])
	os.chdir("/home/.ressources")
	if not os.path.isdir('/home/.ressources/Secure_Working_Sessions'):
		subprocess.call(['git','clone','https://github.com/DanielWinzden/Secure_Working_Sessions.git'])
        print("               +---------------------+")
        print("               | Installation sucess |")
        print("               +---------------------+\n")
#execution du programme
print("               +--------------------------+")
print("               | Working session provider |")
print("               +--------------------------+\n")
#fonctions subalternes
def cool_print(string):
        string = list(string)
        i=0
        while i < len(string):
                time.sleep(0.09)
                sys.stdout.write((string[i]))
                sys.stdout.flush()
                i=i+1
#coeur du code
cool_print("This tool is aimed at help you to keep the integrity of your work,\n")
cool_print("it considerabily reduce the risk of beeing infected by a third party,\n")
cool_print("coded by ~ Morphovid")
time.sleep(2)
subprocess.call(['bash','/home/.ressources//Secure_Working_Sessions/declaration.sh'])

sequence = raw_input('\nenter the name of the sequence ?\n')
duration = raw_input('\nenter the time you plan for it to be achieved (unit: minutes)\n')
duration = int(duration)*60

print(str('\nStarting sequence : ')+str(sequence)+str('...\n'))
x=0
i=0
a=0
b=0
while i<duration:
	sys.stdout.write(str('\rWork in progress')+str(x)+str('%'))
	sys.stdout.flush()
	time.sleep(1)
	i=i+1
	x=i*100
	x=x/duration
	if x >= 25 and a == 0 :
		a=1
	if x >= 50 and a == 0 :
		b=1
