
myList = []

def mainprogram():
    while True:
    print("hello, there! Let's work with lists!")
    print("Choose from the following option. type a number below!")    
    choice = input("""1. add to a list or
2. Return the value at an index position!
3. exit Program """)
    if choice =="1":
        addToList()
    elif choice == "2":
        indexValues()
    elif choice == "3":
        break
    
    
def addToList():
    print("adding to a list! Great choice")
    newItem = input("type an integer here!  ")
    myList.append(int(newItem))

def indexValues():
    print("ohhh! i heard you need a piece of date!")
    indexPos = input("what index position are you  curious about?  ")
    print(myList[int(indexPos)])

if __Name__ == "__main__":
    mainProgram()
    
