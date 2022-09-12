import urllib
from rich.console import Console
from rich.style import StyleStack
from lib_general import ishttp

console = Console()
class wordlist:
    deep = "./wordlist/subdomain_deep.txt"
    normal = "./wordlist/subdomain_normal.txt"

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

def run(url,mode,save):
    if save==False:
        console.print("\nThanos Report [Subdomain]\n",style="blue on white")
        http = ishttp.run(clear_http(url))
        if mode=="deep":
            deep = []
            with open(wordlist.deep,"r") as f:
                deep = f.read().splitlines()
            for sub in deep:
                try:
                    connect = urllib.request.urlopen(http+sub+"."+clear_http(url))
                    console.print(f"({sub}) {http}{sub}.{clear_http(url)}")
                except:
                    pass
            
        elif mode=="normal":
            deep = []
            with open(wordlist.normal,"r") as f:
                deep = f.read().splitlines()
            for sub in deep:
                try:
                    connect = urllib.request.urlopen(http+sub+"."+clear_http(url))
                    console.print(f"({sub}) {http}{sub}.{clear_http(url)}")
                except:
                    pass
    else:
        console.print("\nThanos Report [Subdomain]\n",style="blue on white")
        output = ""
        output += "\nThanos Report [Subdomain]\n"
        http = ishttp.run(clear_http(url))
        if mode=="deep":
            deep = []
            with open(wordlist.deep,"r") as f:
                deep = f.read().splitlines()
            for sub in deep:
                try:
                    connect = urllib.request.urlopen(http+sub+"."+clear_http(url))
                    output += f"\n({sub}) {http}{sub}.{clear_http(url)}"
                    console.print(f"({sub}) {http}{sub}.{clear_http(url)}")
                except:
                    pass
            
        elif mode=="normal":
            deep = []
            with open(wordlist.normal,"r") as f:
                deep = f.read().splitlines()
            for sub in deep:
                try:
                    connect = urllib.request.urlopen(http+sub+"."+clear_http(url))
                    output += f"\n({sub}) {http}{sub}.{clear_http(url)}"
                    console.print(f"({sub}) {http}{sub}.{clear_http(url)}")
                except:
                    pass
        return output