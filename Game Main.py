# Text based GUI adventure game medieval themed with images and choices using frames, buttons
import tkinter

root = tkinter.Tk()
root.title("Arrow to The Knee")

#images #
warriorimg = tkinter.PhotoImage(file="warrior.png")
mageimg = tkinter.PhotoImage(file="mage.png")
archerimg = tkinter.PhotoImage(file="archer.png")
blacksmithimg = tkinter.PhotoImage(file="Blacksmith.png")
deathimg = tkinter.PhotoImage(file="Death.png")
deerimg = tkinter.PhotoImage(file="hunted deer.png")
jailimg = tkinter.PhotoImage(file="jailed.png")
ruinsimg = tkinter.PhotoImage(file="ruins.png")
goldimg = tkinter.PhotoImage(file="Gold Victory.png")
townimg = tkinter.PhotoImage(file="Medieval town.png")

homePage = tkinter.Frame(root, bg="black", height=300, width=300)
homePage.grid_propagate(False) 
homePage.grid(row=0, column=0, sticky="nsew")

pageOne = tkinter.Frame(root, bg="green")
pageOne.grid(row=0, column=0, sticky="nsew")

pageTwo = tkinter.Frame(root, bg="maroon")
pageTwo.grid(row=0, column=0, sticky="nsew")

# MAGE PATH #
pageThree = tkinter.Frame(root, bg= "blue")
pageThree.grid(row=0, column=0, sticky="nsew")

mageimgbutton = tkinter.Button(pageThree, image=mageimg)
mageimgbutton.grid(row=4, column=0)

# Mage A vvv
pageMageA = tkinter.Frame(root, bg= "blue")
pageMageA.grid(row=0, column=0, sticky="nsew")

deerimgbuttonmagea1 = tkinter.Button(pageMageA, image=deerimg)
deerimgbuttonmagea1.grid(row=4, column=0, sticky="nsew")

pageMageA1 = tkinter.Frame(root, bg= "blue")
pageMageA1.grid(row=0, column=0, sticky="nsew")

deathimgbuttonmagea1 = tkinter.Button(pageMageA1, image=deathimg)
deathimgbuttonmagea1.grid(row=4, column=0, sticky="nsew")

pageMageA2 = tkinter.Frame(root, bg= "blue")
pageMageA2.grid(row=0, column=0, sticky="nsew")

deathimgbuttonmagea2 = tkinter.Button(pageMageA2, image=deathimg)
deathimgbuttonmagea2.grid(row=4, column=0, sticky="nsew")

pageMageA3 = tkinter.Frame(root, bg= "blue")
pageMageA3.grid(row=0, column=0, sticky="nsew")

townimgbuttonmagea3 = tkinter.Button(pageMageA3, image=townimg)
townimgbuttonmagea3.grid(row=4, column=0, sticky="nsew")

pageMageA3a = tkinter.Frame(root, bg= "blue")
pageMageA3a.grid(row=0, column=0, sticky="nsew")

deathimgbuttonmagea3a = tkinter.Button(pageMageA3a, image=deathimg)
deathimgbuttonmagea3a.grid(row=4, column=0, sticky="nsew")

pageMageA3b = tkinter.Frame(root, bg= "blue")
pageMageA3b.grid(row=0, column=0, sticky="nsew")

goldimgbuttonmagea3b = tkinter.Button(pageMageA3b, image=goldimg)
goldimgbuttonmagea3b.grid(row=4, column=0, sticky="nsew")

pageMageA3bd = tkinter.Frame(root, bg= "blue")
pageMageA3bd.grid(row=0, column=0, sticky="nsew")

pageMageA3c = tkinter.Frame(root, bg= "blue")
pageMageA3c.grid(row=0, column=0, sticky="nsew")

blacksmithimgbuttonmagea3c = tkinter.Button(pageMageA3c, image=blacksmithimg)
blacksmithimgbuttonmagea3c.grid(row=5, column=0, sticky="nsew")

pageMageA3cd = tkinter.Frame(root, bg= "blue")
pageMageA3cd.grid(row=0, column=0, sticky="nsew")

goldimgbuttonmagea3cd = tkinter.Button(pageMageA3cd, image=goldimg)
goldimgbuttonmagea3cd.grid(row=5, column=0, sticky="nsew")


# Mage A ^^^

# Mage B vvv
pageMageB = tkinter.Frame(root, bg= "blue")
pageMageB.grid(row=0, column=0, sticky="nsew")

townimgbuttonmageb = tkinter.Button(pageMageB, image=townimg)
townimgbuttonmageb.grid(row=0, column=0, sticky="nsew")

pageMageB1 = tkinter.Frame(root, bg= "blue")
pageMageB1.grid(row=0, column=0, sticky="nsew")

jailimgbuttonmageb1 = tkinter.Button(pageMageB1, image=jailimg)
jailimgbuttonmageb1.grid(row=4, column=0, sticky="nsew")

pageMageB2 = tkinter.Frame(root, bg= "blue")
pageMageB2.grid(row=0, column=0, sticky="nsew")

jailimgbuttonmageb2 = tkinter.Button(pageMageB2, image=jailimg)
jailimgbuttonmageb2.grid(row=4, column=0, sticky="nsew")

pageMageB3 = tkinter.Frame(root, bg= "blue")
pageMageB3.grid(row=0, column=0, sticky="nsew")

blacksmithimgbuttonmageb3 = tkinter.Button(pageMageB3, image=blacksmithimg)
blacksmithimgbuttonmageb3.grid(row=6, column=0, sticky="nsew")

pageMageB3a = tkinter.Frame(root, bg= "blue")
pageMageB3a.grid(row=0, column=0, sticky="nsew")

pageMageB3aY = tkinter.Frame(root, bg= "blue")
pageMageB3aY.grid(row=0, column=0, sticky="nsew")

ruinsimagebuttonmageb3ay = tkinter.Button(pageMageB3aY, image=ruinsimg)
ruinsimagebuttonmageb3ay.grid(row=4, column=0, sticky="nsew")

pageMageB3aY1 = tkinter.Frame(root, bg= "blue")
pageMageB3aY1.grid(row=0, column=0, sticky="nsew")

goldimgbuttonmageb3ay1 = tkinter.Button(pageMageB3aY1, image=goldimg)
goldimgbuttonmageb3ay1.grid(row=6, column=0, sticky="nsew")

pageMageB3aY1d = tkinter.Frame(root, bg= "blue")
pageMageB3aY1d.grid(row=0, column=0, sticky="nsew")

pageMageB3aY2 = tkinter.Frame(root, bg= "blue")
pageMageB3aY2.grid(row=0, column=0, sticky="nsew")

blacksmithimgbuttonmageb3ay2 = tkinter.Button(pageMageB3aY2, image=blacksmithimg)
blacksmithimgbuttonmageb3ay2.grid(row=6, column=0, sticky="nsew")

pageMageB3aY2d = tkinter.Frame(root, bg= "blue")
pageMageB3aY2d.grid(row=0, column=0, sticky="nsew")


pageMageB3b = tkinter.Frame(root, bg= "blue")
pageMageB3b.grid(row=0, column=0, sticky="nsew")

# Mage B ^^^

# Mage C vvv
pageMageC = tkinter.Frame(root, bg= "blue")
pageMageC.grid(row=0, column=0, sticky="nsew")

ruinsimagebuttonmagec = tkinter.Button(pageMageC, image=ruinsimg)
ruinsimagebuttonmagec.grid(row=4, column=0, sticky="nsew")

pageMageC1 = tkinter.Frame(root, bg= "blue")
pageMageC1.grid(row=0, column=0, sticky="nsew")

deathimgbuttonmagec1 = tkinter.Button(pageMageC1, image=deathimg)
deathimgbuttonmagec1.grid(row=4, column=0, sticky="nsew")

pageMageC2 = tkinter.Frame(root, bg= "blue")
pageMageC2.grid(row=0, column=0, sticky="nsew")

deathimgbuttonmagec2 = tkinter.Button(pageMageC2, image=deathimg)
deathimgbuttonmagec2.grid(row=4, column=0, sticky="nsew")

pageMageC3 = tkinter.Frame(root, bg= "blue")
pageMageC3.grid(row=0, column=0, sticky="nsew")

deathimgbuttonmagec3 = tkinter.Button(pageMageC3, image=deathimg)
deathimgbuttonmagec3.grid(row=4, column=0, sticky="nsew")
# MAGE C ^^^

# MAGE PATH #


# ARCHER PATH #
pageFour = tkinter.Frame(root, bg= "grey")
pageFour.grid(row=0, column=0, sticky="nsew")
# ARCHER PATH #

# WARRIOR PATH #
pageFive = tkinter.Frame(root, bg= "maroon")
pageFive.grid(row=0, column=0, sticky="nsew")
# WARRIOR PATH #

homePage.tkraise() 

def showHome():
    homePage.tkraise()

def showPageOne():
    pageOne.tkraise()

def showPageTwo():
    pageTwo.tkraise()

# MAGE PATH #  
def showPageThree():
    pageThree.tkraise()
    
# Mage A vvv
def showMageA():
    pageMageA.tkraise()

def showMageA1():
    pageMageA1.tkraise()

def showMageA2():
    pageMageA2.tkraise()

def showMageA3():
    pageMageA3.tkraise()
def showMageA3a():
    pageMageA3a.tkraise()
def showMageA3b():
    pageMageA3b.tkraise()
def showMageA3bd():
    pageMageA3bd.tkraise()     
def showMageA3c():
    pageMageA3c.tkraise()
def showMageA3cd():
    pageMageA3cd.tkraise()    

# Mage A ^^^

# Mage B vvv    
def showMageB():
    pageMageB.tkraise()

def showMageB1():
    pageMageB1.tkraise()
    
def showMageB2():
    pageMageB2.tkraise()

def showMageB3():
    pageMageB3.tkraise()

def showMageB3a():
    pageMageB3a.tkraise()
def showMageB3aY():
    pageMageB3aY.tkraise()
def showMageB3aY1():
    pageMageB3aY1.tkraise()
def showMageB3aY1d():
    pageMageB3aY1d.tkraise()    
def showMageB3aY2():
    pageMageB3aY2.tkraise()
def showMageB3aY2d():
    pageMageB3aY2d.tkraise()     
    
    
def showMageB3b():
    pageMageB3b.tkraise()
    
# Mage B ^^^

# Mage C vvv    
def showMageC():
    pageMageC.tkraise()

def showMageC1():
    pageMageC1.tkraise()
    
def showMageC2():
    pageMageC2.tkraise()

def showMageC3():
    pageMageC3.tkraise()
# Mage C ^^^    

    
    
# MAGE PATH #
    
#ARCHER PATH#
def showPageFour():
    pageFour.tkraise()
#ARCHER PATH#
    
#WARRIOR PATH#
def showPageFive():
    pageFive.tkraise()     
#WARRIOR PATH#
    
#EXIT SETTINGS#
goToTwo = tkinter.Button(homePage, text="EXIT", command=showPageTwo)
goToTwo.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageTwo, text="THANKS FOR PLAYING!")
label1.grid(row=0, column=0)

goHome = tkinter.Button(pageTwo, text="Go to Menu", fg="black", width=10, command=showHome)
goHome.grid(row=1, column=0)
#EXIT SETTINGS#


#GAME STARTS HERE#
goToOne = tkinter.Button(homePage, text="START", command=showPageOne)
goToOne.grid(row=0, column=0, sticky="nsew")

label1 = tkinter.Label(pageOne, text="PICK YOUR CLASS!")
label1.grid(row=0, column=0)


# # # MAGE PATH # # #
goToThree = tkinter.Button(pageOne, text="MAGE", fg="black", command=showPageThree)
goToThree.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageThree, text="You begin your day. The first thing you do...")
label1.grid(row=0, column=0)

# # PATH A vvv
goToMageA = tkinter.Button(pageThree, text="Go Hunting", fg="black", command=showMageA)
goToMageA.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA, text="You use your magic and hunt some deer in the woods")
label1.grid(row=0, column=0)

# PATH A 1
goToMageA1 = tkinter.Button(pageMageA, text="Cook and eat the deer meat", fg="black", command=showMageA1)
goToMageA1.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA1, text="You eat the deer meat and feel nourished.")
label1.grid(row=0, column=0)
label2 = tkinter.Label(pageMageA1, text="But suddendly you realized the meat was bad and get poised from it.")
label2.grid(row=1, column=0)
label3 = tkinter.Label(pageMageA1, text="No one is around to help, you die.")
label3.grid(row=2, column=0)

goToTwo = tkinter.Button(pageMageA1, text="EXIT GAME", command=showPageTwo)
goToTwo.grid(row=3, column=0, sticky="nsew")
# PATH A 1

# PATH A 2
goToMageA2 = tkinter.Button(pageMageA, text="Take dear meat to town and sell it", fg="black", command=showMageA2)
goToMageA2.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA2, text="You take the dear meat to sell at the closest town.")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageA2, text="A bear picks up your scent and catches you by suprise!")
label1.grid(row=1, column=0)
label1 = tkinter.Label(pageMageA2, text="Not prepared to fight you die.")
label1.grid(row=2, column=0)

goToTwo = tkinter.Button(pageMageA2, text="EXIT GAME", command=showPageTwo)
goToTwo.grid(row=3, column=0, sticky="nsew")
# PATH A 2

# PATH A 3
goToMageA3 = tkinter.Button(pageMageA, text="Skin the deer, take the hide and sell it at the town", fg="black", command=showMageA3)
goToMageA3.grid(row=3, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA3, text="Currently at the town.")
label1.grid(row=0, column=0)

# PATH A 3 1
goToMageA3 = tkinter.Button(pageMageA3, text="Browse the shops", fg="black", command=showMageA3a)
goToMageA3.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA3a, text="You visit the shops and see a theif. He runs past you.")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageA3a, text="The shopkeeperss mistake you for the theif and take you to jail")
label1.grid(row=1, column=0)

goToTwo = tkinter.Button(pageMageA3a, text="EXIT GAME", command=showPageTwo)
goToTwo.grid(row=2, column=0, sticky="nsew")
# PATH A 3 1

# PATH A 3 2
goToMageA3 = tkinter.Button(pageMageA3, text="Sell hide and go home with money", fg="black", command=showMageA3b)
goToMageA3.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA3b, text="You take the hide and sell it. It turns out to be from a rare deer!")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageA3b, text="You are surprisingly offered a ton of gold!")
label1.grid(row=1, column=0)

goToTwo = tkinter.Button(pageMageA3b, text="YOU GO HOME", command=showMageA3bd)
goToTwo.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA3bd, text="Congratulations you completed your quest")
label1.grid(row=0, column=0)

goToTwo = tkinter.Button(pageMageA3bd, text="EXIT", command=showPageTwo)
goToTwo.grid(row=1, column=0, sticky="nsew")
# PATH A 3 2

# PATH A 3 3
goToMageA3 = tkinter.Button(pageMageA3, text="Sell hide and go to ruins", fg="black", command=showMageA3c)
goToMageA3.grid(row=3, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA3c, text="You take the hide and sell it. It turns out to be from a rare deer!")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageA3c, text="You are surprisingly offered a ton of gold!")
label1.grid(row=1, column=0)
label1 = tkinter.Label(pageMageA3c, text="With all this you buy top notch weapons, armor and potions")
label1.grid(row=2, column=0)
label1 = tkinter.Label(pageMageA3c, text="Maybe it would be a good time to check out those ancient ruins")
label1.grid(row=3, column=0)

goToMageA3 = tkinter.Button(pageMageA3c, text="Head to ruins", fg="black", command=showMageA3cd)
goToMageA3.grid(row=4, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA3cd, text="You head to the ruin fully geared up. You head inside fully geared up and protected.")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageA3cd, text="Your armor protects you from any traps.You are attacked by a theif but easily take him down")
label1.grid(row=1, column=0)
label1 = tkinter.Label(pageMageA3cd, text="You continue to fight the undead and creature until you reach the depths of the ruins.")
label1.grid(row=2, column=0)
label1 = tkinter.Label(pageMageA3cd, text="Surrounded by treasure and loot. Making you rich beyond your wildest dreams!")
label1.grid(row=3, column=0)

goToTwo = tkinter.Button(pageMageA3cd, text="You leave the ruins", command=showMageB3aY1d)
goToTwo.grid(row=4, column=0, sticky="nsew")
 
label1 = tkinter.Label(pageMageB3aY1d, text="Congratulations you completed your quest!")
label1.grid(row=0, column=0)

goToTwo = tkinter.Button(pageMageB3aY1d, text="EXIT", command=showPageTwo)
goToTwo.grid(row=1, column=0, sticky="nsew")
# PATH A 3 3
# PATH A 3

# # PATH A ^^^

# # Path B vvv
goToMageB = tkinter.Button(pageThree, text="Go Into Town", fg="black", command=showMageB)
goToMageB.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB, text="You make a trip to town where you are surrounded by shops, restaurants, black smiths, etc.")
label1.grid(row=0, column=0)

# PATH B 1
goToMageB1 = tkinter.Button(pageMageB, text="Visit the shops", fg="black", command=showMageB1)
goToMageB1.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB1, text="You visit the shops and see a theif. He runs past you.")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageB1, text="The shopkeeperss mistake you for the theif and take you to jail")
label1.grid(row=1, column=0)

goToTwo = tkinter.Button(pageMageB1, text="EXIT GAME", command=showPageTwo)
goToTwo.grid(row=3, column=0, sticky="nsew")
# PATH B1

# PATH B2
goToMageB2 = tkinter.Button(pageMageB, text="Go to a fancy resturant", fg="black", command=showMageB2)
goToMageB2.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB2, text="You enjoy some of the finest meats and catering!")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageB2, text="Enjoying yourself to much you realize you did't have any gold on you.")
label1.grid(row=1, column=0)
label1 = tkinter.Label(pageMageB2, text="The chef takes great offence and has you arrested and taken to jail.")
label1.grid(row=2, column=0)

goToTwo = tkinter.Button(pageMageB2, text="EXIT GAME", command=showPageTwo)
goToTwo.grid(row=3, column=0, sticky="nsew")
# PATH B2

# PATH B 3
goToMageB3 = tkinter.Button(pageMageB, text="Visit the blacksmith", fg="black", command=showMageB3)
goToMageB3.grid(row=3, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB3, text="You visit the blacksmith and see he is having an argument with his wife.")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageB3, text="Listening you hear that someone has stolen their gold and materials.")
label1.grid(row=1, column=0)
label1 = tkinter.Label(pageMageB3, text="He sees you at the shop and asks if you can retrive his stole goods.")
label1.grid(row=2, column=0)

# PATH B 3 YES
goToMageB3 = tkinter.Button(pageMageB3, text="YES", fg="black", command=showMageB3a)
goToMageB3.grid(row=3, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB3a, text="The blacksmith offers you a reward and loans you a powerful weapon")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageB3a, text="You head to where the theif ran off to. The ruins")
label1.grid(row=1, column=0)

goToMageB3 = tkinter.Button(pageMageB3a, text="Leave black smith. To ruins", fg="black", command=showMageB3aY)
goToMageB3.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB3aY, text="What will you do?")
label1.grid(row=0, column=0)

goToMageB3 = tkinter.Button(pageMageB3aY, text="Do your own looting and goals", fg="black", command=showMageB3aY1)
goToMageB3.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB3aY1, text="You head to the ruin fully geared up. You head inside fully geared up and protected.")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageB3aY1, text="Your armor protects you from any traps.You are attacked by a theif but easily take him down")
label1.grid(row=1, column=0)
label1 = tkinter.Label(pageMageB3aY1, text="You continue to fight the undead and creature until you reach the depths of the ruins.")
label1.grid(row=2, column=0)
label1 = tkinter.Label(pageMageB3aY1, text="Surrounded by treasure and loot. Making you rich beyond your wildest dreams!")
label1.grid(row=3, column=0)

goToTwo = tkinter.Button(pageMageB3aY1, text="You leave the ruins", command=showMageB3aY1d)
goToTwo.grid(row=4, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB3aY1d, text="Congratulations you completed your quest!")
label1.grid(row=0, column=0)

goToTwo = tkinter.Button(pageMageB3aY1d, text="EXIT", command=showPageTwo)
goToTwo.grid(row=1, column=0, sticky="nsew")


goToMageB3 = tkinter.Button(pageMageB3aY, text="Follow your mission and carry out the blacksmiths deed", fg="black", command=showMageB3aY2)
goToMageB3.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB3aY2, text="You head to the ruins with the job in mind. You see the theif almost going inside")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageB3aY2, text="You get the jump on him and kill him wiht your borrowed weapon.")
label1.grid(row=1, column=0)
label1 = tkinter.Label(pageMageB3aY2, text="You return to the blacksmith giving him is stolen valubles.")
label1.grid(row=2, column=0)
label1 = tkinter.Label(pageMageB3aY2, text="He then rewards you wiyh a hefty sum of gold and lets you keep his weapon.")
label1.grid(row=3, column=0)

goToTwo = tkinter.Button(pageMageB3aY2, text="You leave the black smith", command=showMageB3aY2d)
goToTwo.grid(row=4, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB3aY2d, text="Congratulations you completed your quest")
label1.grid(row=0, column=0)

goToTwo = tkinter.Button(pageMageB3aY2d, text="EXIT", command=showPageTwo)
goToTwo.grid(row=2, column=0, sticky="nsew")
# PATH B 3 YES

# PATH B 3 NO
goToMageB3 = tkinter.Button(pageMageB3, text="NO", fg="black", command=showMageB3b)
goToMageB3.grid(row=4, column=0, sticky="nsew")

goToTwo = tkinter.Button(pageMageB3b, text="You leave the black smith", command=showMageB)
goToTwo.grid(row=0, column=0, sticky="nsew")
# PATH B 3

# # Path B ^^^

# # Path C vvv
goToMageC = tkinter.Button(pageThree, text="Explore Ruiuns", fg="black", command=showMageC)
goToMageC.grid(row=3, column=0, sticky="nsew")


label1 = tkinter.Label(pageMageC, text="You go straight twards the local ancient ruins in search of rare loot")
label1.grid(row=0, column=0)

#PATH C 1
goToMageC1 = tkinter.Button(pageMageC, text="Walk into the ruins", fg="black", command=showMageC1)
goToMageC1.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageC1, text="You walk into the ruins without caution.")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageC1, text="Immediately you're met with a booby trap that kills you!")
label1.grid(row=1, column=0)

goToTwo = tkinter.Button(pageMageC1, text="EXIT GAME", command=showPageTwo)
goToTwo.grid(row=2, column=0, sticky="nsew")
# PATH C 1

# PATH C 2
goToMageC2 = tkinter.Button(pageMageC, text="You find a chest at the entrance and search it", fg="black", command=showMageC2)
goToMageC2.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageC2, text="You search the chest that is slightly open. But soon realize it's a coffin!")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageC2, text="An undead rises from the chest and kills you!")
label1.grid(row=1, column=0)

goToTwo = tkinter.Button(pageMageC2, text="EXIT GAME", command=showPageTwo)
goToTwo.grid(row=2, column=0, sticky="nsew")
# PATH C 2

# PATH C 3
goToMageC3 = tkinter.Button(pageMageC, text="You hear a noise and wait outisde to see what happens", fg="black", command=showMageC3)
goToMageC3.grid(row=3, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageC3, text="You wait outisde for a while expecting something to come out.")
label1.grid(row=0, column=0)
label1 = tkinter.Label(pageMageC3, text="Unaware of your surroundings a thief approaches you from behind")
label1.grid(row=1, column=0)
label1 = tkinter.Label(pageMageC3, text="He sneaks up on you and kills you for your loot!.")
label1.grid(row=2, column=0)

goToTwo = tkinter.Button(pageMageC3, text="EXIT GAME", command=showPageTwo)
goToTwo.grid(row=3, column=0, sticky="nsew")
# PATH C 3
# # Path C ^^^
# # # MAGE PATH # # #

# ARCHER PATH #  
goToThree = tkinter.Button(pageOne, text="ARCHER", fg="black", command=showPageThree)
goToThree.grid(row=2, column=0, sticky="nsew")
# ARCHER PATH #

# WARRIOR PATH #
goToThree = tkinter.Button(pageOne, text="Warrior", fg="black", command=showPageThree)
goToThree.grid(row=3, column=0, sticky="nsew")
# WARRIOR PATH #

root.mainloop()
