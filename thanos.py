from rich.console import Console
from rich.style import Style
import optparse 
from datetime import datetime
import typer
import socket 
from thanos_split import *
from lib_error.check import check_error
from lib_general import action

console = Console()

def clear_http(url):
    if(url.startswith('http://')):
        clear = url.split('http://')
        return clear[1]
    else:
        clear = url.split('https://')
        return clear[1]

class conf:
    bar = ['■', '█','▄','▌','▐']

def thanos_main(code: str):
    url = thanos_split(code,"url")
    thanos = thanos_split(code,"actions")

    ip = socket.gethostbyname(clear_http(url))
    console.print("Thanos started succesfully. Checking some errors. Please wait some time...",style="green")
    check_report = check_error(url)
    console.print(f"Starting Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")

    action.run(url,thanos)



if __name__ == "__main__":
    typer.run(thanos_main)