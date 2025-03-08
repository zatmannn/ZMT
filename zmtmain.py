from colorama import Fore, init, Style
import os
from assets import *

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = f"""{Fore.BLUE}
                        :::::::::   :::   ::: ::::::::::: 
                            :+:   :+:+: :+:+:    :+:      
                          +:+   +:+ +:+:+ +:+   +:+       
                        +#+    +#+  +:+  +#+   +#+        
                      +#+     +#+       +#+   +#+         
                    #+#      #+#       #+#   #+#          
                  ######### ###       ###   ###           
                       
                        Zatman's Multi-Tool"""
def main():
    while True:
        clear()
        menu = f"""                          [{Fore.BLUE} OSINT  Tools {Style.RESET_ALL}]

                          [{Fore.BLUE} Social Media {Style.RESET_ALL}]

    {Fore.BLUE}> 01{Fore.WHITE} TikTok Parser              {Fore.LIGHTBLACK_EX}# Retrieve information from a TikTok account
    {Fore.BLUE}> 02{Fore.WHITE} Reddit Parser              {Fore.LIGHTBLACK_EX}# Retrieve information from a Reddit account
    {Fore.BLUE}> 03{Fore.WHITE} GitHub Parser              {Fore.LIGHTBLACK_EX}# Retrieve information from a GitHub account
    {Fore.BLUE}> 04{Fore.WHITE} Username Search            {Fore.LIGHTBLACK_EX}# Search for accounts (and more) by username
    {Fore.BLUE}> 05{Fore.WHITE} Discord Token Information  {Fore.LIGHTBLACK_EX}# Retrieve details about a Discord token
    {Fore.BLUE}> 06{Fore.WHITE} Discord Invite Lookup      {Fore.LIGHTBLACK_EX}# Retrieve details about a Discord invite

                          {Fore.WHITE}[{Fore.BLUE} Lookup Tools {Style.RESET_ALL}]

    {Fore.BLUE}> 07{Fore.WHITE} Google Dork Search         {Fore.LIGHTBLACK_EX}# Perform a Google Dork search
    {Fore.BLUE}> 08{Fore.WHITE} WHOIS Domain Search        {Fore.LIGHTBLACK_EX}# Retrieve domain information
    {Fore.BLUE}> 09{Fore.WHITE} Phone Info                 {Fore.LIGHTBLACK_EX}# Get details about a phone number
    {Fore.BLUE}> 10{Fore.WHITE} IP Info                    {Fore.LIGHTBLACK_EX}# Get details about an IP address
    {Fore.BLUE}> 11{Fore.WHITE} Extract EXIF Data          {Fore.LIGHTBLACK_EX}# Extract EXIF data from an image
    {Fore.BLUE}> 12{Fore.WHITE} BIN Checker                {Fore.LIGHTBLACK_EX}# Get information about a BIN
    {Fore.BLUE}> 13{Fore.WHITE} Database Search            {Fore.LIGHTBLACK_EX}# Search for information in databases (txt, csv, cvv)
    {Fore.LIGHTBLACK_EX}#-----------------------------------------------------------------------------------#
    {Fore.BLUE}> 99{Fore.WHITE} Back to main menu

    {Fore.LIGHTBLACK_EX}# More tools coming soon...
"""
        print(logo)
        print(menu)
        choice = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> {Fore.WHITE}""")
        if choice == "1":
            tiktokparser_main()
        elif choice == "2":
            reddit_parser_main()
        elif choice == "3":
            github_parser_main()
        elif choice == "4":
            main_usernamesearch()
        elif choice == "5":
            token_main()
        elif choice == "6":
            server_lookup_main()
        elif choice == "7":
            dorks_main()
        elif choice == "8":
            domain_main()
        elif choice == "9":
            phone_main()
        elif choice == "10":
            ip_main()
        elif choice == "11":
            exifdata_main()
        elif choice == "12":
            check_bin_main()
        elif choice == "13":
            database_check_main()
        elif choice == "99":
            break
        else:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Invalid input\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
main()
