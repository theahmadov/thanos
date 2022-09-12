from rich.console import Console
from rich.style import Style
from datetime import datetime
import typer
import socket 
from lib_general.thanos_split import *
from lib_error.check import check_error
from lib_general import action
from lib_general import help
from lib_general import update

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
    if(code == "update" or code == "upgrade"):
            update.run()
    elif(code=="thanos" or code == "help"):
        help.help()
    else:
        thanos = thanos_split(code,"actions")
        if(action.search("save",thanos)==True):
            if(action.search("normal",thanos)==True):
                url = thanos_split(code,"url")
                out = ""
                ip = socket.gethostbyname(clear_http(url))
                if(action.search("deep",thanos)==True):
                    console.print(f"Starting 'deep' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")
                    out += f"\nStarting 'deep' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}"
                elif(action.search("normal",thanos)==True):
                    console.print(f"Starting 'normal' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")
                    out += f"\nStarting 'normal' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}"
                else:
                    console.print(f"Starting 'full' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")

                    out += f"\nStarting 'full' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}"

                check_report = check_error(url)
                out += action.run(url,thanos,True)
                with open("output.txt", "w") as output:
                    output.write(out)
                console.print(f"\nThanos scan report of {ip} saved to output.txt!",style="red")
        else:
            url = thanos_split(code,"url")

            ip = socket.gethostbyname(clear_http(url))
            if(action.search("deep",thanos)==True):
                console.print(f"Starting 'deep' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")
            elif(action.search("normal",thanos)==True):
                console.print(f"Starting 'normal' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")
            else:
                console.print(f"Starting 'full' Thanos scan to {ip} with actions : {thanos}! Time : {datetime.now()}")


            check_report = check_error(url)
            action.run(url,thanos,False)


if __name__ == "__main__":
    typer.run(thanos_main)
