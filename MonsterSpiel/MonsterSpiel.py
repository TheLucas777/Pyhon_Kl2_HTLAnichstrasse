import random
import time
import sys
from art import *

def doorprint(cursed_door):
    if cursed_door ==  1:
        tprint("X < <", font="block", chr_ignore=True)
    elif cursed_door ==  2:
        tprint("< X <", font="block", chr_ignore=True)
    elif cursed_door ==  3:
        tprint("< < X", font="block", chr_ignore=True)

def clear():
    for i in range ( 100 ):
        print()

def typewriter(str):
  for letter in str:
    sys.stdout.write(letter)
    time.sleep(0.04)
  print()


typewriter( "Welcome to MonsterSpiel!" )
time.sleep(0.5)
typewriter( "You are in a room with three doors." )
time.sleep(0.5)
typewriter( "Behind one of the doors is a monster." )
time.sleep(0.5)
typewriter( "Behind the other two doors you get to the next level.")
time.sleep(1)

level = 1


while True:
    monsterdoor = random.randint(1,3)

    tprint("Level " + str(level),font="type_set",chr_ignore=True)
    tprint("1 2 3",font="block",chr_ignore=True)

    door = input("Which door do you choose? ")
    try:
        door = int(door)
    except ValueError:
        print("Please enter a number.")
        continue

    if(door > 3 or door < 1):
        print("Please enter a valid door number.")
        continue
    if door == monsterdoor:
        print("You have been eaten by the monster!")
        doorprint(monsterdoor)
        time.sleep(2)
        clear()
        tprint(f"Highcore {level}",font="univers",chr_ignore=True)
        break
    else:
        print("You have passed the stage!")
        doorprint(monsterdoor)
        time.sleep(2)
        level += 1
        clear()
