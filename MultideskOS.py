#!/usr/bin/python3
#MultideskOS

"""
Chez Multidesk on commente pas son code, il doit être compréhensible sans commentaires.
"""

import time, sys
from os import system, getlogin, geteuid
from random import randint

from static.static import pt, pt_chrono, pt_err, ent, pt_l, \
                c_green, c_red, c_lblue, c_blue

import apps.Horoscopy as hsp
import apps.NoHomoBot as nhb

shutdown=False

SPLASH="███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ███████╗███████╗██╗  ██╗ ██████╗ ███████╗\n████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██╔════╝██╔════╝██║ ██╔╝██╔═══██╗██╔════╝\n██╔████╔██║██║   ██║██║     ██║   ██║██║  ██║█████╗  ███████╗█████╔╝ ██║   ██║███████╗\n██║╚██╔╝██║██║   ██║██║     ██║   ██║██║  ██║██╔══╝  ╚════██║██╔═██╗ ██║   ██║╚════██║\n██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██████╔╝███████╗███████║██║  ██╗╚██████╔╝███████║\n╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝\n"
try:
    USER=getlogin().upper()
except:
    from pwd import getpwuid
    USER=getpwuid(geteuid())[0].upper()

MENU_LIST=['BIOS','Start (Pas le même que sur le Windows)','Panneau de configuration (Idem mais ça bug)','Program files','Aide','Définition phonétique','Stop']
MENU_APPLICATIONS=['DOSEmu (Mieux que Windows NT)','Microsoft (Pas obligé)','Compute','Eclipse pour ArnoldC','Windows Vistux Mint','AntiBug v2.0','FTP','Horoscopy','No Homo Bot']

cx = None
error = 0

def startx():
    system("clear")
    print(c_green("GRUB> PootOS.INI ..."))
    time.sleep(0.2)
    pt('Appuyez sur F11 (une fois) (puis ENTER mais après)')
    input()
    for i in SPLASH:
        if randint(0,1) == 1:
            print(c_blue(i),end='')
        else:
            print(c_lblue(i),end='')
        sys.stdout.flush()
        time.sleep(0.002)
    pt('....')
    time.sleep(1)
    pt_err('La garantie expire si vous lisez ceci')
    time.sleep(1)
    pt_err('MultideskOS ne supporte pas l\'assembleur, pour cela, utilisez LindowsOS\n(c\'est pas aussi bien que Multidesk)')
    time.sleep(1)
    pt_err('Seul les fichiers de 766 Octets sont pris en charge pour l\'instant')
    pt(c_blue(USER))
    pt('....')

################################################################################

startx()

while not shutdown and error == 0:
    pt_l(MENU_LIST)
    cx = None
    cx = ent()
    if cx == '':
        cx = ent()
    elif cx == ('menu' or 'm'):
        pt_l(MENU_LIST)
    elif cx == '0':
        pt(c_green('On a pas encore mis le BIOS mais on va le mettre'))
    elif cx == '1':
        pt(c_green('C\'est déjà démarré...'))
    elif cx == '2':
        error = 1
    elif cx == '3':
        pt_l(MENU_APPLICATIONS)
        cx = ent()

        if cx == '0':
            pt_err("'\\' found in home path, '/' expected.'")
        elif cx == '1':
            pt(c_green('Vraiment j\'insiste, c\'est à chier Microsoft...'))
        elif cx == '2':
            pt(c_green('\n#Compute> ON'))
            while 1:
                computed = ent()
                pt(c_red(computed))
                time.sleep(0.2)
                print(c_green("Done. (0.2ms)"))
        elif cx == '3':
            print(c_green("JAVA> Java2K.JAR ..."))
            time.sleep(5)
            pt_err('Fichier trop lent')
            error = 1
        elif cx == '4':
            pt_err("Ce programme essaye d'executer un exe windows, mais les exe windows ne tournent pas sous dos comme MultideskOS")
            error = 2
        elif cx == '5':
            pt('Scan des bugs...')
            for i in range(5):
                time.sleep(0.8)
                print('.',end='')
                sys.stdout.flush()
            print('')
            pt_err("Il y a 2-3 bugs mais pas de hacks")
        elif cx == '6':
            pt(c_green('Les serveurs ne sont pas POP ou IMAP'))
            pt('Entrez votre serveur:')
            ent()
        elif cx == '7':
            hsp.start_horoscopy()
        elif cx == '8':
            nhb.start_no_homo_bot()


    elif cx == '4' or cx == 'h' or cx == 'help':
        pt(c_blue('http://www.multideskos.com/'))

    elif cx == '5':
        pt(c_green("La phonétique (du grec « phônê » qui signifie la « voix », le « son ») est une branche de la linguistique qui étudie les sons utilisés dans la communication parlée. À la différence de la phonologie, qui étudie comment sont agencés les phonèmes d'une langue pour former des mots, la phonétique concerne les sons eux-mêmes (les unités phonétiques, les « phones »), leur production, leur variation plutôt que leur contexte. La sémantique ne fait donc pas partie de ce niveau d'analyse linguistique."))

    elif cx == '6' or cx == 'q' or cx == 'exit':
        shutdown = True
    elif cx.upper() == USER:
        pt(c_green('Vous venez d\'appeler une fonction.'))
        pt('Car pour appeler une fonction, il suffit de taper son nom.')
    else:
        error = 1
print("\n")
if error == 1:
    pt_err('Multidesk a planté')
elif error == 2:
    pt_err('Multidesk a encore planté')
elif error == 0:
    pt('Multidesk utilise des maintenant sa fonction fast shutdown...')
    pt_err('Vos données n\'ont pas été sauvegardée mais c\'est normal il y a que 4Mo de ROM')
else:
    pt_err('Multidesk a vraiment planté')

time.sleep(6)
