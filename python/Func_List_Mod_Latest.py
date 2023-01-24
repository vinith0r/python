# Automating all the posible things that can be done in LIST 
from colorama import Fore, Back, Style 
import os   #importing os to use linux cmd inside python
import pandas as pd
l = []
l2 = []
sum = 0
#title function
def top():
    print("\n\n******************************LIST MODIFICATOIN**********************************\n\n")

def pop2():
	op = int(input("\nEnter the index to be deleted ! : "))
	l2.pop(op)
	print("\nElement in index {} has been poped out!\n\n".format(op))
	print("\n\nLIST 2 : {} \n\n".format(l2))
def pop1():
    o = int(input("\nEnter the index to be deleted ! : "))
    l.pop(o)
    print("\nElement in index {} has been poped out!\n\n".format(o))
    print("\n\nLIST 2 : {} \n\n".format(l))
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
            t=int(input("\n\n(1) pop using index (2) last element : "))
            if t==1:
                pop2()  #this function is completed
            elif t==2:
                l2.pop()
                print("\n\npoping last Element in the list 1........\n\n")
                print("\n\nLIST 2 {}: \n\n ".format(l2))
            else:
                print("put correct option")
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
            t=int(input("\n\n(1) pop using index (2) last element : "))
            if t==1:
                pop1() #completed
            elif t==2:
                l.pop()
                print("\n\npoping last Element in the list 1........\n\n")
                print("\n\nLIST 1 {}: \n\n ".format(l))
            else:
                print("put correct option")
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
# check whether  it's mutable or imutable 
# Imutable : when we modify the value, the address also changing that is Imutable 
# Mutable : when we can modify the value without changing the address of it that is mutable
#!!! problem : List is mutable so this function should say it's mutable
# example of Mutable List:
# >>> list=['hello', '132.1', 'welcome']
# >>> id(list)
# >>> 140501974891712
# >>> list.append('j')
# >>> list
# >>> ['hello', '132.1', 'welcome', 'j']
# >>> id(list)
# >>> 140501974891712
def MorI():
    q = int(input("\n(1)check list 1 (2)check list 2 : "))
    if q==1:
        if l is l.append('1'):                          #comparing the address/id of the l and after modification of value using 'is'
            print("\n\nLIST 1 is 'MUTABLE'\n\n")
        else:
            print("\n\nLIST 1 is 'IMUTABLE'\n\n")
    elif q==2:
        if l2 is l2.append('2'):
            print("\n\nLIST 2 is 'MUTABLE' \n\n")
        else:
            print("\n\nLIST 2 is 'IMUTABLE'\n\n")
    else:
        print("\nput correct option!!!!\n")
#using pandas
def data():
    n = int(input("\n(1)List 1 (2)List 2 : "))
    if n==1:
        ds = pd.Series(l)
        print(ds)
    elif n==2:
        ds ==pd.Series(l2)
    else:
        print("put correct option")
#--------------------not completed-------------------------------------------------------addtion of list using sum()function
def mathadd():
    ad = int(input("\n\n(1) Addtion of List 1\n\n (2)Addtion of List 2  : "))
    if ad==1:
        # Convert the list of strings to a list of integers
        int_list = [int(x) for x in l]

        # Use the sum() function to add all the elements in the list
        result = sum(int_list)

        print("Sum of elements in the list: ", result)

    elif ad==2:
        int_list = list(map(int,l2))
        result = sum(int_list)
        print("Sum of elements in the list: ", result)
    else:
        print("put correct option")
 #------------------------------------------------------------------------------------------------------------
# joining of list 1 and 2
def join():
    for i, (x, y) in enumerate(zip(l, l2)):
        print("[{}] + [{}] = {}".format(i,i,x+y))
# addition of list 1 an 2
def adl1l2():
    for u in range (len(l and l2)):
        print("\nsubtraction of List 1 and list 2 : {}".format(int(l[u])+int(l2[u])))
# subtraction of list 1 and 2
def sub1():
   for u in range (len(l and l2)):
    print("\nsubtraction of List 1 and list 2 : {}".format(int(l[u])-int(l2[u])))
# multiplicatoin of list 1 and 2
def mult1():
   for u in range(len(l and l2)):
    print("\nMultiplication of List 1 and list 2 : {}".format(int(l[u])*int(l2[u])))
# divtion of list 1 and 2
def div1():
   for u in range (len(l and l2)):
    print("\ndivition of List 1 and list 2 : {}".format(float(l[u])/float(l2[u])))
# remainder of list 1 and 2
def rem1():
   for u in range (len(l and l2)):
    print("\nremainder of List 1 and list 2 : {}".format(int(l[u])%int(l2[u])))
#integer divition of list 1 and 2
def intdiv():
   for u in range (len(l and l2)):
    print("\ninteger divition of List 1 and list 2 : {}".format(int(l[u])//int(l2[u])))
# order of list 1 and 2
def order1():
   for u in range (len(l and l2)):
    print("\norder of List 1 and list 2 : {}".format(int(l[u])**int(l2[u])))
#-------------------------------------can be done like line 149-------------------------------------------------getting index
# problem : i want index also to be printed like [0]+[0]
#        for x in l:
#            for y in l2:
 #   print("Addtion of List 1 and list 2 {}+{}: {}".format(index(x), index(y), int(l[u])+int(l[u])))

#--------------------------------------------------------------------------------------------------
#access linux using linux() function
def linux():
    while True:
        s = input("$ ")
        os.system(s)
#this is go to the modify function
def play():
    while True:
        j = int(input("\n\n(1)add (2)extend (3)compare (4)List_MATH (5)check Mutable or Imutable (6)exit (7)pandas_series (8)join\n\n$:>>>>: "))
        if j==1:
            print("\nAdded List : {}\n".format(l+l2))
        elif j==2:
            l.extend(l2)
            print("\nExtended List : {}\n".format(l))
        elif j==3:
            if l==l2:
                print("\nList 1:{} and List 2 :{} are SAME\n".format(l, l2))
            else:
                print("\nList 1:{} and List 2:{} are not SAME\n".format(l, l2))
        elif j==4:
            v = int(input("\n\n(1)add list 1 and 2 (2)sub (3)mult (4)div (5)int div (6)order (7)remeinder (8)back (9)listadd\n$:>>>>>: "))
            if v==1:
                adl1l2()
            elif v==2:
                sub1()
            elif v==3:
                mult1()
            elif v==4:
                div1()
            elif v==5:
                intdiv()
            elif v==9:
                mathadd()
            elif v==6:
                order1()
            elif v==8:
                print("\nexiting....\n")
                break
            elif v==7:
                rem1()
            else:
                print("Put correct option")
                continue
        elif j==5:
            MorI()
        elif j==6:
            print("\n!!exiting.....\n")
            break
        elif j==7:
            data()
        elif j==8:
            join()
        else:
            print("\n\nput correct option!!!\n\n")
            continue
#menu
#Modifing the List 1 and list 2 
def menu():
    #giving graphical banner
    os.system("toilet -f ivrit 'LIST-EXPRIMENT' | boxes -d cat -a hc -p h8 |lolcat")
    os.system(" echo '\033[1;34m' --created by '\033[1;32m'-V I N I T H-") 
    print(Fore.MAGENTA+" in < @vinit_h01")
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
            os.system('fortune | cowsay -f eyes | toilet --metal -f term') # banner with random message after exiting
            break
        else:
            print("\n!!put correct option!!\n")
            continue
#calling menu functions
menu()
