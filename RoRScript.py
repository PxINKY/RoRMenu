import os
import xml.etree.ElementTree as ET
#   _____       _____ _   _ _  ____     __
#  |  __ \     |_   _| \ | | |/ /\ \   / /
#  | |__) |_  __ | | |  \| | ' /  \ \_/ /
#  |  ___/\ \/ / | | | . ` |  <    \   /
#  | |     >  < _| |_| |\  | . \    | |
#  |_|    /_/\_\_____|_| \_|_|\_\   |_|



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  ____   ____ _____ __  _       ___   _____      ____    ____  ____  ____         ___  ___    ____  ______   ___   ____    #
# |    \ |    / ___/|  |/ ]     /   \ |     |    |    \  /    ||    ||    \       /  _]|   \  |    ||      | /   \ |    \   #
# |  D  ) |  (   \_ |  ' /     |     ||   __|    |  D  )|  o  | |  | |  _  |     /  [_ |    \  |  | |      ||     ||  D  )  #
# |    /  |  |\__  ||    \     |  O  ||  |_      |    / |     | |  | |  |  |    |    _]|  D  | |  | |_|  |_||  O  ||    /   #
# |    \  |  |/  \ ||     \    |     ||   _]     |    \ |  _  | |  | |  |  |    |   [_ |     | |  |   |  |  |     ||    \   #
# |  .  \ |  |\    ||  .  |    |     ||  |       |  .  \|  |  | |  | |  |  |    |     ||     | |  |   |  |  |     ||  .  \  #
# |__|\_||____|\___||__|\_|     \___/ |__|       |__|\_||__|__||____||__|__|    |_____||_____||____|  |__|   \___/ |__|\_|  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# File directory set up (automatic unless steam is moved)
try:
    dir = "C:\\Program Files (x86)\\Steam\\userdata\\244091727\\632360\\remote\\UserProfiles"
except:
    dir = input("Enter the path to the directory containing the user profiles: ")

# variables getting defined
playerfile = ""
players = []

for file in os.listdir(dir):
    if file.endswith(".xml"):
        players.append(file)
print("Please select a save in: ")
for x in players:
    tree = ET.parse(dir + "\\" + x)
    root = tree.getroot()
    print(f'{players.index(x)} - {x} - {root.find("name").text}')

playerfile = players[int(input("# here: "))]
tree = ET.parse(dir + "\\" + playerfile)
root = tree.getroot()
# options
print(f"1 - Coin editor\n2 - Item unlocker\n3 - Name editor")
num = int(input("Enter number choice: "))
# ---------------------------------------------------------------------------
# ---------------------------------- COINS ----------------------------------
# ---------------------------------------------------------------------------
if num == 1:
    if root.find("coins") is not None:
        coins = input("Please enter amount of coins to change to: ")
        root.find("coins").text = str(coins)
        tree.write(dir + "\\" + playerfile)
        print("Added coins to " + playerfile)
    else:
        print("No coins tag found in " + playerfile)
# ---------------------------------------------------------------------------
# ---------------------------------- ITEMS ---------------------------------- > WIP
# ---------------------------------------------------------------------------
elif num == 2:
    for n in root.find("stats"):
        if n.tag == "unlock":
            print(n.tag + ": " + n.text)
    unlock = input("Please enter item to unlock: ")
    # go into stats tree and add unlock item
    for n in root.find("stats"):
        if n.tag == "unlock":
            n.text = unlock
    tree.write(dir + "\\" + playerfile)
    print("Unlocked " + unlock + " in " + playerfile)
# ---------------------------------------------------------------------------
# ---------------------------------- NAMES ----------------------------------
# ---------------------------------------------------------------------------
elif num == 3:
    oldname = root.find("name").text
    name = input("Please enter new name: ")
    root.find("name").text = name
    tree.write(dir + "\\" + playerfile)
    print("Changed " + oldname + " to " + name + " in " + playerfile)
else:
    print("Invalid choice")
