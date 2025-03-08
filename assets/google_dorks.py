import requests
from colorama import Fore, init, Style
import os
from googlesearch import search

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def google_dork_search(dork):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"}

    print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please wait, it may take some time...\n")
    try:
        urls = []
        for url in search(dork):
            if not url.strip():
                continue
            try:    
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                urls.append(url)
                print(f"{Fore.BLUE}+ >{Fore.WHITE} [{Fore.GREEN}OK{Fore.WHITE}] Found:{Fore.LIGHTBLACK_EX} {url}")
            except requests.RequestException:
                print(f"{Fore.BLUE}+ >{Fore.WHITE} [{Fore.YELLOW}INACCESSIBLE{Fore.WHITE}] Found:{Fore.LIGHTBLACK_EX} {url}")
                continue
        if not urls:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}No results found!\n")

        save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
            
        if save == "y":
            save_path = os.path.join(BASE_DIR, "google_dork.txt")
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"Search Results\n")
                for url in urls:
                    file.write(f"{url}\n\n")
                print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")
        elif save == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")

    except Exception as e:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Error: {e}")

    input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")

def dorks_main():
    while True:
        clear()
        dork = input(f"""\n{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Enter the search query: {Style.RESET_ALL}""").strip()
        google_dork_search(dork)
        break
