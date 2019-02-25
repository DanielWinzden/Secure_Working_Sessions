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
	subprocess.call(['sudo','apt-get','install','zenity','-y'])
	subprocess.call(['sudo','apt-get','install','git','-y'])
	subprocess.call(['sudo','apt-get','install','xterm','-y'])
	subprocess.call(['sudo','apt-get','install','nautilus','-y'])
	if not os.path.isdir('/home/.gomora/Secure_Working_Sessions'):
		subprocess.call(['git','clone','https://github.com/DanielWinzden/Secure_Working_Sessions.git'])
	print("Please, choose the directory where you'll work")
	subprocess.call(['zenity', '--file-selection', '--title="Choose a directory"', '--directory', '>', 'directory'])
	file = file.open('./directory','r')
	directory = file.readlines()
	print(directory)
        print("            +---------------------+")
        print("            | Installation sucess |")
        print("            +---------------------+\n")
#definition des fonctions subalternes

def cool_print(string, speed):
        string = list(string)
        i=0
        while i < len(string):
                time.sleep(speed)
                sys.stdout.write((string[i]))
                sys.stdout.flush()
		i=i+1

def animation() :
	subprocess.call(['bash','/home/.gomora/Secure_Working_Sessions/ressources/declaration.sh'])
	print('\n')
	cool_print('                      .                               \n',0.02)
	cool_print('                   .  |  .                            \n',0.02)
	cool_print('                 .    |    .                          \n',0.02)
	cool_print('               .      0      .                        \n',0.02)
	cool_print('                 .    |    .                          \n',0.02)
	cool_print('                   . _|_ .                            \n',0.02)
	cool_print('                      .                               \n',0.02)
	cool_print('\n                 ShadowedWSP',0.1)
	print('\n')
	time.sleep(2)

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

def Main() :
	print('[Main]')
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
	print('+---http://ftp.fau.de/cdn.media.ccc.de/')

def choose_a_dir () :
	subprocess.call(['bash','/home/.gomora/Secure_Working_Sessions/ressources/choose_dir.sh'])
	file = open('/home/.gomora/Secure_Working_Sessions/ressources/dir','r')
	directory = file.readlines()
	file.close()
	directory = directory[0]
	os.remove('/home/.gomora/Secure_Working_Sessions/ressources/dir')
	return directory

def save_session(directory) :
	file = open('/home/.gomora/Secure_Working_Sessions/ressources/sessions_list','a')
	file.write(directory)
	file.close()

def remove_n(liste) :
	clear_list = []
	for i in range(len(liste)) :
		element=liste[i]
		element = list(element)
		element.pop(len(element)-1)
		clear_element = ''.join(str(i) for i in element)
		clear_element=str(clear_element)
		clear_list.append(clear_element)
	return clear_list

def read_dir_list() :
        file = open('/home/.gomora/Secure_Working_Sessions/ressources/sessions_list','r')
        dir_list = file.readlines()
        file.close()
        return dir_list

def read_previous_sequences_title () :
	none = none
#execution du proigramme

#introduction

#animation()

clear_screen()

Main()

choice = input('\nYour choice :\n> ')

#submenus

def About() :
	cool_print("This tool is aimed at help you to keep the integrity\n",0.06)
	cool_print("of your work, it considerabily reduce the risk of\n",0.06)
	cool_print("beeing infected by a third party.\n",0.06)
	cool_print("\ncoded by ~       Morphovid\n",0.06)
	time.sleep(3)
	clear_screen()
	Main()

def Start_a_new_session() :
	sequence = raw_input('\nenter the name of the sequence :\ne.g : "Finish the html module" , "Learn about Li-Fi networks" , "Newspaper break" etc... \n> ')
	duration = raw_input('\nenter the time you plan for it to be achieved (unit: minutes)\n> ')
	duration = int(duration)*60

	print('\nNow please choose a directory for your session ... ')
	time.sleep(3)
	directory = choose_a_dir()
        dir_list = save_session(directory)
	dir_list = remove_n(dir_list)

	print(str('\nStarting sequence : ')+str(sequence)+str('...\n'))

	subprocess.call(['bash','/home/.gomora/Secure_Working_Sessions/ressources/new_session.sh'])
	x=0
	i=0
	a=0
	b=0
	c=0
	d=0
	while i<duration:
		sys.stdout.write(str('\rWork in progress ')+str(x)+str('%'))
		sys.stdout.flush()
		time.sleep(1)
		i=i+1
		x=i*100
		x=x/duration
		if x >= 25 and a == 0 :
			a=1
		if x >= 50 and a == 0 :
			b=1
                if x >= 75 and a == 0 :
                        c=1
                if x >= 100 and a == 0 :
                        d=1
	print('\n')

def Open_a_previous_working_sequence() :
	print('[previous working sessions : ]')
        k=0
	dir_list = read_dir_list()
	dir_list = remove_n(dir_list)
	print('|')
	for i in range(len(dir_list)) :
                print(str('|-')+str(k)+str(' ')+str(dir_list[i]))
		k=k+1
	print('|')
	print('+---http://ftp.fau.de/cdn.media.ccc.de/')
	choice = input('Your choice :\n> ')
	dir=dir_list[choice]
	dir = str('"')+str(choice)+str('"')
	subprocess.call(['nautilus',dir])

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
"""
NOTES :

-pour la reouverture d'ancienne session, demander a nautilus de s'ouvrir dans la
directory enregistree avec >/dev/null 2>&1 </dev/null &

-pour ouvrir un nouveau terminal |a chaque debut de tache| : xterm -hold -e command >/dev/null 2>&1 </dev/null &

"""
