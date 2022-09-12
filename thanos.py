from rich.console import Console
from rich.style import Style
from datetime import datetime
import typer
import socket 
from lib_general.thanos_split import *
from lib_error.check import check_error
from lib_general import action
from lib_general import help

console = Console()

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

class conf:
    bar = ['■', '█','▄','▌','▐']


def thanos_main(code: str):
    
    if(help.check(code)==False):
        url = thanos_split(code,"url")
        thanos = thanos_split(code,"actions")

        ip = socket.gethostbyname(clear_http(url))
        if(action.search("deep",thanos)==True):
            console.print(f"Starting 'deep' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")
        elif(action.search("normal",thanos)==True):
            console.print(f"Starting 'normal' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")
        else:
            console.print(f"Starting 'full' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")


        check_report = check_error(url)
        action.run(url,thanos)
    else:
        help.help()


if __name__ == "__main__":
    typer.run(thanos_main)