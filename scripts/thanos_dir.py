import urllib
from rich.console import Console
from rich.style import StyleStack
from lib_general import ishttp

console = Console()

class wordlist:
    deep = "./wordlist/directory_deep.txt"
    normal = "./wordlist/directory_normal.txt"

def clear_http(url):
    if(url.startswith('http://')):
        clear = url.split('http://')
        return clear[1]
    else:
        try:
            clear = url.split('https://')
            return clear[1]
        except:
            return url

def run(url,mode):
    console.print("\nThanos Report [Directory]\n",style="blue on white")
    http = ishttp.run(clear_http(url))
    if mode=="deep":
        deep = []
        with open(wordlist.deep,"r") as f:
            deep = f.read().splitlines()
        for dr in deep:
            try:
                connect = urllib.request.urlopen(http+clear_http(url)+"/"+dr)
                console.print(f"({dr}) {http}{clear_http(url)}/{dr}")
            except:
                pass
        
    elif mode=="normal":
        normal = []
        with open(wordlist.normal,"r") as f:
            normal = f.read().splitlines()
        for dr in normal:
            try:
                connect = urllib.request.urlopen(http+clear_http(url)+"/"+dr)
                console.print(f"({dr}) {http}{clear_http(url)}/{dr}")
            except:
                pass