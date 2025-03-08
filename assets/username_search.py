import re
import requests
from colorama import Fore, init, Style
import os
from googlesearch import search

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/91.0.4472.124 Safari/537.36"}

def username_search(nickname):
    print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please wait, it may take some time...\n")
    print(f"{Fore.WHITE}[ {Fore.BLUE}Username Search Results for: {nickname}{Fore.WHITE} ]\n")
    
    sites = {
        "Instagram": "https://www.instagram.com/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Twitter (X)": "https://www.x.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "YouTube": "https://www.youtube.com/@{}",
        "Telegram": "https://t.me/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "GitHub": "https://www.github.com/{}",
        "VK": "https://vk.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "DeviantArt": "https://www.deviantart.com/{}",
}

    
    found_results = []
    nickname_pattern = re.compile(rf"\b{re.escape(nickname)}\b", re.IGNORECASE)

    for site, url_template in sites.items():
        url = url_template.format(nickname)
        try:
            response = requests.get(url, headers=headers, timeout=10)
            status_code = response.status_code

            if status_code == 200:
                page_text = response.text.lower()
                found = bool(nickname_pattern.search(page_text))
                result = f"[{site}] Found: {url}"
                if found:
                    found_results.append(result)
                    print(f"{Fore.BLUE}+ >{Fore.WHITE} [{site} - {Fore.GREEN}OK{Fore.WHITE}]{Fore.LIGHTBLACK_EX} {url}")
                else:
                    print(f"{Fore.BLUE}+ >{Fore.WHITE} [{site} - {Fore.YELLOW}UNKNOWN{Fore.WHITE}]{Fore.LIGHTBLACK_EX} {url}")
            else:
                print(f"{Fore.BLUE}- >{Fore.WHITE} [{site} - {Fore.RED}BAD:{status_code}{Fore.WHITE}]")

        except requests.exceptions.Timeout:
            print(f"{Fore.BLUE}- >{Fore.WHITE} [{site} - {Fore.RED}TIMEOUT{Fore.WHITE}]")
        except requests.exceptions.ConnectionError:
            print(f"{Fore.BLUE}- >{Fore.WHITE} [{site} - {Fore.RED}CONNECTION ERROR{Fore.WHITE}]")
        except requests.exceptions.RequestException:
            print(f"{Fore.BLUE}- >{Fore.WHITE} [{site} - {Fore.RED}REQUEST EXCEPTION{Fore.WHITE}]")
        except Exception:
            print(f"{Fore.BLUE}- >{Fore.WHITE} [{site} - {Fore.RED}UNEXPECTED ERROR{Fore.WHITE}]")
    
    return found_results

def google_dork_search(dork):
    print(f"\n{Fore.WHITE}[ {Fore.BLUE}Google Dorks Search Results{Fore.WHITE} ]\n")
    
    dork_results = []
    
    try:
        for url in search(dork, num_results=10, timeout=5): 
            if not url.strip():
                continue
            try:    
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                status_code = response.status_code
                dork_results.append(url)
                print(f"{Fore.BLUE}+ >{Fore.WHITE} [{Fore.GREEN}OK{Fore.WHITE}] Found:{Fore.LIGHTBLACK_EX} {url}")
            except requests.RequestException:
                print(f"{Fore.BLUE}+ >{Fore.WHITE} [{Fore.YELLOW}INACCESSIBLE{Fore.WHITE}] Found:{Fore.LIGHTBLACK_EX} {url}")
                continue
        if not dork_results:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}No results found!\n")
    except Exception as e:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Error: {e}")
    
    return dork_results

def main_usernamesearch():
    while True:
        clear()
        
        nickname = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Username: {Style.RESET_ALL}""")
        
        if not nickname:
            print(f"\n{Fore.BLUE}! > {Fore.WHITE}Please, enter username\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
        
        results = username_search(nickname)
        
        extended_search = input(f"\n{Fore.BLUE}> ! {Fore.WHITE}Do you want an extended search with Google Dorks? (y/n): ").strip().lower()

        if extended_search == 'y':
            dork_query = f"+intext:{nickname} OR +inurl:{nickname}"
            dork_results = google_dork_search(dork_query)
            results.extend(dork_results)
        elif extended_search == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Skipping extended search with Google Dorks")
        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Skipping extended search with Google Dorks")
        
        save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()

        if save.lower() == 'y':
            filename = f"{nickname}_search_results.txt"
            file_path = os.path.join(BASE_DIR, filename)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"Username Search Results for: {nickname}\n")
                for result in results:
                    file.write(result + "\n")
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{file_path}'")
        
        
        elif save == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
            
        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")

        input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
    
        break