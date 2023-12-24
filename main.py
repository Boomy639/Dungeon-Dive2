import random
import time

print(">> Disclaimer!!! \n \n>> This is an 'iron man' RPG, meaning you have one run, no saves \n>> This is not because im too lazy to make a save game system \n")

# Main Menu Section
print(f"\n>> TEXT BASED RPG")
main_menu = input(f">> Start \n>> Quit\n \n").lower()
if main_menu == "start":
    print(f"\n>> Your Game Will Now Start!")
else:
    quit()

# After main menu >>
print("\n >>> Loading...." * 3)
time.sleep(3) # wait 3 seconds!
print(f"\n >>> Finished Loading")

