#!/usr/local/bin/python
# coding: latin-1
#if you use this code give me credit @tuf_unkn0wn
#i do not give you permission to show / edit this script without my credit
#to ask questions or report a problem message me on instagram @tuf_unkn0wn
"""


 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████ ▓█████▄ 
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▒██▀ ██▌
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ░██   █▌
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ░▓█▄   ▌
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░▒████▓ 
 ▒ ▒░▒ ▒▒   ▓▒█ ░▒ ▒  ░▒ ▒▒ ▓▒ ▒░ ░ ▒▒▓  ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░ ░ ▒  ▒ 
 ░   ░  ░   ▒   ░        ░  ░    ░    ░ ░  ░ 
 ░  ░  ░      ░   ░      ░  ░      ░  ░   ░    
                  ░                       ░      


"""
import os
import sys
import random
lred = '\033[91m'
lblue = '\033[94m'
lgreen = '\033[92m'
yellow = '\033[93m'
cyan = '\033[1;36m'
purple = '\033[95m'
red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
orange = '\033[33m'

colorlist = [red, blue, green, yellow, lblue, purple, cyan, lred, lgreen, orange]
randomcolor = random.choice(colorlist)
banner3list = [red, blue, green, purple]

def mainbanner1():
	print """\033[1;36m
       ┬  ┬┌┬┐┌─┐\033[0m  
       │  │ │ ├┤ \033[1;36m  
       ┴─┘┴ ┴ └─┘ \033[0m 
██╗  ██╗████████╗██╗  ██╗
██║  ██║╚══██╔══╝██║ ██╔╝\033[1;36m
███████║   ██║   █████╔╝ \033[0m
██╔══██║   ██║   ██╔═██╗ 
██║  ██║   ██║   ██║  ██╗
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
	\n""".decode('utf-8')

def mainbanner2():
	print """
                ░░▒█████████
              ▒▓▓█████████████
            ░▓█████████████████████░ ░▒███▓ 
          ░▓██████████████████████████████████ 
        ░░▒▓▓▓███████████┬  ┬┌┬┐┌─┐████████████▓  
     ░▓██████▓▓██████████│  │ │ ├┤ █████████████▓░
  ░▓██████▓███████▓██████┴─┘┴ ┴ └─┘████████████████░
    ░░▒░░░░▒▒▒▓▓░░▒███████████████████████████▓▓▓░   
                 ░░░▒░░░▒▓▓▒░▒▒░▒▓████████▓▓██▒▒░ 
                                ░▒░░░░░░▒░░░░░░░  
	\n""".decode('utf-8')

def mainbanner3():
	print """
╔═══════════════════════════════════════════════╗
║                                               ║
║     {0}    ██░ ██ ▄▄▄█████▓ ██ ▄█▀ ██▓ \033[0m          ║
║     {1}   ▓██░ ██▒▓  ██▒ ▓▒ ██▄█▒ ▓██▒  \033[0m         ║
║      {2}  ▒██▀▀██░▒ ▓██░ ▒░▓███▄░ ▒██░   \033[0m        ║
║      {3}  ░▓█ ░██ ░ ▓██▓ ░ ▓██ █▄ ▒██░           \033[0m║
║      {4}  ░▓█▒░██▓  ▒██▒ ░ ▒██▒ █▄░██████▒       \033[0m║
║       {5}  ▒ ░░▒░▒  ▒ ░░   ▒ ▒▒ ▓▒░ ▒░▓  ░       \033[0m║
║       {6}  ▒ ░▒░ ░    ░    ░ ░▒ ▒░░ ░ ▒  ░       \033[0m║
║       {7}  ░  ░░ ░  ░      ░ ░░ ░   ░ ░          \033[0m║
║       {8}  ░  ░  ░         ░  ░       ░  ░       \033[0m║
║                                               ║
║                                               ║
╚═══════════════════════════════════════════════╝
	""".decode('utf-8').format(random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list), random.choice(banner3list))

def mainbanner4():
	print """\033[0m
████████████████████████████████████████████████████████████████████████████\033[91m
███  ███████  ██          █   ███   ███████    ████████ ██      ████████████\033[33m
████ ███████ ██████    █████ ██  █████████ █  █ █████████ ██  ██ ██████  ███\033[93m
████  █████  ███████  ██████   █████████████  ████████   ███  █████     ████\033[92m
████         ██████    █████  █████████████    ██████ █ █ ██  ██ █ █████ ███\033[94m
████  █████  ███████  ██████   █████████████  █████████ ████  ███        ███\033[1;36m
████ ███████ ███████  ██████ ██  ███████████  █████ ███ ████  ██ █ █████████\033[95m
███   █████   █████    ████   ███   ████████        ██   ███  ████       ███\033[0m
████████████████████████████████████████████████████████████████████████████
	\033[0m\n""".decode('utf-8')

def mainbanner5():
	print """\033[92m
                                                
  █ ▄    ▄ █                    ▄███▄           ▄██ ▄███▀
  ███    ███                 ▄█████████▄        ███▐██▀
  ███    ███                 ██▀▀███▀▀██        █████▀
  ███▄▄▄▄███                 ▀   ███   ▀       ██████▄
  ███▀▀▀▀███                 ▄   ███   ▄        ███▐██▄
  ███    ███ \033[0m┌─┐┌─┐┬┌─┌─┐┬─┐┌─┐  \033[92m███  \033[0m┌─┐┌─┐┬   \033[92m███ ▀███▄ \033[0m┬┌┬┐\033[92m
  ███    ███ \033[0m├─┤│  ├┴┐├┤ ├┬┘└─┐  \033[92m███  \033[0m│ ││ ││   \033[92m███    ██ \033[0m│ │ \033[92m
  █        █ \033[0m┴ ┴└─┘┴ ┴└─┘┴└─└─┘ \033[92m▀███▀ \033[0m└─┘└─┘┴─┘ \033[92m▀       ▀ \033[0m┴ ┴\033[92m


            
                ███    
                █ █        
                █ █        ██ ████████ ███████
                █ █        ██    ██    ██  
                █ █        ██    ██    █████
                █ █     ▄  ██    ██    ██
                █████▄▄██  ██    ██    ███████
         

	""".decode('utf-8')

def mainbanner6():
	print """
 • \033[35m▄█\033[0m .  \033[35m█▄  \033[0m.     \033[35m███  \033[0m.  •  \033[35m▄█   ▄█▄\033[0m. \033[35m▄█ \033[0m•      
  \033[35m█#█    █#█\033[0m•  \033[35m▀████=████▄\033[0m.  \033[35m███ ▄█ █▀ █⇣█ \033[0m.      
. \033[35m█#█ \033[0m. •\033[35m█#█ \033[0m.    \033[35m▀█-█▀▀██  \033[0m.\033[35m█ █▐ █▀ \033[0m• \033[35m█L█   \033[0m.    
 \033[35m▄███▄▄▄▄███▄▄   \033[0m. \033[35m█▪█ \033[0m. \033[35m▀  ▄█████▀   \033[0m.\033[35m█i█      
▀▀█+█▀▀▀▀█+█▀  \033[0m•   \033[35m█▪█   \033[0m. \033[35m▀▀█ █ █▄\033[0m.   \033[35m█t█    \033[0m.  
 .\033[35m█•█  \033[0m. \033[35m█•█ \033[0m.     \033[35m█▪█  \033[0m•    \033[35m███▐ █▄ \033[0m. \033[35m█e█  \033[0m.     
  \033[35m█+█    █+█   \033[0m.   \033[35m█▪█    \033[0m.  \033[35m█ █\033[0m.\033[35m▀█ █▄ █⇡█▌  \033[0m• \033[35m▄ 
\033[0m• \033[35m███   \033[0m.\033[35m█▀  \033[0m.   \033[35m ▄████▀ \033[0m.   \033[35m███ \033[0m. \033[35m▀█▀ █████▄▄██ 
    \033[0m .           .  .     .  \033[35m▀        \033[0m•\033[35m▀\033[0m]         
	""".decode('utf-8')
def mainbanner7():
	print """\033[31m
██╗  ██╗████████╗██╗  ██╗     ██╗     ██╗████████╗███████╗
██║  ██║╚\033[91m══██╔══╝██║ ██╔╝     ██║     ██║╚══██╔══╝██╔════╝
███████║   ██║   █████╔╝████\033[33m█╗██║     ██║   ██║   █████╗  
██╔══██║   ██║   ██╔═██╗╚════╝\033[93m██║     ██║   ██║   ██╔══╝  
██║  ██║   ██║   ██║  ██╗     ███████╗██║   ██║   ███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚══════╝╚═╝   ╚═╝   ╚══════╝\033[0m
	""".decode('utf-8')

def mainbanner8():
	print """\033[34m
██╗  ██╗████████╗██╗  ██╗     ██╗     ██╗████████╗███████╗
██║  ██║╚══██╔══╝██║ ██╔╝     ██║     ██║╚══██╔══╝██╔════╝
███████║   ██║   █████╔╝█████╗█\033[94m█║     ██║   ██║   █████╗  
██╔══██║   ██║   ██╔═██╗╚════╝██║     ██║   ██║   ██╔══╝  
██║  ██║   █\033[1;36m█║   ██║  ██╗     ███████╗██║   ██║   ███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚══════╝╚═╝   ╚═╝   ╚══════╝
	\033[0m""".decode('utf-8')

def mainbanner9():
	print """\033[93m
██╗  ██╗████████╗██╗  ██╗     ██╗     ██╗████████╗███████╗
██║  ██║╚══██╔══╝██║ ██╔╝     ██║     ██║╚══██╔══╝██╔════╝
███\033[92m████║   ██║   █████╔╝█████╗██║     ██║   ██║   █████╗  
██╔══██║   ██║   ██╔═██╗╚════╝\033[32m██║     ██║   ██║   ██╔══╝  
██║  ██║   ██║   ██║  ██╗     ███████╗██║   ██║   ███████╗
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚══════╝╚═╝   ╚═╝   ╚══════╝
	\033[0m""".decode('utf-8')

def mainbanner():
	import random
	for x in range(10):
	  num = random.randint(1,9)
	if num == 1:
		mainbanner1()
	if num == 2:
		mainbanner2()
	if num == 3:
		mainbanner3()
	if num == 4:
		mainbanner4()
	if num == 5:
		mainbanner5()
	if num == 6:
		mainbanner6()
	if num == 7:
		mainbanner7()
	if num == 8:
		mainbanner8()
	if num == 9:
		mainbanner9()

mainbanner()
