import string
import random
import urllib3
import subprocess as sp
from colorama import init, Fore, Back, Style
import time
startTime = time.time()
init(autoreset=True)
init(convert=True)
sp.call('cls', shell=True)
http = urllib3.PoolManager()
#resets colorama color at the end of every line
def id_generator(size=6, chars=(string.ascii_lowercase)): # + "1234567890"
    return ''.join(random.choice(chars) for _ in range(size))
#generates end of a link it should try
CYAN = Fore.CYAN #colorma text color
space1 = "        "
space = "    "
global total_guessed
total_guessed = 0
global Repeat_counter
Repeat_counter = 0
#some variables
def img_generator(total_guessed):
    #clear cmd
    sp.call('cls', shell=True)
    print(CYAN+space1+'   _____   _    _    ____     _____   _______   ____    _____   _   _  ')
    print(CYAN+space1+'  / ____| | |  | |  / __ \   / ____| |__   __| |  _ \  |_   _| | \ | | ')
    print(CYAN+space1+' | |  __  | |__| | | |  | | | (___      | |    | |_) |   | |   |  \| | ')
    print(CYAN+space1+' | | |_ | |  __  | | |  | |  \___ \     | |    |  _ <    | |   | . ` | ')
    print(CYAN+space1+' | |__| | | |  | | | |__| |  ____) |    | |    | |_) |  _| |_  | |\  | ')
    print(CYAN+space1+'  \_____| |_|  |_|  \____/  |_____/     |_|    |____/  |_____| |_| \_| ')

    print(CYAN+space+'   _____   ______   _   _   ______   _____               _______    ____    _____   ')
    print(CYAN+space+'  / ____| |  ____| | \ | | |  ____| |  __ \      /\     |__   __|  / __ \  |  __ \  ')
    print(CYAN+space+' | |  __  | |__    |  \| | | |__    | |__) |    /  \       | |    | |  | | | |__) | ')
    print(CYAN+space+' | | |_ | |  __|   | . ` | |  __|   |  _  /    / /\ \      | |    | |  | | |  _  /  ')
    print(CYAN+space+' | |__| | | |____  | |\  | | |____  | | \ \   / ____ \     | |    | |__| | | | \ \  ')
    print(CYAN+space+'  \_____| |______| |_| \_| |______| |_|  \_\ /_/    \_\    |_|     \____/  |_|  \_\ ')
    print(CYAN+space+"                                                                                    ")
    print(CYAN+space+"====================================================================================")
    print(CYAN+space+"           Made by: 50r4          Total guessed:"+str(total_guessed)+"                               ")
    print(CYAN+space+"====================================================================================")
#generates this text with number of valid links
img_generator(0) #dont change the zero its used fot the total_guessed counter
# links_for_generation = int(input(Fore.CYAN+"" + "    How many links should i try to guess: "))
links_for_generation = 100

#creates the link and checks it
def check_and_generation(generator_lenght, imtrying):
    linky = ""
    global should_i_reset_it
    global total_guessed
    global Repeat_counter
    should_i_reset_it = 0
    for x in range(imtrying): #how many links do you want to create
        link = 'https://ghostbin.co/paste/'+(id_generator(generator_lenght)) #makes the link with the id_generator and connects it to ghostbin url
        r = http.request('GET', link)

        if str(r.status) == "404": #check if the url is valid
            Repeat_counter += 1
            print (Fore.RED +"                              "+"|" +link+"|"+Fore.CYAN+"  |"+str(Repeat_counter)+"|")
        if str(r.status) == '200':
            f = open("hit.txt", "a") #opens file to write links in
            #linky += link+"\n"
            f.write(link+"\n") #if the link is valind it writes itself into hit.txt
            f.close()
            Repeat_counter += 1
            print (Fore.GREEN +"                              "+"|"+link+"|"+Fore.CYAN+"  |"+str(Repeat_counter)+"|")
            total_guessed += 1 #add 1 if guessed correctly
        should_i_reset_it += 1 #counter if UI should reset
        if should_i_reset_it == 12: #how many links should be at console at 1 time
            img_generator(total_guessed)
            should_i_reset_it = 0


    f.close()
check_and_generation(5, links_for_generation)
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
