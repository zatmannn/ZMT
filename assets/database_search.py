from colorama import Fore, init, Style
import os
import time

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def database_check(search_text, encodings=("utf-8", "cp1251", "cp1252")):
    print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please wait, it may take some time...\n")
    directory = os.path.join(BASE_DIR, "database")
    found = False
    results = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            for encoding in encodings:
                try:
                    with open(file_path, "r", encoding=encoding) as file:
                        for line in file:
                            if search_text in line:
                                result = f"{line.strip()}\n"
                                print(f"{Fore.BLUE}> + {Fore.WHITE}Found in {filename}: {Fore.LIGHTBLACK_EX}{result}")
                                results.append(result)
                                found = True
                                time.sleep(1)
                    break
                except (UnicodeDecodeError, FileNotFoundError, IOError):
                    continue
    return found, results

def database_check_main():
    while True:
        clear()
        search_text = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Enter text to search: {Style.RESET_ALL}""")
        
        found, results = database_check(search_text)
        
        if not found:
            print(f"{Fore.BLUE}> ! {Fore.WHITE}The text is not found in the databases, or you do not have any databases")
        else:
            save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()

            if save == "y":
                save_path = os.path.join(BASE_DIR, "database_results.txt")
                with open(save_path, "w", encoding="utf-8") as file:
                    file.writelines(results)
                print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")
            elif save == "n":
                print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved")
            else:
                print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved")
            
        input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")
        break
