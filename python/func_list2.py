import os
l = []
l2 = []
sum = 0
#title function
def top():
    print("\n\n******************************LIST MODIFICATOIN**********************************\n\n")

#modifing function for List2
def List2():
    while True:
        top()
        option = int(input("\n\n(1)add (2)pop (3)empty (4)sort (5)clearsrc (6)exit $:>>>>:  "))
        if option==1:
            op2 = input("\n\nEnter the Element to add : ")
            l2.append(op2)
            print("\n\nAdding Element to the list 1........\n\n")
            print("LIST 2 : {}\n\n".format(l2))
        elif option==2:
            l2.pop()
            print("\n\npoping last Element in the list 1........\n\n")
            print("\n\nLIST 2 {}: \n\n ".format(l2))
        elif option==3:
            l2.clear()
            print("\n\nclearing the List 1 Element to the list 1........\n\n")
            print("LIST 2 : {}\n\n".format(l2))
        elif option==4:
            l2.sort()
            print("\n\nSorting LIST 1........\n\n")
            print("LIST 2 : {}\n\n".format(l2))
        elif option==5:
            os.system('clear')
        elif option==6:
            print("\nExiting......")
            break
        else:
            print("\n\n!!!put correct option!!!\n\n")
            continue
#modifing list 1 function
def List1():
    while True:
        top()
        option = int(input("\n\n(1)add (2)pop (3)emty (4)sort (5)clearsrc (6)exit $:>>>>>:  "))
        if option==1:
            op2 = input("\n\nEnter the Element to add : ")
            l.append(op2)
            print("\n\nAdding Element to the list 1........\n\n")
            print("LIST 1 : {}\n\n".format(l))
        elif option==2:
            l.pop()
            print("\n\npoping last Element in the list 1........\n\n")
            print("\n\nLIST 1 {}: \n\n ".format(l))
        elif option==3:
            l.clear()
            print("\n\nclearing the List 1 Element to the list 1........\n\n")
            print("LIST 1 : {}\n\n".format(l))
        elif option==4:
            l.sort()
            print("\n\nSorting LIST 1........\n\n")
            print("LIST 1 : {}\n\n".format(l))
        elif option==5:
            os.system('clear')  #clears the screen
        elif option==6:
            print("\nExiting......")
            break
        else:
            print("\n\n!!!put correct option!!!\n\n")
            continue
#--------------------------------------------------------------------------------------------addtion of list
#def mathadd():
#   ad = int(input("\n\n(1) Addtion of List 1\n\n (2)Addtion of List 2  : "))
#   if ad==1:

#   #elif ad==1:
    #   print("Addtion of List 1 : {}".format(int(op2), sum(l)))
 #   else:
 #       print("put correct option")
 #------------------------------------------------------------------------------------------------------------

def adl1l2():
   for u in range (len(l and l2)):
    print("Addtion of List 1 and list 2 : {}".format(int(l[u])+int(l[u])))
#-------------------------------------------------------------------------------------------------getting index
#        for x in l:
#            for y in l2:
 #   print("Addtion of List 1 and list 2 {}{}: {}".format(index(x), index(y), int(l[u])+int(l[u])))

#--------------------------------------------------------------------------------------------------
#access linux using linux() function
def linux():
    while True:
        s = input("$ ")
        os.system(s)
#this is go to the modify function
def play():
    while True:
        j = int(input("\n(1)add (2)extend (3)compare (4)List_MATH (6)exit \n$:>>>>: "))
        if j==1:
            print("\nAdded List : {}\n".format(l+l2))
        elif j==2:
            l.extend(l2)
            print("\nExtended List : {}\n".format(l))
        elif j==3:
            if l==l2:
                print("\nList 1:{} and List:{} 2 are SAME\n".format(l, l2))
            else:
                print("\nList 1:{} and List 2:{} are not SAME\n".format(l, l2))
        elif j==4:
            adl1l2()
        else:
            print("\n!!exiting.....\n")
            break
#Modifing the List 1 and list 2
def modify():
    while True:
        top()
        mod=int(input("\n\n(1) modify List 1\n\n(2) modify list 2\n\n(3) play (4) linux (5) exit \n\n$:>>>>: "))
        if mod==1:
           List1()
        elif mod==2:
            List2()
        elif mod==3:
            play()
        elif mod==4:
            linux()
        elif mod==5:
            print("\nexiting..........\n")
            break
        else:
            print("\n!!put correct option!!\n")
            continue
#calling functions
modify()