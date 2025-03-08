import requests
from colorama import Fore, init, Style
import os
import json
import datetime

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def reddit_parser(username):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
    }

    url = f'https://www.reddit.com/user/{username}/about.json'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        user_data = data['data']
        username = user_data['name']
        karma = user_data['total_karma']
        link_karma = user_data['link_karma']
        comment_karma = user_data['comment_karma']
        created_utc = user_data['created_utc']
        created_date = datetime.datetime.fromtimestamp(created_utc, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        is_verified = user_data.get('verified') or "No"
        subscribers = user_data.get('subscribers') or "0"
        awardee_karma = user_data.get('awardee_karma') or "0"
        awarder_karma = user_data.get('awarder_karma') or "0"

        results = f"""
          {Fore.WHITE}[ {Fore.BLUE}Reddit Parser Information{Fore.WHITE} ]
    {Fore.BLUE}> + {Fore.WHITE}Username        :{Fore.LIGHTBLACK_EX} {username}
    {Fore.BLUE}> + {Fore.WHITE}Total Karma     :{Fore.LIGHTBLACK_EX} {karma}
    {Fore.BLUE}> + {Fore.WHITE}Link Karma      :{Fore.LIGHTBLACK_EX} {link_karma}
    {Fore.BLUE}> + {Fore.WHITE}Comment Karma   :{Fore.LIGHTBLACK_EX} {comment_karma}
    {Fore.BLUE}> + {Fore.WHITE}Created On      :{Fore.LIGHTBLACK_EX} {created_date}
    {Fore.BLUE}> + {Fore.WHITE}Verified        :{Fore.LIGHTBLACK_EX} {is_verified}
    {Fore.BLUE}> + {Fore.WHITE}Subscribers     :{Fore.LIGHTBLACK_EX} {subscribers}
    {Fore.BLUE}> + {Fore.WHITE}Awardee Karma   :{Fore.LIGHTBLACK_EX} {awardee_karma}
    {Fore.BLUE}> + {Fore.WHITE}Awarder Karma   :{Fore.LIGHTBLACK_EX} {awarder_karma}
    """
        print(results)

        save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
        if save == "y":
            save_path = os.path.join(BASE_DIR, "reddit_parser.txt")
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"""Reddit Parser Information

Username      : {username}
Total Karma   : {karma}
Link Karma    : {link_karma}
Comment Karma : {comment_karma}
Created On    : {created_date}
Verified      : {is_verified}
Subscribers   : {subscribers}
Awardee Karma : {awardee_karma}
Awarder Karma : {awarder_karma}""")
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")
        
        elif save == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
            
        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")
            
    except requests.RequestException:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Error: This profile doesn't exist or an error occurred")
    
    input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")

def reddit_parser_main():
    while True:
        clear()
        username = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Username (without /u/): {Style.RESET_ALL}""")
        if not username:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please, enter username\n")    
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
        reddit_parser(username)
        break