## using sets to find duplicates in a list with only duplicate values
# list containing data
from colorama import init, Fore, Back, Style
import subprocess as sp
import time
init(autoreset=True)
CYAN =  Fore.CYAN
sp.call('cls', shell=True)
duplicatesnew = []
space = "     "
space1 = "    "
def create_text():
    print (CYAN+space1 +" _____  _    _ _____  _      _____ _____       _______ ______  ")
    print (CYAN+space1 +"|  __ \| |  | |  __ \| |    |_   _/ ____|   /\|__   __|  ____| ")
    print (CYAN+space1 +"| |  | | |  | | |__) | |      | || |       /  \  | |  | |__    ")
    print (CYAN+space1 +"| |  | | |  | |  ___/| |      | || |      / /\ \ | |  |  __|   ")
    print (CYAN+space1 +"| |__| | |__| | |    | |____ _| || |____ / ____ \| |  | |____  ")
    print (CYAN+space1 +"|_____/ \____/|_|    |______|_____\_____/_/    \_\_|  |______| ")


    print (CYAN+space1 +space + " _____  ______ __  __  ______      ________ _____    ")
    print (CYAN+space1 +space + "|  __ \|  ____|  \/  |/ __ \ \    / /  ____|  __ \  ")
    print (CYAN+space1 +space + "| |__) | |__  | \  / | |  | \ \  / /| |__  | |__) | ")
    print (CYAN+space1 +space + "|  _  /|  __| | |\/| | |  | |\ \/ / |  __| |  _  /  ")
    print (CYAN+space1 +space + "| | \ \| |____| |  | | |__| | \  /  | |____| | \ \  ")
    print (CYAN+space1 +space + "|_|  \_\______|_|  |_|\____/   \/   |______|_|  \_\ ")
    print (CYAN+space1 +"===============================================================")
    print (CYAN+space1 +"                         Made by: 50r4                         ")
    print (CYAN+space1 +"===============================================================")
def check_duplicates():
    create_text()

    lst1 = open("hit.txt").readlines()
    f = open("noduplicates.txt", "a")
    x = 0
    q = 0
    # create an empty set
    duplicates = set()
    # loop through elements and find matches
    for i in lst1:
        if i not in duplicates:
            duplicates.add(i)
    for sub in duplicates:
        duplicatesnew.append(sub.replace("\n", ""))
  # show data
    for c in duplicates:
        time.sleep(0.1)
        link = (list(duplicatesnew)[x])

        x += 1
        f.write(str(link+'\n'))
        if q == 5:
            sp.call('cls', shell=True)
            create_text()
            q = 0
        print(CYAN+space1+"                "+"["+link+"]")
        q += 1




check_duplicates()
