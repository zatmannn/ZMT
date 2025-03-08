from colorama import Fore, init, Style
import os
import whois
import requests
import socket

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def domain_date(date):
    if isinstance(date, list):
        date = date[0]
    return date.strftime("%Y-%m-%d") if date else "Unknown"

def reverse_ip_lookup(ip):
    try:
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Performing Reverse IP Lookup...")
        hostnames = socket.gethostbyaddr(ip)
        return hostnames[1] if hostnames else ["No domains found"]
    except socket.herror:
        return ["Reverse lookup failed"]

def domain_info(domain_url):
    print(f"{Fore.BLUE}> ! {Fore.WHITE}Please wait, it may take some time...\n")
    try:
        domain_data = whois.whois(domain_url)
        name = domain_data.domain_name
        registrar = domain_data.registrar
        create_date = domain_date(domain_data.creation_date) or 'Unknown'
        exp_date = domain_date(domain_data.expiration_date) or 'Unknown'
        last_upd = domain_date(domain_data.updated_date) or 'Unknown'
        registrar_name = domain_data.registrant_name or 'Private'
        registrar_email = domain_data.registrant_email or 'Private'
        registrant_country = domain_data.registrant_country  or 'Unknown'
        admin_name = domain_data.admin_name or 'Private'
        admin_email = domain_data.admin_email or 'Private'
        tech_name = domain_data.tech_name or 'Private'
        tech_email = domain_data.tech_email or 'Private'
        name_servers = domain_data.name_servers
        city = domain_data.city or 'Unknown'
        address = domain_data.address or 'Unknown'
        zipcode = domain_data.zipcode or 'Unknown'
        country = domain_data.country or 'Unknown'
        whois_text =f"""
         [{Fore.BLUE} WHOIS Information {Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}Domain             :{Fore.LIGHTBLACK_EX} {name}
    {Fore.BLUE}> + {Fore.WHITE}Registrar          :{Fore.LIGHTBLACK_EX} {registrar}
    {Fore.BLUE}> + {Fore.WHITE}Creation Date      :{Fore.LIGHTBLACK_EX} {create_date}
    {Fore.BLUE}> + {Fore.WHITE}Expiration Date    :{Fore.LIGHTBLACK_EX} {exp_date}
    {Fore.BLUE}> + {Fore.WHITE}Last Updated       :{Fore.LIGHTBLACK_EX} {last_upd}
    {Fore.BLUE}> + {Fore.WHITE}Registrant Name    :{Fore.LIGHTBLACK_EX} {registrar_name}
    {Fore.BLUE}> + {Fore.WHITE}Registrant Email   :{Fore.LIGHTBLACK_EX} {registrar_email}
    {Fore.BLUE}> + {Fore.WHITE}Registrant Country :{Fore.LIGHTBLACK_EX} {registrant_country}
    {Fore.BLUE}> + {Fore.WHITE}Admin Name         :{Fore.LIGHTBLACK_EX} {admin_name}
    {Fore.BLUE}> + {Fore.WHITE}Admin Email        :{Fore.LIGHTBLACK_EX} {admin_email}
    {Fore.BLUE}> + {Fore.WHITE}Tech Name          :{Fore.LIGHTBLACK_EX} {tech_name}
    {Fore.BLUE}> + {Fore.WHITE}Tech Email         :{Fore.LIGHTBLACK_EX} {tech_email}
    {Fore.BLUE}> + {Fore.WHITE}Name Servers       :{Fore.LIGHTBLACK_EX} {name_servers}
    {Fore.BLUE}> + {Fore.WHITE}City               :{Fore.LIGHTBLACK_EX} {city}
    {Fore.BLUE}> + {Fore.WHITE}Address            :{Fore.LIGHTBLACK_EX} {address}
    {Fore.BLUE}> + {Fore.WHITE}Zipcode            :{Fore.LIGHTBLACK_EX} {zipcode}
    {Fore.BLUE}> + {Fore.WHITE}Country            :{Fore.LIGHTBLACK_EX} {country}
        """

        print(whois_text)

    except Exception as e:
        print(f"{Fore.BLUE}> ! {Fore.WHITE} Error: {e}")

    try:
        ip = socket.gethostbyname(domain_url) or 'Unknown'
        url = f"https://ipwhois.app/json/{ip}"
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        ip_address = response.get('ip')
        ip_type = response.get('type')
        country_phone = response.get('country_phone')
        city = response.get('city') or "None"
        asn = response.get('asn') or "None"
        region = response.get('region') or "None"
        country = response.get('country') or "None"
        continent = response.get('continent') or "None"
        postal = response.get('postal') or "None"
        org = response.get('org') or "None"
        lat = response.get('latitude') or "None"
        lon = response.get('longitude') or "None"
        timezone = response.get('timezone') or "None"
        currency = response.get('currency') or "None"
        ip_text = f"""
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
        print(ip_text)

    except socket.gaierror:
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Unable to get IP address")
        

    save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()

    if save == "y":
        save_path = os.path.join(BASE_DIR, "WHOIS_info.txt")
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(f"""WHOIS Information

Domain             : {name}
Registrar          : {registrar}
Creation Date      : {create_date}
Expiration Date    : {exp_date}
Last Updated       : {last_upd}
Registrant Name    : {registrar_name}
Registrant Email   : {registrar_email}
Registrant Country : {registrant_country}
Admin Name         : {admin_name}
Admin Email        : {admin_email}
Tech Name          : {tech_name}
Tech Email         : {tech_email}
Name Servers       : {name_servers}
City               : {city}
Address            : {address}
Zipcode            : {zipcode}
Country            : {country}""")
            if ip != 'Unknown':
                file.write(f"""
IP Information

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

ASN : {asn}
ORG : {org}

Additional Information

Currency      : {currency}
Country Phone : {country_phone}
    """)
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")

    elif save == "n":
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
            
    else:
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")

    input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")



def domain_main():
    while True:
        clear()
        domain_url = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> URL: {Style.RESET_ALL}""")
        if not domain_url:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please, enter URL\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
        domain_info(domain_url)
        break