import os
import time
import py_compile
os.system("clear")
os.system("pip3 install uncompyle6")
os.system("clear")

# Bold
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
b="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
def banner() :

    print(R+"             __   __    _   _    _    ____  _   _   ")
    time.sleep(0.1)
    print(R+"             \ \ / /   | | | |  / \  / ___|| | | |  ")
    time.sleep(0.1)
    print(R+"              \ V /____| |_| | / _ \ \___ \| |_| |  ")
    time.sleep(0.1)
    print(R+"               | |_____|  _  |/ ___ \ ___) |  _  |  ")
    time.sleep(0.1)
    print(R+"               |_|     |_| |_/_/   \_\____/|_| |_|  ")
    time.sleep(0.1)
    print(W+"               _____ _____ _____ _____ _____ _____  ")
    time.sleep(0.1)
    print(b+"              |_____|_____|_____|_____|_____|_____|   ")
    time.sleep(0.1)
    print(W+"         _____ _____ _____ _____ _____ _____ _____ _____ ")
    time.sleep(0.1)
    print(b+"        |_____|_____|_____|_____|_____|_____|_____|_____|  ")
    time.sleep(0.1)

    print("         _                                             _  ")
    time.sleep(0.1)
    print("       _| |_            \033[1;33m♤Welcome To Y-Hash♤        \033[1;34m  _| |_  ")
    time.sleep(0.1)
    print("      \033[1;34m|_   _|                                       |_   _| ")
    time.sleep(0.1)
    print("       \033[1;34m |_|                                           |_|     ")
    time.sleep(0.1)
    print("         \033[1;34m_ \033[1;31m=====>>> \033[1;37m[\033[1;31m1\033[1;37m] \033[1;32mEncode python                  \033[1;34m_ ")

    time.sleep(0.1)
    print("       \033[1;34m_| |_                                         _| |_  ")
    time.sleep(0.1)
    print("      \033[1;34m|_   _|                                       |_   _| ")
    time.sleep(0.1)
    print("        \033[1;34m|_|                                           |_|     ")
    time.sleep(0.1)
    print("         \033[1;34m_ \033[1;31m=====>>> \033[1;37m[\033[1;31m2\033[1;37m] \033[1;32mDecode python                  \033[1;34m_ ")
    time.sleep(0.1)
    print("       \033[1;34m_| |_                                         _| |_  ")
    time.sleep(0.1)
    print("      \033[1;34m|_   _|                                       |_   _| ")
    time.sleep(0.1)
    print("        \033[1;34m|_|                                           |_|     ")
    time.sleep(0.1)
    print("         \033[1;34m_ \033[1;31m=====>>> \033[1;37m[\033[1;31m3\033[1;37m] \033[1;32mExit Y-Hash                    \033[1;34m_ ")
    time.sleep(0.1)
    print("       \033[1;34m_| |_                                         \033[1;34m_| |_  ")


    time.sleep(0.1)
    print("      |_   _|                                       \033[1;34m|_   _| ")
    time.sleep(0.1)
    print("        |_|     \033[1;33m♧By:Yassa Lotfy♧                      \033[1;34m|_|     ")

    time.sleep(0.1)
Loop=True
while Loop:
    banner ()
    Y=input(R+"        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    if Y == '1' :
       os.system("clear")
       os.system("clear")
       print("                 _____                     _  ")
       time.sleep(0.1)
       print("                | ____|_ __   ___ ___   __| | ___   ")
       time.sleep(0.1)
       print("                |  _| | '_ \ / __/ _ \ / _` |/ _ \  ")
       time.sleep(0.1)
       print("                | |___| | | | (_| (_) | (_| |  __/ ")
       time.sleep(0.1)
       print("                |_____|_| |_|\___\___/ \__,_|\___|  ")
       time.sleep(0.1)
       print(W+"                _____ _____ _____ _____ _____ _____  ")
       time.sleep(0.1)
       print(b+"               |_____|_____|_____|_____|_____|_____|   ")
       time.sleep(0.1)
       print(W+"          _____ _____ _____ _____ _____ _____ _____ _____ ")
       time.sleep(0.1)
       print(b+"         |_____|_____|_____|_____|_____|_____|_____|_____|  ")
       time.sleep(0.1)
       print("")
       Hash=input("         \033[1;37m[\033[1;31m+\033[1;37m] \033[1;33mType A File Name \033[1;31m=====>>> ")
       YT=os.rename(hash , "Y.py" )  
       py_compile.compile(YT)
       os.system("mv __pycache__ -- EncodeY-Hash")
       os.system("mv EncodeY-Hash .. ")
       print(W+"                      ♧File encryption succeeded♧     ")

       print("")
       print("")
       YHK=input(G+"Go to the home page")
       if YHK == "" :
          os.system("clear")
    if Y == '2' :
       os.system("clear")
       print("                 ____                     _   ")
       time.sleep(0.1)
       print("                |  _ \  ___  ___ ___   __| | ___   ")
       time.sleep(0.1)
       print("                | | | |/ _ \/ __/ _ \ / _` |/ _ \ ")
       time.sleep(0.1)
       print("                | |_| |  __/ (_| (_) | (_| |  __/ ")
       time.sleep(0.1)
       print("                |____/ \___|\___\___/ \__,_|\___|  ")
       time.sleep(0.1)
       print(W+"                _____ _____ _____ _____ _____ _____  ")
       time.sleep(0.1)
       print(b+"               |_____|_____|_____|_____|_____|_____|   ")
       time.sleep(0.1)
       print(W+"          _____ _____ _____ _____ _____ _____ _____ _____ ")
       time.sleep(0.1)
       print(b+"         |_____|_____|_____|_____|_____|_____|_____|_____|  ")
       time.sleep(0.1)
       print("")
       h=input("         \033[1;37m[\033[1;31m+\033[1;37m] \033[1;33mType A File Name \033[1;31m=====>>> ")
       x=os.system("uncompyle6 " +h)
       print(x)
       time.sleep(2)
       print("")
       print("")
       YHK=input(G+"Go to the home page")
       if YHK == "" :
          os.system("clear")
    if Y == "3" :
       os.system("clear")
       quit()
       os.system("cd..")
    if Y =="" :
       os.system("clear")
       print("ERROR❎"*50)
       os.system("clear")
       time.sleep(0.1)



