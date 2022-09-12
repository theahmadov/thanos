from rich.console import Console
from rich.style import Style
from rich.theme import Theme
from colorama import Fore
console = Console()

def version():
    with open("./version.txt","r") as f:
        version = f.read()
    return version

class config:
    ferror = "Unknown Error Occured while trying to run help command. Please try again later."
    version = version()
    help = f"""
Thanos {version}

-SCAN :
    port : python3 thanos.py [normal,port]example.com
    subdomain : python3 thanos.py [normal,sub]example.com
    directory : python3 thanos.py [normal,dir]example.com

-SAVE :
    save output : python3 thanos.py [normal,port,dir,sub]example.com

Update : python3 thanos.py update
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
    console.print(load_help(),style="markdown.code") #markdown.code
