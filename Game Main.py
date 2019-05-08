# Text based GUI adventure game Elder Scrolls themed with images and choices using frames, buttons, RNG?.

import tkinter

root = tkinter.Tk()

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

# Mage A vvv
pageMageA = tkinter.Frame(root, bg= "blue")
pageMageA.grid(row=0, column=0, sticky="nsew")

pageMageA1 = tkinter.Frame(root, bg= "blue")
pageMageA1.grid(row=0, column=0, sticky="nsew")

pageMageA2 = tkinter.Frame(root, bg= "blue")
pageMageA2.grid(row=0, column=0, sticky="nsew")

pageMageA3 = tkinter.Frame(root, bg= "blue")
pageMageA3.grid(row=0, column=0, sticky="nsew")
# Mage A ^^^

# Mage B vvv
pageMageB = tkinter.Frame(root, bg= "blue")
pageMageB.grid(row=0, column=0, sticky="nsew")

pageMageB1 = tkinter.Frame(root, bg= "blue")
pageMageB1.grid(row=0, column=0, sticky="nsew")

pageMageB2 = tkinter.Frame(root, bg= "blue")
pageMageB2.grid(row=0, column=0, sticky="nsew")

pageMageB3 = tkinter.Frame(root, bg= "blue")
pageMageB3.grid(row=0, column=0, sticky="nsew")

# Mage B ^^^

# Mage C vvv
pageMageC = tkinter.Frame(root, bg= "blue")
pageMageC.grid(row=0, column=0, sticky="nsew")

pageMageC1 = tkinter.Frame(root, bg= "blue")
pageMageC1.grid(row=0, column=0, sticky="nsew")

pageMageC2 = tkinter.Frame(root, bg= "blue")
pageMageC2.grid(row=0, column=0, sticky="nsew")

pageMageC3 = tkinter.Frame(root, bg= "blue")
pageMageC3.grid(row=0, column=0, sticky="nsew")
# MAGE C ^^^

# MAGE PATH #


# ARCHER PATH #
pageFour = tkinter.Frame(root, bg= "grey")
pageFour.grid(row=0, column=0, sticky="nsew")
# ARCHER PATH #

# WARRIOR PATH #
pageFive = tkinter.Frame(root, bg= "red")
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


# MAGE PATH #
goToThree = tkinter.Button(pageOne, text="MAGE", fg="black", command=showPageThree)
goToThree.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageThree, text="You begin your day. The first thing you do...")
label1.grid(row=0, column=0)

# PATH A vvv
goToMageA = tkinter.Button(pageThree, text="Go Hunting", fg="black", command=showMageA)
goToMageA.grid(row=1, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageA, text="You use your magic and hunt some deer in the woods")
label1.grid(row=0, column=0)

goToMageA1 = tkinter.Button(pageMageA, text="Cook and eat the deer meat", fg="black", command=showMageA1)
goToMageA1.grid(row=1, column=0, sticky="nsew")

goToMageA2 = tkinter.Button(pageMageA, text="Take dear meat to town and sell it", fg="black", command=showMageA2)
goToMageA2.grid(row=2, column=0, sticky="nsew")

goToMageA3 = tkinter.Button(pageMageA, text="Skin the deer, take the hide and sell it at the town", fg="black", command=showMageA3)
goToMageA3.grid(row=3, column=0, sticky="nsew")
# PATH A ^^^

# Path B vvv
goToMageB = tkinter.Button(pageThree, text="Go Into Town", fg="black", command=showMageB)
goToMageB.grid(row=2, column=0, sticky="nsew")

label1 = tkinter.Label(pageMageB, text="You make a trip to town where you are surrounded by shops, restaurants, black smiths, etc.")
label1.grid(row=0, column=0)

goToMageB1 = tkinter.Button(pageMageB, text="Visit the shops", fg="black", command=showMageB1)
goToMageB1.grid(row=1, column=0, sticky="nsew")

goToMageB2 = tkinter.Button(pageMageB, text="Go to a fancy resturant", fg="black", command=showMageB2)
goToMageB2.grid(row=2, column=0, sticky="nsew")

goToMageB3 = tkinter.Button(pageMageB, text="Visit the blacksmith", fg="black", command=showMageB3)
goToMageB3.grid(row=3, column=0, sticky="nsew")
# Path B ^^^

# Path C vvv
goToMageC = tkinter.Button(pageThree, text="Explore Ruiuns", fg="black", command=showMageC)
goToMageC.grid(row=3, column=0, sticky="nsew")


label1 = tkinter.Label(pageMageC, text="You go straight twards the local ancient ruins in search of rare loot")
label1.grid(row=0, column=0)

goToMageC1 = tkinter.Button(pageMageC, text="Walk into the ruins", fg="black", command=showMageC1)
goToMageC1.grid(row=1, column=0, sticky="nsew")

goToMageC2 = tkinter.Button(pageMageC, text="You find a chest at the entrance and search it", fg="black", command=showMageC2)
goToMageC2.grid(row=2, column=0, sticky="nsew")

goToMageC3 = tkinter.Button(pageMageC, text="You hear a noise and wait outisde to see what happens", fg="black", command=showMageC3)
goToMageC3.grid(row=3, column=0, sticky="nsew")
# Path C ^^^

# MAGE PATH #

# ARCHER PATH #  
goToThree = tkinter.Button(pageOne, text="ARCHER", fg="black", command=showPageFour)
goToThree.grid(row=2, column=0, sticky="nsew")
# ARCHER PATH #

# WARRIOR PATH #
goToThree = tkinter.Button(pageOne, text="Warrior", fg="black", command=showPageFive)
goToThree.grid(row=3, column=0, sticky="nsew")
# WARRIOR PATH #

root.mainloop()
