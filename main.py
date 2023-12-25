import random
import time

print(">> Disclaimer!!! \n \n>> This is an 'iron man' RPG, meaning you have one run, no saves \n>> This is not because im too lazy to make a save game system \n")

# Main Menu Section
print(f"\n>> TEXT BASED RPG")
main_menu = input(f">> Start \n>> Quit\n \n>> ").lower()
if main_menu == "start":
    print(f"\n>> Your Game Will Now Start!")
else:
    quit()

# After main menu >>
print("\n >>> Loading...." * 3)
time.sleep(3) # wait 3 seconds!
print(f"\n >>> Finished Loading")

print(">> You awake in a dungeon... You aren't sure just how you got here, but you know you're here")

name = input(">> Now..... what is your name hero? ")
print(">> Welcome...", name)

print(">> Just to make you aware, incase you didnt read the disclaimer..")
print(f"\n>> This is an IRONMAN game, no saves")

ironman = input(">> Are you ok with this? ").lower()
if ironman == "yes":
    print(">> Good luck on your journey, hero...")
else:
    quit()