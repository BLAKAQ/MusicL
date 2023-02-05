from os import system 
import time
def start():
    while True :
        system("rm -fr ./downloads/*")
        print("Done")
        time.sleep(120)

print("Started Cleaning ....\nby : @GGG66")
start()
