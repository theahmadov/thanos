from rich.console import Console
from rich.style import Style
from rich.theme import Theme
from colorama import Fore
console = Console()

class config:
    ferror = "Unknown Error Occured while trying to run help command. Please try again later."
    version = 1.1
    help = f"""
Thanos {version}

SCAN :
    port : python3 thanos.py [deep,port]example.com
    subdomain : python3 thanos.py [deep,sub]example.com
    directory : python3 thanos.py [deep,dir]example.com

Full : python3 thanos.py [x]example.com
"""
def check(code):
    if((code == "help") or (code == "thanos")):
        return True
    else:
        return False


def load_help():
    try:
        return config.help
    except:
        return config.ferror


def help():
    print(load_help()) #markdown.code
