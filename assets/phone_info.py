from colorama import Fore, init, Style
from phonenumbers import parse, is_valid_number, number_type, PhoneNumberType, geocoder, carrier, format_number, PhoneNumberFormat
import phonenumbers
import os

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def phoneinfo(phone_number):
    try:
        parsed_number = parse(phone_number)
        country = geocoder.country_name_for_number(parsed_number, "en") or "Unknown"
        region = geocoder.description_for_number(parsed_number, "en") or "Unknown"
        operator = carrier.name_for_number(parsed_number, "en") or "Unknown"
        valid = is_valid_number(parsed_number)
        validity = "Valid" if valid else "Invalid"
        number_type_code = number_type(parsed_number)
        number_type_str = {
            PhoneNumberType.MOBILE: "Mobile",
            PhoneNumberType.FIXED_LINE: "Fixed Line",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed or Mobile",
            PhoneNumberType.VOIP: "VoIP",
            PhoneNumberType.TOLL_FREE: "Toll-Free",
            PhoneNumberType.PREMIUM_RATE: "Premium Rate"}.get(number_type_code) or "Unknown"
        intl_format = format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
        national_format = format_number(parsed_number, PhoneNumberFormat.NATIONAL)
        e164_format = format_number(parsed_number, PhoneNumberFormat.E164)
        whatsapp = f"https://wa.me/{e164_format}"
        telegram = f"https://t.me/{e164_format}"
        viber = f"https://viber.click/{e164_format}"

        phonetext = f"""
         {Fore.WHITE}[{Fore.BLUE} Phone Number Information {Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}Number          :{Fore.LIGHTBLACK_EX} {phone_number}
    {Fore.BLUE}> + {Fore.WHITE}Country         :{Fore.LIGHTBLACK_EX} {country}
    {Fore.BLUE}> + {Fore.WHITE}Region          :{Fore.LIGHTBLACK_EX} {region}
    {Fore.BLUE}> + {Fore.WHITE}Operator        :{Fore.LIGHTBLACK_EX} {operator}
    {Fore.BLUE}> + {Fore.WHITE}Validity        :{Fore.LIGHTBLACK_EX} {validity}
    {Fore.BLUE}> + {Fore.WHITE}Type            :{Fore.LIGHTBLACK_EX} {number_type_str}
    {Fore.BLUE}> + {Fore.WHITE}Intl. Format    :{Fore.LIGHTBLACK_EX} {intl_format}
    {Fore.BLUE}> + {Fore.WHITE}National Format :{Fore.LIGHTBLACK_EX} {national_format}
    {Fore.BLUE}> + {Fore.WHITE}E.164 Format    :{Fore.LIGHTBLACK_EX} {e164_format}

      {Fore.WHITE}[{Fore.BLUE} Check on Social Platforms {Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}WhatsApp : {Fore.LIGHTBLACK_EX}{whatsapp}
    {Fore.BLUE}> + {Fore.WHITE}Telegram : {Fore.LIGHTBLACK_EX}{telegram}
    {Fore.BLUE}> + {Fore.WHITE}Viber    : {Fore.LIGHTBLACK_EX}{viber}"""

        print(phonetext)

        save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
        if save == "y":
            save_path = os.path.join(BASE_DIR, "phone_info.txt")
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"""Phone Number Information

Number          : {phone_number}
Country         : {country}
Region          : {region}
Operator        : {operator}
Validity        : {validity}
Type            : {number_type_str}
Intl. Format    : {intl_format}
National Format : {national_format}
E.164 Format    : {e164_format}

Check on Social Platforms

WhatsApp : {whatsapp}
Telegram : {telegram}
Viber    : {viber}""")
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")

        elif save == "n":
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
            
        else:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")

        input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")

    except phonenumbers.phonenumberutil.NumberParseException:
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Error: invalid phone number format")
        input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")


def phone_main():
    while True:
        clear()
        phone_number = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Phone number: {Style.RESET_ALL}""")
        if not phone_number:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please, enter phone number\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
            continue
        phoneinfo(phone_number)
        break