from hashlib  import md5,sha1,sha256,sha512
import string
from os import system
import threading
import multiprocessing

word=[]
list=[]
hashs=[]
count=0
bakra=""


def comp2(get,count):
    int=count
    got=0
    #print("{} comapring with {}".format(get,word[int]))

    while int>=0:
    #    print("{} comapring with {}".format(get,word[int]))
        if get==word[int]:

            print("[+] {} is  {}".format(list[int],word[int]))
            got=1
            #asks(count)
        int-=1

        #asks(count)



def files(count):
    mc=0
    #system('clear')
    print ("====================================================")
    print ("             lightning Mode Enabled")
    print ("\n                            Made By:-Sarthak Saini")
    print ("====================================================")
    hashi=input("Enter hashfile name with Full path:-")
    hashes=open(hashi,"r")

    for i in hashes:
        mc+=1
        hashs.append(i.strip())


    mc-=1
    print("\nChoose the method to Operate With:-\n\nPress 1 for MultiThreading (it's safe for system but slow)\nPress 2 for multiProcessing (it's fast but might crash your system with big wordlist)")
    e=input(">")

    print("[+] Starting the comparison ...")

    temps1=int(mc/2)


    if e=='1':
        print ("[+] Mode:-MultiThreading Activated")
        p1 = threading.Thread(target=rusty,args=(mc, temps1))
    elif e=='2':
        print ("[+] Mode:-multiProcessing Activated")
        p1 = multiprocessing.Process(target=rusty, args=(mc,temps1,))
    else:
        print ("[+] Default mode:-Threading Activated")
        p1 = threading.Thread(target=rusty,args=(mc, temps1))

    kc=temps1
    temps2=int(0)
    if e=='1':
        p2 = threading.Thread(target=rusty,args=(kc,temps2))
    elif e=='2':
        p2 = multiprocessing.Process(target=rusty, args=(kc,temps2,))
    else:
        p2 = threading.Thread(target=rusty,args=(kc,temps2))

    print("\n++++++++++++++++++++++++++++++++++++++++++++")
    print("[*] Total Number of Hashes To decrypt {}".format(mc))
    print("++++++++++++++++++++++++++++++++++++++++++++\n\n")
    #fucker(mc,temps1)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    asks(count)

def rusty(mc,temps1):
    while mc>temps1:

        comp2(hashs[mc],count)
        #print(mc)
        #ml=input("enter:::")
        mc-=1

def asks(count):
    try:
        e=input("Enter choice\npress 1 to enter a hash\npress 2 to enter a file of hashes\n>")
        if e=='1':
            get=input("\nenter hash :")
            comp(get,count)
        elif e=='2':
            files(count)
        else:
            print("error")
    except:
        exit(0)

def hash(name):
    result=md5(name.encode())
    return result.hexdigest()

def hashsha(name):
    return sha1(name.encode()).hexdigest()

def hashsha256(name):
    return sha256(name.encode()).hexdigest()

def hashsha512(name):
    return sha512(name.encode()).hexdigest()


def rainbow(fdata):
    global count
    print("[+] Generating Rainbow file !")
    for i in fdata:
        count+=1

        list.append(i.strip())
        word.append(hash(i.strip()))

    count-=1
    print("[+] Done..{} Hashes loaded on Rainbow :)".format(count))
    asks(count)


def rainbowsha(fdata):
    global count
    print("[+] Generating Rainbow file !")
    for i in fdata:
        count+=1

        list.append(i.strip())
        word.append(hashsha(i.strip()))

    count-=1
    print("[+] Done..{} Hashes loaded on Rainbow :)".format(count))
    asks(count)

def rainbowsha256(fdata):
    global count
    print("[+] Generating Rainbow file !")
    for i in fdata:
        count+=1

        list.append(i.strip())
        word.append(hashsha256(i.strip()))

    count-=1
    print("[+] Done..{} Hashes loaded on Rainbow :)".format(count))
    asks(count)

def rainbowsha512(fdata):
    global count
    print("[+] Generating Rainbow file !")
    for i in fdata:
        count+=1

        list.append(i.strip())
        word.append(hashsha512(i.strip()))

    count-=1
    print("[+] Done..{} Hashes loaded on Rainbow :)".format(count))

    asks(count)


def comp(get,count):
    int=count
    got=0
    print("[+] Starting the comparison ...")
    while int>=0:

        if get==word[int]:
            print("[+] Found the target !!!!\n")
            print("{} is  {}".format(list[int],word[int]))
            got=1
            asks(count)
        int-=1
    if got==0:
        print("[-] Not Found Great sire !! ('__')")
        asks(count)





def start():
    bakra=input("\n\nEnter the wordlist with its full path:-")
    try:

            file=open(bakra, encoding="latin-1")
            print("[+] Importing the wordlist       [filename/path]::{}".format(bakra))
            print("[+] Done loading !")

            zop=input("\n[+]Enter the choice\npress 1 to md5\npress 2 to sha1\npress 3 to sha256\npress 4 to sha512\n>")
            if zop=='1':
                rainbow(file)
            elif zop=='2':
                rainbowsha(file)
            elif zop=='3':
                rainbowsha256(file)
            elif zop=='4':
                rainbowsha512(file)

    except:
        print("[-] Program Termination !")




def main():
    system('clear')

    print ("====================================================")
    print ("              HEXOR TREXOR v1.0")
    print ("\n                            Made by:-Sarthak Saini")
    print ("=====================================================")



    start()

main()
