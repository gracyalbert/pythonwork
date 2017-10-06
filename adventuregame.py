from time import *
from random import *
import os,sys
import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

sword = 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#This is a function, we use it to do lots of things and then call it by it's name later on
#To create a function we use "def name():" where name can be anything.

def clear_screen():  #Simple function that clears the screen
    os.system('cls' if os.name=='nt' else 'clear')
def title():
     print ("   ░█▀▀█ ▒█▀▀▄ ▒█░░▒█ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀ ▒█░▒█ ▒█▀▀█ ▒█▀▀▀ 　 ▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ▒█▀▀▀ ")
     print ("   ▒█▄▄█ ▒█░▒█ ░▒█▒█░ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░ ▒█░▒█ ▒█▄▄▀ ▒█▀▀▀ 　 ▒█░▄▄ ▒█▄▄█ ▒█▒█▒█ ▒█▀▀▀ ")
     print ("   ▒█░▒█ ▒█▄▄▀ ░░▀▄▀░ ▒█▄▄▄ ▒█░░▀█ ░▒█░░ ░▀▄▄▀ ▒█░▒█ ▒█▄▄▄ 　 ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█▄▄▄ ")

def castle():

    print ("*                                 |>>>                    +        ")
    print ("+          *                      |                   *       +")
    print ("                    |>>>      _  _|_  _   *     |>>>		   ")
    print ("           *        |        |;| |;| |;|        |                 *")
    print ("     +          _  _|_  _    \\.    .  /    _  _|_  _       +")
    print (" *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|")
    print ("               \\..      /    ||:+++. |    \\.    .  /           *")
    print ("      +         \\.  ,  /     ||:+++  |     \\:  .  /")
    print ("                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *")
    print ("          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +")
    print ("                 ||+++ ||.    .     .      . ||+++.|   *")
    print ("+   *            ||: . ||:.     . .   .  ,   ||:   |               *")
    print ("         *       ||:   ||:  ,     +       .  ||: , |      +")
    print ("  *              ||:   ||:.     +++++      . ||:   |         *")
    print ("     +           ||:   ||.     +++++++  .    ||: . |    +")
    print ("           +     ||: . ||: ,   +++++++ .  .  ||:   |             +")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |        *")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |")


def north():
    print ("To go north press n then enter")

def east():
    print ("To go east press e then enter")

def south():
    print ("to go south press s then enter")

def west():
    print ("To go west press w then enter")


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
     
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name player? ")
    #randint is a great way of adding some variety to your players statistics.
    HP = randint(5,20)
    MP = randint(5,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi", "Are you a hero?", "Are you from this village?", "There has been a dark shadow cast across the village"]
    npcnamechoice = ["Roger", "Dexter", "Sarah", "Susan"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to the villager")
    time.sleep(1)
    if input() == "y":
        print ("["+npcname+":] " +responses[0])
    else:
        print("["+npcname+":] Goodbye")

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "monster"
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("                 SUDDENLY...                    ")
    print ("   YOU HEAR A ROAR, AND FROM THE SHADOW YOU     ")
    print ("  SEE AN "+enemyname+" COMING STRAIGHT AT YOU   ")
    print ("                       ----------Oooo---        ")
    print ("                      -----------(----)---       ")
    print ("                      ------------)--/---- ")
    print ("                      ------------(_/- ")
    print ("                      ----oooO---- ")
    print ("                      ----(---)---- ")
    print ("                      -----\--(-- ")
    print ("                      ------\_)- ")
    print ("                      -----------Oooo--- ")
    print ("                      -----------(----)--- ")
    print ("                      ------------)--/---- ")
    print ("                      ------------(_/- ")
    print ("                      ----oooO---- ")
    print ("                      ----(---)---- ")
    print ("                      -----\--(-- ")
    print ("                      ------\_)- ")
    print (" ")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #print enemyname
    print ("Your enemy has " + " " + str(enemyHP) + " " + "Health Points")
    print ("Your enemy has " + " " + str(enemyMP) + " " + "Magic Points")
    print ("""  A. Grab a nearby rock and throw it at the monster
    B. Lie down and wait to be mauled
    C. Run""")
    choice = input(">>> ") #Here is your first choice.
    if choice in answer_A:
      option_rock()
    elif choice in answer_B:
      print ("\nWelp, that was quick. ")
      print ("                  _______$___________$_______")
      print ("                  _____$$_____________$$_____")
      print ("                  ____$____$$$___$$$____$____")
      print ("                  ________$$$$$_$$$$$________")
      print ("                  ________$$$$$_$$$$$________")
      print ("                  ________$$$$$_$$$$$________")
      print ("                  _________$$$___$$$_________")
      print ("                  ___$__________________$____")
      print ("                  ____$________________$_____")
      print ("                  _____$$$$$$$$$$$$$$$$______")
      print ("                  ___________$$$$$$$_________")
      print ("                  ____________$$$$$$$________")
      print ("                  _____________$$$$$$________")
      print ("                  ______________$$$$_________")
      print ("             YOU DIED!             ")
    elif choice in answer_C:
      option_run()
    else:
      print (required)
      
def option_rock():
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("  The monster is stunned, but regains control.  ")
  print ("             He begins                          ")
  print ("  running towards you again. Will you:          ")
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run towards a nearby cave""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
   print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   print ("      You decided to throw another rock,        ")
   print ("                 as if the first                ") 
   print ("      rock thrown did much damage.              ")
   print ("          The rock flew well over the ,         ")
   print ("         monster head. You missed.     ")
   print ("                  _______$___________$_______")
   print ("                  _____$$_____________$$_____")
   print ("                  ____$____$$$___$$$____$____")
   print ("                  ________$$$$$_$$$$$________")
   print ("                  ________$$$$$_$$$$$________")
   print ("                  ________$$$$$_$$$$$________")
   print ("                  _________$$$___$$$_________")
   print ("                  ___$__________________$____")
   print ("                  ____$________________$_____")
   print ("                  _____$$$$$$$$$$$$$$$$______")
   print ("                  ___________$$$$$$$_________")
   print ("                  ____________$$$$$$$________")
   print ("                  _____________$$$$$$________")
   print ("                  ______________$$$$_________")
   print ("             YOU DIED!             ")
   print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  
  print ("\nYou were hesitant, since the cave was dark and ")
  print  (      "ominous. Before you fully enter,"          )
  print  (     "you notice a shiny sword on "               )
  print(      "the ground. Do you pick up a sword. Y/N?"    )
  print  ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 #adds a sword
  else:
    sword = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print  ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (  "\nReally? You're going to hide in the dark? I think  ")
    print ( "moster can see very well in the dark, right? Not sure,")
    print (       "but,I'm going with YES, so...\n     ")
    print ("                  _______$___________$_______")
    print ("                  _____$$_____________$$_____")
    print ("                  ____$____$$$___$$$____$____")
    print ("                  ________$$$$$_$$$$$________")
    print ("                  ________$$$$$_$$$$$________")
    print ("                  ________$$$$$_$$$$$________")
    print ("                  _________$$$___$$$_________")
    print ("                  ___$__________________$____")
    print ("                  ____$________________$_____")
    print ("                  _____$$$$$$$$$$$$$$$$______")
    print ("                  ___________$$$$$$$_________")
    print ("                  ____________$$$$$$$________")
    print ("                  _____________$$$$$$________")
    print ("                  ______________$$$$_________")
    print("                 \nYOU DIED! ")
    print ( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  elif choice in answer_B:
   if sword > 0:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\nYou laid in wait. The shimmering sword attracted ")
    print("the monster, which thought you were no match. As he walked ")
    print("closer and closer, your heart beat rapidly. As the orc ")
    print("reached out to grab the sword, you pierced the blade into ")
    print(                          "its chest"                      )
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    global name
    global HP
    global MP
    global move
    global enemyHP

    while HP > 0:
#This loop will only work while our characters HP is greater than 0.
          hit = randint(0,5)
          print ("You swing your sword and cause " + str(hit) + " of damage")
          enemyHP = enemyHP - hit
          print (enemyHP)
          enemyhit = randint(0,5)
          print ("The moster swings a club at you and causes " + str(enemyhit) + " of damage")
          HP = HP - enemyhit
          print (HP)
          print("you win" ,name)
   else: #If the user didn't grab the sword
     print ("\nYou should have picked up that sword. You're "
     "defenseless. \n\nYou died!")
  elif choice in answer_C:
    print ("As the monster enters the dark cave, you sliently "
    "sneak out. You're several feet away, but the orc turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\nYou run as quickly as possible, but the moster's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an moster. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("      \nWhile frantically running, you notice a rusted ")
  print("    sword lying in the mud. You quickly reach down and grab it, ")
  print("  but miss. You try to calm your heavy breathing as you hide ")
  print("   behind a delapitated building, waiting for the monster to come ")
  print("     charging around the corner. You notice a purple flower ")
  print("          near your foot. Do you pick it up? Y/N")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending moster.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the orc. It does! The moster was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")

     
def intro():
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print ("     After a drunken night out with friends,    ")
  print ("               you awaken the                   ")
  print ("        next morning in a thick, dank forest.   ")             
  print ("               Head spinning and                ")
  print ("          fighting the urge to vomit,           ")  
  print ("         you stand and marvel at your new,      ")
  print ("               unfamiliar land......            ")
  print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
clear_screen()
title()
castle()
setup()

print ("Welcome to the Adventure, " + name)
time.sleep(1)
intro()

#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour health is" + " " + str(HP))
print ("Your magic skill is" + " " + str(MP))

print ("Would you like to venture out into the land? Press y then enter to continue")
if input() == "y":
    print ("In the distance to the north you can see a small village, to the east you can see a river and to the west a field of wild flowers.")
print ("\n")
north()
east()
west()
move = input("Where would you like to go? ")
if move == 'n':
    print ("\nYou move to the north, walking in the sunshine.")
    print ("A villager is in your path and greets you")
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == 'e':
    print ("\nYou walk to the river which lies to the east of your home.")
    print ("A villager is in your path and greets you")
elif move == 'w':
    print ("\nYou walk to the field of wild flowers, stopping to take in the beauty")
    print ("A villager is in your path and greets you\n")
villager()
enemy()
