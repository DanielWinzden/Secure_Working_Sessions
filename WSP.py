#!/usr/bin/python
#!encoding=UTF-8
import subprocess, time, os, sys

#installation
if not os.path.isdir('/home/.gomora'):
        os.makedirs('/home/.gomora')
	print("               +--------------+")
	print("               | Installation |")
	print("               +--------------+\n")
	subprocess.call(['sudo','apt-get','install','ccrypt','-y'])
	subprocess.call(['sudo','apt-get','install','mplayer','-y'])
	subprocess.call(['sudo','apt-get','install','python3.7','-y'])
	subprocess.call(['sudo','apt-get','install','git','-y'])
	if not os.path.isdir('/home/.gomora/Secure_Working_Sessions'):
		subprocess.call(['git','clone','https://github.com/DanielWinzden/Secure_Working_Sessions.git'])
        print("            +---------------------+")
        print("            | Installation sucess |")
        print("            +---------------------+\n")
#execution du programme

def cool_print(string, speed):
        string = list(string)
        i=0
        while i < len(string):
                time.sleep(speed)
                sys.stdout.write((string[i]))
                sys.stdout.flush()
                i=i+1
#introduction
def animation() :
	subprocess.call(['bash','/home/.gomora/Secure_Working_Sessions/ressources/declaration.sh'])
	cool_print('                                                      \n',0.01)
	cool_print('                      .                               \n',0.01)
	cool_print('                   .  |  .                            \n',0.01)
	cool_print('                 .    |    .                          \n',0.01)
	cool_print('               .      0      .                        \n',0.01)
	cool_print('                 .    |    .                          \n',0.01)
	cool_print('                   . _|_ .                            \n',0.01)
	cool_print('                      .                               \n',0.01)
	cool_print('                                                      \n',0.01)
	cool_print('                 ShadowedWSP',0.05)
	print('\n')
	time.sleep(2)

animation()

def clear_screen() :
	subprocess.call(['clear'])
	cool_print('                                                      \n',0)
        cool_print('                      .                               \n',0)
        cool_print('                   .  |  .                            \n',0)
        cool_print('                 .    |    .                          \n',0)
        cool_print('               .      0      .                        \n',0)
        cool_print('                 .    |    .                          \n',0)
        cool_print('                   . _|_ .                            \n',0)
        cool_print('                      .                               \n',0)
        cool_print('                                                      \n',0)

clear_screen()

def Main() :
	print('[Main]')
	print('|')
        print('|')
	print('|-1 Start a new session')
        print('|')
	print('|-2 Open a previous working sequence')
        print('|')
	print('|-3 Start a rootkit scan')
        print('|')
	print('|-4 Settings')
        print('|')
	print('|-5 About')
        print('|')
	print('|-6 Contact')
	print('|')
        print('|')
	print('+---http://ftp.fau.de/cdn.media.ccc.de/')

Main()
choice = input('Your choice :\n> ')
def About() :
	cool_print("This tool is aimed at help you to keep the integrity of your work,\n",0.09)
	cool_print("it considerabily reduce the risk of beeing infected by a third party,\n",0.09)
	cool_print("coded by ~       Morphovid\n",0.09)
	time.sleep(2)

def Start_a_new_session() :
	sequence = raw_input('\nenter the name of the sequence ?\n> ')
	duration = raw_input('\nenter the time you plan for it to be achieved (unit: minutes)\n> ')
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
if 0<choice<7 :
	if choice == 1 :
		Start_a_new_session()
	if choice == 2 :
		Open_a_previous_working_sequence()
	if choice == 3 :
		Start_a_rootkit_scan()
	if choice == 4 :
		Settings()
	if choice == 5 :
		About()
	if choice == 6 :
		Contact()
