import os
import xml.etree.ElementTree as ET
try:
    dir = "C:\\Program Files (x86)\\Steam\\userdata\\244091727\\632360\\remote\\UserProfiles"
except:
    dir = input("Enter the path to the directory containing the user profiles: ")

playerfile = ""
# check directory for xml file
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

# read xml file
tree = ET.parse(dir + "\\" + playerfile)
root = tree.getroot()
print(f"1 - Coin editor\n2 - Item unlocker\n3 - Name editor")
num = int(input("Enter number choice: "))
# if "coins" tag exists, add coins
if num == 1:
    if root.find("coins") is not None:
        coins = input("Please enter amount of coins to change to: ")
        root.find("coins").text = str(coins)
        tree.write(dir + "\\" + playerfile)
        print("Added coins to " + playerfile)
    else:
        print("No coins tag found in " + playerfile)
# this choice allows the user to unlock items
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
# this choice allows the user to change the name of the player
elif num == 3:
    oldname = root.find("name").text
    name = input("Please enter new name: ")
    root.find("name").text = name
    tree.write(dir + "\\" + playerfile)
    print("Changed " + oldname + " to " + name + " in " + playerfile)
else:
    print("Invalid choice")