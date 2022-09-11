from rich.console import Console
from rich.style import Style
import optparse 
from datetime import datetime
from scripts import thanos_port
from lib_error.check import check_error
import typer

console = Console()

class conf:
    bar = ['■', '█','▄','▌','▐']


def thanos_main(code: str):
    console.print("Thanos started succesfully. Checking some errors. Please wait some time...",style="green")
    check_report = check_error(code)
    console.print(f"Starting Thanos scan! Time : {datetime.now()}")
    
    thanos_port.scan(code,"normal") # Port Scan |deep-normal|



if __name__ == "__main__":
    typer.run(thanos_main)
