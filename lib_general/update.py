import os
from rich.console import Console
from rich.style import Style
import requests 
import time
from rich.progress import track
from rich.progress import Progress

console = Console()

def version():
    with open("./version.txt","r") as f:
        version = f.read()
    return version


class conf:
    bar = ['■', '█','▄','▌','▐']

def new_version():
    version = requests.get("https://raw.githubusercontent.com/thesaderror/thanos/main/version.txt").text 

def run():
    console.print(f"Updating Thanos! {version()} --> {new_version}",style="markdown.code")
    console.print(f"Update module just avaliable on Linux Operating Systems...",style="traceback.exc_type")
    os.system("cd ..")
    os.system("rm -rf thanos")
    os.system("git clone https://github.com/thesaderror/thanos")
    os.system("pip3 install -r requirements.txt")
    os.system("clear")
    with Progress() as progress:
        task = progress.add_task("[red]Downloading...", total=1000)

        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.01)
    console.print(f"\nThanos Already Updated! Current Version : {version()}",style="markdown.link")
    os.system("python3 thanos.py thanos")
