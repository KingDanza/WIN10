import os
import config

CBLACK = '\33[30m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE = '\33[36m'
CWHITE = '\33[37m'

CEND = '\33[0m'
CBOLD = '\33[1m'
CITALIC = '\33[3m'
CURL = '\33[4m'
CBLINK = '\33[5m'
CBLINK2 = '\33[6m'
CSELECTED = '\33[7m'

ENDC = '\033[0m'
CBLACKBG = '\33[40m'
CREDBG = '\33[41m'
CGREENBG = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG = '\33[46m'
CWHITEBG = '\33[47m'

def clear():
    os.system('cls')  # on Windows System
    
def mainMenu():
    clear()
    banner()
    c1 = "\33[6m"
    print(49 * "-")
    print('''| ''' + CBLUEBG +     ''' [1] ''' + CVIOLETBG + CYELLOW + '''| Crack With Aircrack-ng (without BSSID) |
''' + ENDC + '''| ''' + CVIOLETBG +''' [2] ''' + CBLUEBG + CWHITE +    '''| Crack With Aircrack-ng (with BSSID)    |
''' + ENDC + '''| ''' + CBLUEBG +  ''' [3] ''' + CVIOLETBG + CYELLOW + '''| Crack With Hashcat (with wordlist)     |
''' + ENDC + '''| ''' + CVIOLETBG +''' [4] ''' + CBLUEBG + CWHITE +    '''| Crack With Hashcat (with mask)         |
''' + ENDC + '''| ''' + CBLUEBG +  ''' [5] ''' + CVIOLETBG + CYELLOW + '''| Crack With Hashcat (with masklist)     |
''' + ENDC + '''| ''' + CVIOLETBG +''' [6] ''' + CBLUEBG + CWHITE +    '''| Helpful Infomation                     |
''' + ENDC + '''| ''' + CBLUEBG +  ''' [7] ''' + CVIOLETBG + CYELLOW + '''| Exit Script                            |
''' + ENDC + '''| ''' + CVIOLETBG +''' [8] ''' + CBLUEBG + CWHITE +    '''|                                        |
''' + ENDC + '''| ''' + CBLUEBG +  ''' [9] ''' + CVIOLETBG + CYELLOW + '''|                                        |''' + ENDC + '''''')
    print(49 * "-")
    tt = input("| [!] Make your choice: ")
    print(49 * "-")
    if tt == "1":
        airCrack()
        mainMenu()
    elif tt == "2":
        airCrackBSSID()
        mainMenu()        
    elif tt == "3":
        hashCATwordlist()
        mainMenu()
    elif tt == "4":
        hashCATmask()
        mainMenu()
    elif tt == "5":
        hashCATmasklist()
    elif tt == "6":
        readme()
def readme():
    print('''|  This is a script for Windows 10 users only.  | 
|  You will need to manually download Aircrack  |
|  and Hashcat before you'll be able to use any |
|  of the options you see. To download them     |
|  just google Aircrack-ng and download the     |
|  windows version. Do the same for Hashcat.    |
|  After you have those, edit the config file   |
|  that was included with this script. Add your |
|  file paths to Aircrack and Hashcat as asked. |''')
    print(49 * "-")
    
def hashCATmasklist():
    cappath= input("| Hccapx Path: ")
    print(49 * "-")
    print('''| ''' + CRED + '''Masklist info:''' + ENDC + '''                                |
| Create a file named masks.hcmask and inside   |
| put a new mask combo on each line. Save the   |
| file and use it as your masklist. If you're   |
| confused, check the image linked below.       |
|                                               |
| Example: https://i.ibb.co/hZW0B1b/masks.png   |''')
    print(49 * "-")
    wlist= input("| Masklist Path: ")
    command = "" + config.hashcatEXEpath + " --potfile-disable -o crack.txt -w 3 -a 3 -m 22000 " + cappath + " " + wlist + ""
    os.chdir(config.hashcatpath)
    os.system("start cmd.exe @cmd /k " + command)
    
def airCrack():
    #bssidd= input("BSSID: ")
    cappath= input("| Capture Path: ")
    wlist= input("| Wordlist Path: ")
    command = "" + config.aircrackEXEpath + " -w " + wlist + " " + cappath + ""
    os.chdir(config.aircrackpath)
    os.system("start cmd.exe @cmd /k " + command)
def airCrackBSSID():
    bssidd= input("| BSSID: ")
    cappath= input("| Capture Path: ")
    wlist= input("| Wordlist Path: ")
    command = "" + config.aircrackEXEpath + " -b " + bssidd + " -w " + wlist + " " + cappath + ""
    os.chdir(config.aircrackpath)
    os.system("start cmd.exe @cmd /k " + command)

def hashCATmask():
    cappath= input("| Hccapx Path: ")
    print(49 * "-")
    print('''| ''' + CRED + '''Mask options:''' + ENDC + '''                                 |
| ?l = abcdefghijklmnopqrstuvwxyz               |
| ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ               |
| ?d = 0123456789                               |
| ?h = 0123456789abcdef                         |
| ?H = 0123456789ABCDEF                         |
| ?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~  |
| ?a = ?l?u?d?s                                 |
| ?b = 0x00 – 0xff                              |''')
    print(49 * "-")
    mask= input("| Mask: ")
    #wlist= input("Wordlist Path: ")
    command = "" + config.hashcatEXEpath + " --potfile-disable -o crack.txt -m 22000 -a 3  " + cappath + " " + mask + ""
    os.chdir(config.hashcatpath)
    os.system("start cmd.exe @cmd /k " + command)

def hashCATwordlist():
    cappath= input("| Hccapx Path: ")
    #mask= input("Mask: ")
    wlist= input("| Wordlist Path: ")
    command = "" + config.hashcatEXEpath + " --potfile-disable -o crack.txt -m 22000 -a 0 " + cappath + " " + wlist + ""
    os.chdir(config.hashcatpath)
    os.system("start cmd.exe @cmd /k " + command)
        
def banner():
        print('''
 ''' + CBLUE +   '''██╗    ██╗██╗███╗   ██╗ ██╗ ██████╗     ██╗    ██╗██████╗  █████╗ 
 ''' + CVIOLET + '''██║    ██║██║████╗  ██║███║██╔═████╗    ██║    ██║██╔══██╗██╔══██╗
 ''' + CBLUE +   '''██║ █╗ ██║██║██╔██╗ ██║╚██║██║██╔██║    ██║ █╗ ██║██████╔╝███████║
 ''' + CVIOLET + '''██║███╗██║██║██║╚██╗██║ ██║████╔╝██║    ██║███╗██║██╔═══╝ ██╔══██║
 ''' + CBLUE +   '''╚███╔███╔╝██║██║ ╚████║ ██║╚██████╔╝    ╚███╔███╔╝██║     ██║  ██║
''' + CVIOLET + '''  ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═╝ ╚═════╝      ╚══╝╚══╝ ╚═╝     ╚═╝  ╚═╝'''+ ENDC)
        print(49 * "-")
        print('''|  This is a script for ''' + CURL + CBLUE + '''Windows 10''' + ENDC + ''' users only.  | 
|  You will need to manually download ''' + CYELLOW + '''Aircrack''' + ENDC + '''  |
|  and ''' + CYELLOW + '''Hashcat''' + ENDC + ''' before you'll be able to use any |
|  of the options you see. To download them     |
|  just google ''' + CVIOLET + '''Aircrack-ng''' + ENDC + ''' and download the     |
|  windows version. Do the same for ''' + CVIOLET + '''Hashcat''' + ENDC + '''.    |
|  After you have those, edit the config file   |
|  that was included with this script. Add your |
|  file paths to ''' + CGREEN + '''Aircrack''' + ENDC + ''' and ''' + CGREEN + '''Hashcat''' + ENDC + ''' as asked. |''', end="")
        print(49 * "")
mainMenu()


