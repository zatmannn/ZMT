import subprocess
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from colorama import Fore, init, Style
import os

init(autoreset=True)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def extract_image_info(image_path):
    image = Image.open(image_path)
    size = image.size
    width = image.width
    height = image.height
    img_format = image.format
    mode = image.mode
    palette = image.palette or "Unknown"
    is_animated = getattr(image, 'is_animated', False)
    frames = getattr(image, 'n_frames', 1)
    dpi = image.info.get('dpi') or 'Unknown'
    
    image_text = f"""
        [{Fore.BLUE} Image Information {Fore.WHITE}]
    {Fore.BLUE}> + {Fore.WHITE}Image path  :{Fore.LIGHTBLACK_EX} {image_path}
    {Fore.BLUE}> + {Fore.WHITE}Size        :{Fore.LIGHTBLACK_EX} {size}
    {Fore.BLUE}> + {Fore.WHITE}Width       :{Fore.LIGHTBLACK_EX} {width}
    {Fore.BLUE}> + {Fore.WHITE}Height      :{Fore.LIGHTBLACK_EX} {height}
    {Fore.BLUE}> + {Fore.WHITE}Format      :{Fore.LIGHTBLACK_EX} {img_format}
    {Fore.BLUE}> + {Fore.WHITE}Mode        :{Fore.LIGHTBLACK_EX} {mode}
    {Fore.BLUE}> + {Fore.WHITE}Palette     :{Fore.LIGHTBLACK_EX} {palette}
    {Fore.BLUE}> + {Fore.WHITE}Is animated :{Fore.LIGHTBLACK_EX} {is_animated}
    {Fore.BLUE}> + {Fore.WHITE}Frames      :{Fore.LIGHTBLACK_EX} {frames}
    {Fore.BLUE}> + {Fore.WHITE}DPI         :{Fore.LIGHTBLACK_EX} {dpi}
    """
    exif_data = image.getexif()
    lat, lon = "None", "None"
    
    if exif_data:
        gps_info = exif_data.get(0x8825)
        
        if gps_info:
            gps_info = {GPSTAGS.get(k, k): v for k, v in gps_info.items()}
            if "GPSLatitude" in gps_info and "GPSLongitude" in gps_info:
                def to_degrees(val):
                    d, m, s = val
                    return d + (m / 60.0) + (s / 3600.0)

                lat = to_degrees(gps_info["GPSLatitude"]) * (1 if gps_info["GPSLatitudeRef"] == "N" else -1)
                lon = to_degrees(gps_info["GPSLongitude"]) * (1 if gps_info["GPSLongitudeRef"] == "E" else -1)
        
        image_text += f"""{Fore.BLUE}> + {Fore.WHITE}Latitude    :{Fore.LIGHTBLACK_EX} {lat}
    {Fore.BLUE}> + {Fore.WHITE}Longitude   :{Fore.LIGHTBLACK_EX} {lon}\n"""
    else:
        image_text += f"""{Fore.BLUE}> + {Fore.WHITE}Latitude    :{Fore.LIGHTBLACK_EX} None
    {Fore.BLUE}> + {Fore.WHITE}Longitude   :{Fore.LIGHTBLACK_EX} None\n"""

    print(image_text)

    save = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Save results to file? (y/n): {Style.RESET_ALL}""").strip().lower()
    if save == "y":
        save_path = os.path.join(BASE_DIR, "exifdata.txt")
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(f"""Image Information

Image path  : {image_path}
Size        : {size}
Width       : {width}
Height      : {height}
Format      : {img_format}
Mode        : {mode}
Palette     : {palette}
Is animated : {is_animated}
Frames      : {frames}
Colors      : {colors}
DPI         : {dpi}
Latitude    : {lat}
Longitude   : {lon}
""")
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Results saved to '{save_path}'")
    elif save == "n":
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Results not saved.")
    else:
        print(f"{Fore.BLUE}> ! {Fore.WHITE}Invalid input. Results not saved.")

    input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to exit...")

def exifdata_main():
    while True:
        clear()
        try:
            image_path = input(f"""{Fore.BLUE}┌──({Fore.WHITE}root{Fore.BLUE}@{Fore.WHITE}ZMT{Fore.BLUE})-[{Fore.WHITE}ZMT{Fore.BLUE}]
└─{Fore.BLUE}> Image path: {Style.RESET_ALL}""").strip()
            if not image_path:
                print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Please, enter path to image\n")
                input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
                continue
            extract_image_info(image_path)
            
            break
        except FileNotFoundError:
            print(f"\n{Fore.BLUE}> ! {Fore.WHITE}Error: File not found\n")
            input(f"{Fore.BLUE}> ! {Fore.WHITE}Press Enter to restart...")
        