import requests
from colorama import Fore, init, Style
import os

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_bin(bin_number):
    url = f"https://lookup.binlist.net/{bin_number}"
    
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if "error" not in data:
            scheme = data.get("scheme") or "Not found"
            card_type = data.get("type") or "Not found"
            brand = data.get("brand") or "Not found"
            bank = data.get("bank", {}).get("name") or "Not found"
            country = data.get("country", {}).get("name") or "Not found"
            lat = data.get("country", {}).get("latitude") or "Not found"
            lon = data.get("country", {}).get("latitude") or "Not found"
            bin_text = f"""
      [{Fore.BLUE} BIN Checker information {Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}Scheme    :{Fore.LIGHTBLACK_EX} {scheme}
    {Fore.BLUE}> + {Fore.WHITE}Type      :{Fore.LIGHTBLACK_EX} {card_type}
    {Fore.BLUE}> + {Fore.WHITE}Brand     :{Fore.LIGHTBLACK_EX} {brand}
    {Fore.BLUE}> + {Fore.WHITE}Bank      :{Fore.LIGHTBLACK_EX} {bank}
    {Fore.BLUE}> + {Fore.WHITE}Counrty   :{Fore.LIGHTBLACK_EX} {country}
    {Fore.BLUE}> + {Fore.WHITE}Latitude  :{Fore.LIGHTBLACK_EX} {lat}
    {Fore.BLUE}> + {Fore.WHITE}Longitude :{Fore.LIGHTBLACK_EX} {lon}
            """
            print(bin_text)
        else:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Error: Invalid BIN or data not found")
        save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
        if save == "y":
            save_path = os.path.join(BASE_DIR, "bin_checker.txt")
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"""BIN Checker information
                
Scheme    : {scheme}
Type      : {card_type}
Brand     : {brand}
Bank      : {bank}
Counrty   : {country}
Latitude  : {lat}
Longitude : {lon}""")
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")
        
        elif save == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
        
        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")
    except requests.exceptions.RequestException:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Error: This BIN doesn't exist or an error occurred")

    input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")

def check_bin_main():
    while True:
        clear()
        bin_number = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> BIN: {Style.RESET_ALL}""")
        if not bin_number:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please, enter BIN\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
        check_bin(bin_number)
        break

