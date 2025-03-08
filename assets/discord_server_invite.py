import requests
import os
from colorama import Fore, init, Style

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def server_lookup(invite_link):

    try:
        response = requests.get(f"https://discord.com/api/v10/invites/{invite_link}")
        response.raise_for_status()
        discord = response.json()
        inviter = discord.get('inviter', {})
        username = inviter.get('username') or 'Unknown'
        userid = inviter.get('id') or 'Unknown'
        username2 = inviter.get('global_name') or 'Unknown'
        guild = discord.get('guild', {})
        code = discord.get('code')
        date = discord.get('expires_at') or 'Never'
        serverid = guild.get('id') or 'Unknown'
        verification = guild.get('verification_level') or 'Unknown'
        channel = discord.get('channel', {}).get('name') or 'Unknown'
        servername = guild.get('name') or 'Unknown'
        results = f"""
      {Fore.WHITE}[ {Fore.BLUE}Invite Information{Fore.WHITE} ]

        {Fore.WHITE}[ {Fore.BLUE}Invite Details{Fore.WHITE} ]
    {Fore.BLUE}> + {Fore.WHITE}Invite Link     :{Fore.LIGHTBLACK_EX} https://discord.gg/{code}
    {Fore.BLUE}> + {Fore.WHITE}Target Channel  :{Fore.LIGHTBLACK_EX} {channel}
    {Fore.BLUE}> + {Fore.WHITE}Expiration Date :{Fore.LIGHTBLACK_EX} {date}

       {Fore.WHITE}[ {Fore.BLUE}Inviter Details{Fore.WHITE} ]
    {Fore.BLUE}> + {Fore.WHITE}Username        :{Fore.LIGHTBLACK_EX} {username}
    {Fore.BLUE}> + {Fore.WHITE}Global Username :{Fore.LIGHTBLACK_EX} {username2}
    {Fore.BLUE}> + {Fore.WHITE}User ID         :{Fore.LIGHTBLACK_EX} {userid}

          {Fore.WHITE}[ {Fore.BLUE}Server Details{Fore.WHITE} ]
    {Fore.BLUE}> + {Fore.WHITE}Server Name        :{Fore.LIGHTBLACK_EX} {servername}
    {Fore.BLUE}> + {Fore.WHITE}Server ID          :{Fore.LIGHTBLACK_EX} {serverid}
    {Fore.BLUE}> + {Fore.WHITE}Verification Level :{Fore.LIGHTBLACK_EX} {verification}
"""
        print(results)
        save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
        if save == "y":
            save_path = os.path.join(BASE_DIR, "server_invite.txt")
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"""Invite Details

Invite Link     : https://discord.gg/{code}
Target Channel  : {channel}
Expiration Date : {date}

Inviter Details

Username        : {username}
Global Username : {username2}
User ID         : {userid}

Server Details

Server Name        : {servername}
Server ID          : {serverid}
Verification Level : {verification}
""")
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")
        
        elif save == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
            
        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")

    
        input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")
    
    except requests.exceptions.RequestException:
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Request failed. Either Discord servers are down, or the link is invalid")    
        input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")

def server_lookup_main():
    while True:
        clear()
        invite_link = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Invite code: {Style.RESET_ALL}""")
        if not invite_link:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please, enter invite code\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
        server_lookup(invite_link)
        break