def mainprogram():
    myList = []
    print("hello, there! Let's work with lists!")
    print("Choose from the following option. type a number below!")    
    choice = input("1. add to a list , 2. Return the value at an index position!   ")
    if choice =="1":
        addToList()
    elif choice == "2":
        indexValues()
    
    
def addToList():
    print("adding to a list! Great choice")
    newItem = input("type an integer here!  ")
    myList.append(int(newItem))

def indexValues():

if __Name__ == "__main__":
