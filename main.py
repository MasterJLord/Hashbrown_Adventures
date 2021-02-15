from random import *
from time import sleep
import sys

def typewriter(line, delay = .35, irregular = "qwertyuiopasdfghjklzxcvbnm"):
    line_1 = str(line)
    if irregular != "qwertyuiopasdfghjklzxcvbnm":
        wait = delay/10
        for x in line_1:
            print(x, end='')
            sys.stdout.flush()
            sleep(wait)
        sleep(wait*3)
    else:
        wait = delay/5
        for x in line_1:
            print(x, end='')
            sys.stdout.flush()
            sleep(uniform(0, wait))
        sleep(uniform(0, wait*3))
    print("")
    
    


inventory = []
do = 0
ddo = 0
gameOver = 0
room = []
hintcodes = ["""You are being trained. Please do not resist. This is not a tutorial- nevermind, it is. to begin the actual game, play the game. If you are having trouble with commands, here are a few hints: 
Commands are space-sensitive.
The list of objects contains both the objects in the room around you and the objects in your inventory that may be usable.
Do not enter targets of actions on the same line as actions. For example, do not play the game- instead, 
play
the game.""", "There's only one way out of this room, and that's through the window. You'll need something to break it with.", "This hint is less direct than the others: there used to be an enchant action, but it has now been combined with use.", "What happens in this room depends mostly in what you did in previous rooms.", "White is sometimes more powerful than red, but in this case the other is more useful.", "As you look closer at the screens, you notice what seems to be a diagram of a giant golden orb. Where would you expect a giant golden orb..."]
abilities = []
magic = []
enchantments = ["white", "blue", "black", "red", "green"]
endings = []
objects = {}


def hint():
    if "5" in room:
        typewriter(hintcodes[5])
    elif "4" in room:
        typewriter(hintcodes[4])
    elif "3" in room:
        typewriter(hintcodes[3])
    elif "2" in room:
        typewriter(hintcodes[2])
    elif "1" in room:
        typewriter(hintcodes[1])
    else:
        typewriter(hintcodes[0])

def lose(item):
    for i in range(len(inventory)):
        if inventory[i-1] == item:
            inventory.pop(i-1)
            break

def pickup():
    typewriter("What would you like to pick up?")
    do = input()
    if do in objects:
        abilities = objects[do]
        if "pickup" in abilities:
            abilities["pickup"]()
        else:
            typewriter("Sorry, that is not a valid target.")
    else:
        typewriter("Sorry, that is not a valid target.")
        
def throw():
    typewriter("What would you like to throw?")
    do = input()
    if do in inventory:
        if "throw" in objects[do]:
            objects[do]["throw"]()
        else:
            typewriter("Sorry, that is not a valid target.")
    else:
        typewriter("Sorry, that is not a valid target.")
            
def crawl():
    typewriter("What would you like to crawl through?")
    do = input()
    if do in objects:
        abilities = objects[do]
        if "crawl" in abilities:
            typewriter("crawling")
            abilities["crawl"]()
        else:
            typewriter("Sorry, that is not a valid target.")
    else:
        typewriter("Sorry, that is not a valid target.")
        
def getGold():
    typewriter("You pick up the gold- it is large enough to be heavy.")
    inventory.append("gold")
                
def pickupRock():
    inventory.append("rock")
    typewriter("You pick up a rock.")
    if "secret" in inventory and len(inventory) > 3:
        typewriter("You find a giant sphere made of gold just a few rocks down. Who could ever have expected that?")
        objects.update({"gold":{"pickup":getGold}})

def throwRock():
    typewriter("What would you like to throw the rock at?")
    do = input()
    if do in objects:
        abilities=objects[do]
        if "target" in abilities:
            lose("rock")
            abilities["target"]()
        else:
            typewriter("Sorry, that is not a valid target.")
    else:
        typewriter("Sorry, that is not a valid target.")
    
def regretish():
    typewriter("The window is broken.")
    
def breakWindow():
    objects["broken window"] = {"crawl":room2, "look":regretish}
    objects.pop("window")
    typewriter("You break the window")
        
def typewriterObjects():
    ddo = str(objects.keys())
    inside = 0
    do = ""
    for i in range(len(ddo)):
        if ddo[i-1] == " ":
            do = do + " "
        if ddo[i-1] == ",":
            do = do + ","
        if ddo[i-1] == "'" and inside == 1:
            inside = 2
        if inside == 1:
            do = do + ddo[i-1]
        if ddo[i-1] == "'" and inside == 0:
            inside = 1
        if inside == 2:
            inside = 0
    typewriter(do)
        
def typewriterActions():
    ddo = str(actions.keys())
    inside = 0
    do = ""
    for i in range(len(ddo)):
        if ddo[i-1] == " ":
            do = do + " "
        if ddo[i-1] == ",":
            do = do + ","
        if ddo[i-1] == "'" and inside == 1:
            inside = 2
        if inside == 1:
            do = do + ddo[i-1]
        if ddo[i-1] == "'" and inside == 0:
            inside = 1
        if inside == 2:
            inside = 0
    typewriter(do)
    
def hashbrown():
    typewriter("Would you like to list objects or actions?")
    do = input()
    if do in lists:
        lists[do]["list"]()
    else:
        typewriter("Sorry, that is not a valid target.")
    return []
        
def use():
    typewriter("What would you like to use?")
    do = input()
    if do in inventory:
        if do in objects:
            if "enchant" in objects[do]:
                objects[do]["enchant"]()
            else:
                typewriter("sorry, that is not a valid target.")
        else:
            typewriter("sorry, that is not a valid target")
    else:
        typewriter("You don't have that item.")

def look():
    typewriter("What would you like to look at?")
    do = input()
    if do in objects:
        if "look" in objects[do]:
            objects[do]["look"]()
        else:
            typewriter("You try to look at that but it is so unbelievably boring that you manage to fail.")
    else:
        typewriter("sorry, that is not a valid target.")
    return []
        
def shrineColors():
    typewriter("The shrine is a small pedestal surrounded by 5 orbs of various colors. The colors are white, the color of protection and loyalty, blue, the color of knowledge and magic, black, the color of power and greed, red, the color of fire and accuracy, and green, the color of growth and strength.")
    
def regainRock():
    inventory.append("rock")
    objects["rock"].pop("pickup")

def enchantRock():
    typewriter("Where would you like to use the rock?")
    do = input()
    if do in objects:
        if "pray" in objects[do]:
            objects[do]["pray"]()
        else:
            typewriter("sorry, that is not a valid target")
    else:
        typewriter("Sorry, that is not a valid target.")
    
def shrinenchant():
    if len(magic) < 2:
        typewriter('As you approach the shrine and begin to pray for the rock to be enchanted, a voice floats through your mind: "What 2 colors would you like to choose?"')
        do = input()
        if do in enchantments:
            typewriter("As you touch the "+do+" orb, the rock glows "+do+" and then fades back to normal.")
            magic.append(do)
        else:
            typewriter("Sorry, that is not a valid color.")
    else:
        typewriter("Your rock is already fully enchanted.")
    if len(magic) < 2:
        typewriter("You may still choose another color.")
    elif len(magic) == 2:
        typewriter("The idol dulls slightly.")

def win():
    typewriter("an outer layer of the golden orb strips off, and reveals a glowing white orb inside, pulsating with power. The flashing lights on the consoles switch off, and you feel movement away from the structure you were in before- and hopefully, towards home.")
    inventory.append("gameOver")

def move():
    typewriter("where would you like to go?")
    do = input()
    if do in objects:
        if "go" in objects[do]:
            objects[do]["go"]()
        else:
            typewriter("Sorry, that is not a valid target.")
    else:
        typewriter("Sorry, that is not a valid target.")
        
def risk():
    if "white" in magic:
        typewriter("It gets hotter closer to the orb, but your shield is enough to protect you.")
        room4()
    else:
        typewriter("As you approach the orb, the heat grows warmer and warmer, until you can't bear it anymore.")
        die()
        
def youcant():
    typewriter('A voice floats through your head, saying "To enchant something, it must have played some role in your life, however slight."')
    
def foreshadow():
    typewriter("It is a pile of rocks. You know that, right? What were you expecting, a giant sphere made of gold just a few rocks down?")
    inventory.append("secret")
    
def activateship():
    typewriter("Where would you like to use the orb?")
    do = input()
    if do in objects:
        if "activate" in objects[do]:
            objects[do]["activate"]()
        else:
            typewriter("Sorry, that is not a valid target.")
    else:
        typewriter("Sorry, that is not a valid target.")
        
def whatdawhat():
    typewriter("You try to understand what is happening, but you have no idea. The only thing you can figure out is that the ship appear sto be missing some critical part.")
    
def windowsurf():
    typewriter("the window is a normal window. You look through it but all you can see is a section of a stone brick wall opposite you; you have no idea what else might be in the room.")
    
def play():
    typewriter("What would you like to play?")
    do = input()
    if do in objects:
        if "play" in objects[do]:
            ddo = objects[do]["play"]()
            return ddo
        else:
            typewriter("sorry, that is not a valid target")
    else:
        typewriter("Sorry, that is not a valid target")

def end():
    inventory.append("playtime")
    return(inventory)
    
def holook():
    typewriter("It is a hole in the base of the wall, about the same size as the window.") 
    
def hot():
    typewriter("the orb is visibly hot.") 
    
def aim():
    typewriter("the iron bar is a few feet tall and a few inches wide.")
    
def roboarms():
    typewriter("The pedestal has a hole in it that looks like it would fit a sphere about a foot in diameter.") 
    
def bars():
    typewriter("The bars are solid and close together. There is no apparent door, so you wonder how you even got there. You son't be getting out this way.")
    
def rebound():
    typewriter("you throw the rock between the bars; it bounces off the opposite wall but stays out of reach.")  
    
def intro():
    typewriter("It is the game you are currently playing.")
    
    
    
def room5():
    typewriter("You find yourself standing on the bridge of a spaceship. In the middle of the room is a pedestal, and all around are screens flashing red.")
    objects.clear()
    objects.update({"gold":{"enchant":activateship}, "pedestal":{"activate":win, "look":roboarms}, "computers":{"look":whatdawhat}})
    room.append("5")
    
def attemptoThrow():
    if "red" in magic:
        typewriter("Your stone glows red as you throw it and curves in the air to hit the rod. With nothing holding it up, the drawbridge comes crashing down.")
        objects.update({"drawbridge":{"go":room5}})
    else:
        typewriter("You throw the stone at the iron rod, but miss, and the rock bounce off of the wall to dissapear under the lava below.")
        
def room2():
    typewriter("You fall onto another stone floor, very different from the previous room you were in. In one corner is a shrine to an unknown diety, and in another is a hole close to the floor leading to somewhere out of sight. It is uncomfortably warm, but not warm enough to evaporate the water on the floor. The rock you threw before is in the middle of the room.")
    while "rock" in inventory:
        lose("rock")
        inventory.append("unused rock")
    room.append("2")
    objects.clear()
    objects.update({"shrine":{"look":shrineColors, "pray":shrinenchant}, "rock":{"pickup":regainRock, "enchant":enchantRock}, "hole":{"crawl":room3, "look":holook}, "unused rock":{"enchant":youcant}})
    
def room3():
    typewriter("You crawl through the hole, and find yourself falling. You land after a short time, miraculously unhurt. In front of you, there is a long hallway, and above you there is an unscalable wall upwards to where you came from.")
    if "red" in magic:
        if "white" in magic:
            typewriter("There is a spot in the center of the corridor glowing fiercely red. Your stone is glowing both red and white, shooting an almost entirely transparent cord of red light to the thing, but also projecting a shield of glowing white light around you. It feels very hot.")
        else:
            typewriter("Your stone glows red, and an incredible heat swells from a red orb in the middle of the room.")
            die()
    elif "white" in magic:
        typewriter("You feel heat emanating from a red orb in the middle of the room, but your stone glows white and propels a shield of white light to protect you.")
    else:
        typewriter("A glowing red orb in the middle of the hallway emits a sweltering heat.")
    objects.clear()
    objects.update({"forwards":{"go":risk}, "orb":{"look":hot}})
    room.append("3")
    
def room4():
    typewriter("You are in a larger room with a lava moat in the middle. On the opposite side is a drawbridge, held up by a supporting iron rod being squeezed between the wood and an outcropping of stone.")
    objects.clear()
    objects.update({"rock":{"throw":throwRock}, "support":{"target":attemptoThrow, "look":aim}})
    room.append("4")
    
def playgame():
    secret = 0
    room.append("1")
    inventory = []
    objects.clear()
    objects.update({"rock":{"pickup":pickupRock, "throw":throwRock, "look":foreshadow}, "window": {"target":breakWindow, "look":windowsurf}, "bars":{"look":bars, "target":rebound}})
    typewriter("You wake up in a small jail cell with no memories of how you arrived. In one corner is a pile of stones, an another is a hole in the wall, and in another is a window.")
    while not("gameOver" in inventory):
        typewriter(questions[randint(1,3)-1])
        do = input()
        if do == "quit":
            break
        elif do == "cheat":
            room2()
#        elif do == "hint":
#            typewriter(hintcodes[room])
        elif do in actions:
            actions[do]()
        else:
            typewriter("Sorry, that's not a valid action.")

def die():
    typewriter("You have died. Would you like to play again? (y/n)")
    do = input()
    if do == "y":
        playgame()
    else:
        typewriter("Then this time, you die for good.")
        inventory.append(gameOver)
    
        
def restart():
    playgame()
    
    
    
lists = {
    "objects":{"list": typewriterObjects},
    "actions":{"list": typewriterActions}
}

questions = ["What would you like to do?", "Please choose an action.", "Do something!"]

actions = {
    "play":play,
    "list":hashbrown,
    "look":look,
    "hint":0
}        
        
def startup():
    typewriter("Welcome to the tutorial!")
    typewriter('.')
    objects.clear()
    objects.update({"game":{"play":end, "look":intro}})
    inventory = []
    while not "playtime" in inventory:
        typewriter(questions[randint(1,3)-1])
        do = input()
        if do == "quit":
            break
        elif do == "hint":
            typewriter(hintcodes[0])
        elif do in actions:
            inventory = (actions[do]())
        else:
            typewriter("sorry, that is not a valid action.")
    return do
    

    
do = startup()

actions = {
    "pick up":pickup,
    "throw":throw,
    "crawl":crawl,
    "list":hashbrown,
    "use":use,
    "look":look,
    "move":move,
    "restart":restart,
    "hint":hint,
    "quit":0
}


if not do == "quit":
    playgame()
