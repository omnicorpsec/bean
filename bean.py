import time
import sys
import subprocess
import os
import welcome
import fileinput
import shutil

def party(focus):
    print "\n----------------------------"
    print "\n~~~~~~~~~WAR~PARTY~~~~~~~~~~"
    print "\n        wizardking"
    print "\n          builder"
    print "\n           rouge"
    print "\n          warrior"
    print "\n        necromancer"
    print "\n           newjo"
    print "\n     quit, help, focus"
    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    cmdlist = []
    cmd = getcmd(cmdlist)
def getcmd(cmdlist):
    cmd = raw_input('\n ;o.0 >>')
    if cmd in cmdlist:
        return cmd
    elif cmd == 'wizardking':
        wizardking(focus)
    elif cmd == 'builder':
        builder(focus)
    elif cmd == 'rouge':
        rouge(focus)
    elif cmd == 'warrior':
        warrior(focus)
    elif cmd == 'necromancer':
        necromancer(focus)
    elif cmd == 'newjo':
        newjo(focus)

    elif cmd == 'help':
        print "\n This is help, just type the party member you want to know about"
        return getcmd(cmdlist)
    elif cmd == 'focus':
        clear()
        print "\n ~~~~~~~~~~FOCUSING~~~~~~~~~"
        time.sleep(2)
        clear()
        party(focus)
    elif cmd == 'secret':
        clear()
        print "\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*"
        print "\n ~~~~~~~~S E C R E T S~~~~~~~~"
        print "\n ~~~~~~~~~~~~~~O F~~~~~~~~~~~~"
        print "\n ~~~~~~~T H E  M A G I C~~~~~~"
        print "\n ~~~~~~~~~V A R I E T Y~~~~~~~"
        print "\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "\n*                             *"
    elif cmd == 'plan':
        warVision()
    elif cmd == 'quit':
        clear()
        print "\n destroying War Plan and exiting..."
        os.remove("warplan.txt")
        time.sleep(1)
        clear()
        print "\n....................... Goodbye...................."
        time.sleep(1)
        clear()
        exit(0)
    else:
        print "\n You can check help or your spelling"
        return getcmd(cmdlist)
def clear():
    subprocess.call('clear')
clear()

def start(focus):
    clear()
    print "####################################################################"
    print "# OK,                                                              #"
    print "#     it is time to make War,                                      #"
    print "#                                                                  #"
    print "#                  and every good war needs a plan,                #"
    print "#                                                    ~Newjo        #"
    print "####################################################################"
    print "\n...making war plan...getting Newjo..."
    #make txt file
    warPlan = open("warplan.txt","w")
    warPlan.write("~~~~~~~~~~W A R  P L A N~~~~~~~~~~")
    warPlan.write("============>>Newjo<<=============\n")
    warPlan.write("\n Wizard King:                     ")
    warPlan.write("\n                                  ")
    warPlan.write("\n The Builder:                     ")
    warPlan.write("\n                                  ")
    warPlan.write("\n The Rouge  :                     ")
    warPlan.write("\n                                  ")
    warPlan.write("\n The Warrior:                     ")
    warPlan.write("\n                                  ")
    warPlan.write("\n Necromancer:                     ")
    warPlan.write("\n                                  ")
    warPlan.write("\n Target:                          ")
    warPlan.write("\n                                  ")
    warPlan.write("\n War Chief:                       ")
    warPlan.write("\n \n \n \n ")
    warPlan.close()
    time.sleep(2)
    clear()
    print "\n \n \n \n \n \n \n"
    print "                                   ...W A R  P L A N..."
    time.sleep(2)
    clear()
    party(focus)

def warVision():
    clear()
    p1 = subprocess.call(["cat", "warplan.txt"])
    print "\n -focus to return to the War Party"
warVision()
def andintheshade():
    p1 = subprocess.call(["rm", "warplan.txt"])
    p2 = subprocess.call(["mv", "inthesun.txt","warplan.txt"])
andintheshade()
def tree():
    subprocess.call(["rm","inthesun.txt"])
tree()
def beanfook():
    bean = False
beanfook()
#party members and fuctions go here
####################################wizardKing##################
def wizardking(focus):
    clear()
    print "~~~~~~~~~~~~~~~~~~WAR~PARTY~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~\|/~~~~~~~~~~~~~"
    print "~~~~~~~\  |  /~~~~\|/{0}\|/~~~~~~~~~~"
    print "~~~~~~~~\_|_/~~~~~~|||||||~~~~~~~~~~~"
    print "~~~~~~~~~~\~~~~~~~{O}/.\{O}~~~~~~~~~~"
    print "~~~~~~~~~~~\~~~~~~\|\_-_/|/~~~~~~~~~~"
    print "~~~~~~~~~~~~\~~/ /\ \ | / /|~~~~~~~~~"
    print "~~~~~~~~~~~~~\/ /~~\|\|/|/ |~~~~~~~~~"
    print "~~~~~~~~~~~~~O0o~~~~| | | /~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~\~~~~| | |/~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~\~~~/V|V\~~~~~~~~~~~~"
    print "\n               The Wizard King, "
    print "\n            Order the Magic Attacks"
    print "\n "
    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "\n-magestorm, -whitemage, -blackmage,"
    print "\n    -redmage, -bluemage, focus"
    cmdlist = ['-magestorm', '-whitemage','-blackmage','-redmage','-bluemage']
    cmd = getcmd(cmdlist)
    
    if cmd == '-magestorm':
        clear()
        f_old = open('warplan.txt','r')
        f_new = open('inthesun.txt','w')
        for line in f_old:
            f_new.write(line)
            if 'King:' in line:
                f_new.write('\n          The Mages have started Storming')
            else:
               if 'started Storming' in line:
                clear()
                print "The Storm Has Already Started"
                f_old.close()
                f_new.close()
                tree() 
                time.sleep(3)
                wizardking(focus)
        f_old.close()
        f_new.close()
        andintheshade()
        print "\n This will initiate all mages at once"
        time.sleep(2)
        wizardking(focus)
    elif cmd == '-whitemage':
        clear()
        healcheck = open("warplan.txt","r")
        for line in healcheck:
            if 'Storming' in line:
                clear()
                print "\n MageStorm is Storming"
                time.sleep(2)
        healcheck.close()
        wizardking(focus)
    elif cmd == '-blackmage':
        clear()
        print "\n This will compare target against known exploits"
        time.sleep(2)
        wizardking(focus)
    elif cmd == '-redmage':
        clear()
        print "\n This will start SET and BeEf together with special java script"
        time.sleep(2)
        wizardking(focus)
    elif cmd == '-bluemage':
         clear()
         print "\n This will take care of time"
         time.sleep(2)
         wizardking(focus)
    else:
        return getcmd(cmdlist)


#######################Builder################################
def builder(focus):
    clear()
    print "\n~~~~~~~~~~~~~~~~~~~~WAR~PARTY~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~*~*~*~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~-[o_o]-~~~~~~~~~~~~"  
    print "~~\~|~/~~~~~~~~~~~~~~~~| |~~~~~~~~~~~~~~"
    print "~~~~0~~~~~~~~~~~~[   ] ROBOT [   ]~~~~~~~~~~~"
    print "~~~/|\~~~~~~~~~~~[x) /     ]~~~(0]~~~~~~~~~~~"
    print "~~/ | \~~~~~~~~~~(x)~~[    ]~~{__}~~~~~~~~~~~"   
    print "~/  |  \~~~~~~~~~/|\~~\    /~~ ||~~~~~~~.\|/."
    print "/   |   \~~~~~~~~\|/~~(0)(0)~~~{}~~~~~~~~~~~~~"
    print "\__/~\__/~~~~~~~~~I~~~[ ][ ]~~~~~~~~~~~~~~"
    print "(__\~/__)~~~~~~~~~~~~~[ ][ ]~~~~~~~~~~~~~~~~~~"
    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    print "\n              This is the Builder"
    print "\n What machines do you wish to make war with?"
    print "\n         -drone, -robot, -make, focus"
    cmdlist = ['-drone', '-robot', '-make']
    cmd = getcmd(cmdlist)
    
    if cmd == '-drone':
        clear()
        print "\n Recon is done by this drone"
        time.sleep(2)
        builder(focus)
    elif cmd == '-robot':
        clear()
        print "\n This is for making bots"
        time.sleep(2)
        builder(focus)
    elif cmd == '-make':
        clear()
        print "\n This is for automating tasks"
        time.sleep(2)
        builder(focus)
    else:
        return getcmd(cmdlist)
    
#######################Rouge##################################
def rouge(focus):
    clear()
    print "\n This is the Rouge"
    print "\n Where do you wish to sneak?"
    print "\n EvilTwin, NewFace, Disable, Poison, focus"
    cmdlist = ['EvilTwin','NewFace','Disable','Poison']
    cmd = getcmd(cmdlist)

    if cmd == 'EvilTwin':
        clear()
        print "\n Evil Twin Attack, wireless attack"
        time.sleep(2)
        rouge(focus)
    elif cmd == 'NewFace':
        clear()
        print "\n Anonymity, Tor restart, Macchanger, proxychains"
        time.sleep(2)
        rouge(focus)
    elif cmd == 'Disable':
        clear()
        print "\n Denial of Service Attack"
        time.sleep(2)
        rouge(focus)
    elif cmd == 'Poison':
        clear()
        print "\n Arp Poison"
        time.sleep(2)
        rouge(focus)
    else:
        return getcmd(cmdlist)
######################Warrior#################################
def warrior(focus):
    clear()
    print "\n This is The Warrior"
    print "\n What do you want to smash?"
    print "\n -smash, -bang, -slam, focus"
    cmdlist = ['-smash','-bang','-slam']
    cmd = getcmd(cmdlist)
    
    if cmd == '-smash':
        clear()
        print "\n BruteForce Attacks"
        time.sleep(2)
        warrior(focus)
    elif cmd == '-bang':
        clear()
        print "\n custom wordlist attacks"
        time.sleep(2)
        warrior(focus)
    elif cmd == '-slam':
        clear()
        print "\n Hash Attacks with vm on server"
        time.sleep(2)
        warrior(focus)
    else:
        return getcmd(cmdlist)
#####################Necromancer##############################
def necromancer(focus):
    clear()
    print "\n Necromancer"
    print "\n What would you like to summon?"
    print "\n -zombie, -skeleton, -demon, focus"
    cmdlist = ['-zombie','-skeleton','-demon']
    cmd = getcmd(cmdlist)

    if cmd == '-zombie':
        clear()
        print "\n Calling the undead army (RAT on ZOMBIE MACHINES)"
        time.sleep(2)
        necromancer(focus)
    elif cmd == '-skeleton':
        clear()
        print "\n Summoning a Skeleton (Party Member from Server)"
        time.sleep(2)
        necromancer(focus)
    elif cmd == '-demon':
        clear()
        print "\n Making minions on target machine, or server"
        time.sleep(2)
        necromancer(focus)
    else:
        return getcmd(cmdlist)
#####################newjo####################################
def newjo(focus):
    clear()
    warVision()
    print "\n This is Newjo, War Party Leader"
    print "\n  war, -check, -horn, -chief"
    cmdlist = ['war','-check','-horn','-chief']
    cmd = getcmd(cmdlist)

    if cmd == 'war':
        clear()
        print "\n When involved in multiple Wars"
        time.sleep(2)
        newjo(focus)
    elif cmd == '-check':
        clear()
        print "\n Shows what everyone is doing"
        time.sleep(2)
        newjo(focus)
    elif cmd == '-horn':
        clear()
        print "\n Starts events from server"
        time.sleep(2)
        newjo(focus)
    elif cmd == '-chief':
        clear()
        print "\n ssh into server to call on additional resources"
        time.sleep(2)
        newjo(focus)










if __name__=="__main__":
    focus  = ['Party']
    start(focus)
