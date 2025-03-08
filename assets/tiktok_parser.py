from bs4 import BeautifulSoup
import requests
from colorama import Fore, init, Style
import os
import json

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tiktok_parser(username):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
    }

    url = f'https://www.tiktok.com/@{username}'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Error: {e}")

    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', id='__UNIVERSAL_DATA_FOR_REHYDRATION__', type='application/json')

    try:
        json_data = json.loads(script_tag.string)
        user_data = json_data['__DEFAULT_SCOPE__']['webapp.user-detail']
        user_info = user_data['userInfo']['user']
        stats = user_data['userInfo']['stats']
        share_meta = user_data['shareMeta']
        userid = user_info['id']
        uniqueid = user_info['uniqueId']
        nickname = user_info['nickname']
        bio = user_info['signature'].replace('\n', ' ')
        privacy = user_info['privateAccount']
        region = user_info['region']
        language = user_info['language']
        desc = share_meta['desc']
        title = share_meta['title']
        vidcount = stats['videoCount']
        likecount = stats['heartCount']
        followcount = stats['followingCount']
        followercount = stats['followerCount']
        results = f"""
          {Fore.WHITE}[ {Fore.BLUE}TikTok Parser Information{Fore.WHITE} ]
    {Fore.BLUE}> + {Fore.WHITE}Username        :{Fore.LIGHTBLACK_EX} {username}
    {Fore.BLUE}> + {Fore.WHITE}ID              :{Fore.LIGHTBLACK_EX} {userid}
    {Fore.BLUE}> + {Fore.WHITE}Unique ID       :{Fore.LIGHTBLACK_EX} {uniqueid}
    {Fore.BLUE}> + {Fore.WHITE}Region          :{Fore.LIGHTBLACK_EX} {region}
    {Fore.BLUE}> + {Fore.WHITE}Language        :{Fore.LIGHTBLACK_EX} {language}
    {Fore.BLUE}> + {Fore.WHITE}Bio             :{Fore.LIGHTBLACK_EX} {bio}
    {Fore.BLUE}> + {Fore.WHITE}Description     :{Fore.LIGHTBLACK_EX} {desc}
    {Fore.BLUE}> + {Fore.WHITE}Title           :{Fore.LIGHTBLACK_EX} {title}
    {Fore.BLUE}> + {Fore.WHITE}Video Count     :{Fore.LIGHTBLACK_EX} {vidcount}
    {Fore.BLUE}> + {Fore.WHITE}Like Count      :{Fore.LIGHTBLACK_EX} {likecount}
    {Fore.BLUE}> + {Fore.WHITE}Following Count :{Fore.LIGHTBLACK_EX} {followcount}
    {Fore.BLUE}> + {Fore.WHITE}Follower Count  :{Fore.LIGHTBLACK_EX} {followercount}
    {Fore.BLUE}> + {Fore.WHITE}Private Account :{Fore.LIGHTBLACK_EX} {privacy}
    """
        print(results)
    
        save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
        if save == "y":
            save_path = os.path.join(BASE_DIR, "tiktok_parser.txt")
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"""TikTok Parser Information

Username        : {username}
ID              : {userid}
Unique ID       : {uniqueid}
Region          : {region}
Language        : {language}
Bio             : {bio}
Description     : {desc}
Title           : {title}
Video Count     : {vidcount}
Like Count      : {likecount}
Following Count : {followcount}
Follower Count  : {followercount}
Private Account : {privacy}""")
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")
            
        elif save == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
            
        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")

    except (json.JSONDecodeError, KeyError):
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Error: This profie doesn't exists")
    input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")

def tiktokparser_main():
    while True:
        clear()
        username = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Username (without @): {Style.RESET_ALL}""")
        if not username:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please, enter username\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
        tiktok_parser(username)
        break