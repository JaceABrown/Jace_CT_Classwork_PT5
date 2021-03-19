import random
myList = []

def mainProgram():
    while True:
        try:
            print("hello, there! Let's work with lists!")
            print("Choose from the following option. type a number below!")    
            choice = input("""1. add to a list or

 2. add a bunch of numbers
 2. Return the value at an index position!
 3. Random Search
 6. print contents of list 
 4. Quit Program""")
            if choice =="1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                randomSearch()
            elif choice == "4":
                randomSearch
            elif choice == "5":
                print(myList)
            elif choice == "6":
                print(myList)
            else:
                break
        except:
            print:("you made a whoopsie")
    
    
def addToList():
    print("adding to a list! Great choice")
    newItem = input("type an integer here!  ")
    myList.append(int(newItem))
    
def addABunch():
    print("we are adding a bunch of intergers here! ")
    numToAdd = input("how many new intergers would you like to add!")
    numRange = input("and how high would you like these numbers to go?")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("your list is now complete.")



def indexValues():
    print("ohhh! i heard you need a piece of date!")
    indexPos = input("what index position are you  curious about?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("RANdOm SeArCh")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("we'er gonna check out each item one at a time in your list!  this sucks")
    serchItem = input("what you looking for, pardner")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position{}".format(x))
            

if __name__ == "__main__":
    mainProgram()
