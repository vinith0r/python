import os
l = []
l2 = []
def List2():
    while True:
        option = int(input("\n(1)add\n(2)pop\n(3)sort\n(4)emty\n(5)clear\n(6)exit : "))
        if option==1:
            op2 = input("Enter the Element to add : ")
            l2.append(op2)
            print(l2)
        elif option==2:
            l2.pop()
            print(l2)
        elif option==3:
            l2.clear()
            print(l2)
        elif option==4:
            l2.sort()
            print(l2)
        elif option==5:
            os.system('clear')
        elif option==6:
            print("Exiting......")
            break
        else:
            print("put correct option")
            continue
def List1():
    while True:
        option = int(input("\n(1)add\n(2)pop\n(3)sort\n(4)emty\n(5)clear\n(6)exit : "))
        if option==1:
            op2 = input("Enter the Element to add : ")
            l.append(op2)
            print(l)
        elif option==2:
            l.pop()
            print(l)
        elif option==3:
            l.clear()
            print(l)
        elif option==4:
            l.sort()
            print(l)
        elif option==5:
            os.system('clear')
        elif option==6:
            print("Exiting......")
            break
        else:
            print("put correct option")
            continue
def modify():
    while True:
        mod=int(input("(1)modify List 1 (2) modify list 2 (3) both : "))
        if mod==1:
           List1()
        elif mod==2:
            List2()
        elif mod==3:
            print("modifing")
        else:
            print("put correct option")
            continue
#calling functions
modify()