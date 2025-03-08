from colorama import Fore, init, Style
import requests
import os

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ipinfo(ip, ip_choice):
    if ip_choice == "1":
        url = f"https://ipwhois.app/json/"
    elif ip_choice == "2":
        url = f"https://ipwhois.app/json/{ip}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data.get('ip') is None:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Invalid IP Address. No data found for the given IP.\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            return

        ip_address = data.get('ip', "None")
        ip_type = data.get('type', "None")
        country_phone = data.get('country_phone', "None")
        city = data.get('city', "None")
        asn = data.get('asn', "None")
        region = data.get('region', "None")
        country = data.get('country', "None")
        continent = data.get('continent', "None")
        postal = data.get('postal', "None")
        org = data.get('org', "None")
        lat = data.get('latitude', "None")
        lon = data.get('longitude', "None")
        timezone = data.get('timezone', "None")
        currency = data.get('currency', "None")

        ip_details = f"""
          {Fore.WHITE}[{Fore.BLUE}IP Information{Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}IP Address :{Fore.LIGHTBLACK_EX} {ip_address}
    {Fore.BLUE}> + {Fore.WHITE}IP Type    :{Fore.LIGHTBLACK_EX} {ip_type}

       {Fore.WHITE}[{Fore.BLUE}Location Information{Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}City        :{Fore.LIGHTBLACK_EX} {city}
    {Fore.BLUE}> + {Fore.WHITE}Region      :{Fore.LIGHTBLACK_EX} {region}
    {Fore.BLUE}> + {Fore.WHITE}Country     :{Fore.LIGHTBLACK_EX} {country}
    {Fore.BLUE}> + {Fore.WHITE}Continent   :{Fore.LIGHTBLACK_EX} {continent}
    {Fore.BLUE}> + {Fore.WHITE}Postal Code :{Fore.LIGHTBLACK_EX} {postal}
    {Fore.BLUE}> + {Fore.WHITE}Latitude    :{Fore.LIGHTBLACK_EX} {lat}
    {Fore.BLUE}> + {Fore.WHITE}Longitude   :{Fore.LIGHTBLACK_EX} {lon}
    {Fore.BLUE}> + {Fore.WHITE}Timezone    :{Fore.LIGHTBLACK_EX} {timezone}

       {Fore.WHITE}[{Fore.BLUE}Network Information{Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}ASN :{Fore.LIGHTBLACK_EX} {asn}
    {Fore.BLUE}> + {Fore.WHITE}ORG :{Fore.LIGHTBLACK_EX} {org}

      {Fore.WHITE}[{Fore.BLUE}Additional Information{Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}Currency      :{Fore.LIGHTBLACK_EX} {currency}
    {Fore.BLUE}> + {Fore.WHITE}Country Phone :{Fore.LIGHTBLACK_EX} {country_phone}
"""
        print(ip_details)

        save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
        if save == "y":
            save_path = os.path.join(BASE_DIR, "ip_info.txt")
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"""IP Information

IP Address : {ip_address}
IP Type    : {ip_type}

Location Information

City        : {city}
Region      : {region}
Country     : {country}
Continent   : {continent}
Postal Code : {postal}
Latitude    : {lat}
Longitude   : {lon}
Timezone    : {timezone}

Network Information

ASN         : {asn}
ORG         : {org}

Additional Information

Currency      : {currency}
Country Phone : {country_phone}
""")
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")

        elif save == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")

        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")

    except requests.exceptions.Timeout:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Request timed out. Please try again later")
    except requests.exceptions.ConnectionError:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Connection error")
    except requests.exceptions.HTTPError as e:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}HTTP error: {e.response.status_code}")
    except Exception as e:
        print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Error: {e}")
    input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")


def ip_main():
    while True:
        clear()
        print(f"{Fore.BLUE}    > 01 {Fore.WHITE}Check your IP Address\n{Fore.BLUE}    > 02 {Fore.WHITE}Check other IP Address\n{Fore.LIGHTBLACK_EX}    #----------------------------------------------------#\n{Fore.BLUE}    > 99 {Fore.WHITE}Exit\n")

        ip_choice = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> {Style.RESET_ALL}""")
        if ip_choice == "1":
            clear()
            ipinfo(None, ip_choice)
        elif ip_choice == "2":
            clear()
            ip = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> IP: {Style.RESET_ALL}""")
            if not ip:
                print(f"\n{Fore.BLUE}! > {Fore.WHITE}Please, enter IP Adress\n")
                input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
                continue
            ipinfo(ip, ip_choice)
        elif ip_choice == "99":
            break
        else:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Invalid input\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue