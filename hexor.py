from hashlib  import md5,sha1,sha256,sha512
from os import system


list={}
count=0

def asks():
    try:
        e=input("Enter choice\npress 1 to enter a hash\npress 2 to enter a file of hashes\n>")
        if e=='1':
            get=input("\nenter hash :")
            if get in list:
                print(get," is ",list[get])
        elif e=='2':
            arm()
        else:
            print("error")
    except:
        exit(0)


def rainbow(file):
    global count
    print("[+] Generating Rainbow file !")
    for i in file:
        count+=1
        list[hash(i.replace('\n',''))]=i.replace('\n','')
    print("[+] Done..{} Hashes loaded on Rainbow :)".format(count))
    asks()


def rainbowsha(file):
    global count
    print("[+] Generating Rainbow file !")
    for i in file:
        count+=1
        list[hashsha(i.replace('\n',''))]=i.replace('\n','')

    print("[+] Done..{} Hashes loaded on Rainbow :)".format(count))
    asks()


def rainbowsha256(file):
    global count
    print("[+] Generating Rainbow file !")
    for i in file:
        count+=1
        list[hashsha256(i.replace('\n',''))]=i.replace('\n','')
    print("[+] Done..{} Hashes loaded on Rainbow :)".format(count))
    asks()

def rainbowsha512(file):
    global count
    print("[+] Generating Rainbow file !")
    for i in file:
        count+=1
        
        list[hashsha512(i.replace('\n',''))]=i.replace('\n','')
    print("[+] Done..{} Hashes loaded on Rainbow :)".format(count))
    asks()





def finder(name):
    if name in list:
        print(name," is ",list[name])


def hash(name):
    result=md5(name.encode())
    return result.hexdigest()

def hashsha(name):
    return sha1(name.encode()).hexdigest()

def hashsha256(name):
    return sha256(name.encode()).hexdigest()

def hashsha512(name):
    return sha512(name.encode()).hexdigest()


def start():
        bakra=input("\n\nEnter the wordlist with its full path:-")
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





def arm():
    print ("\n\n[+] Enter the Hashfile full name with path")
    hashi=input(">")
    ak=open(hashi,"r")
    for i in ak:

        finder(i.replace('\n',''))

def main():
    system('clear')

    print ("====================================================")
    print ("              HEXOR TREXOR v1.0")
    print ("\n                            Made by:-Sarthak Saini")
    print ("=====================================================")



    start()


main()
