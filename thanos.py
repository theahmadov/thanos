from rich.console import Console
from rich.style import Style
import optparse 
from datetime import datetime
from scripts.port_scan import thanos_port
from lib_error.check import check_error


console = Console()

class conf:
    bar = ['■', '█','▄','▌','▐']


def thanos_main(url,params):
    console.print("Thanos started succesfully. Checking some errors. Please wait some time...",style="green")
    check_report = check_error(url)
    console.print(f"Starting Thanos scan! Time : {datetime.now()}")
    
    thanos_port(url,"d")

if __name__ == '__main__':

    parser = optparse.OptionParser(f"thanos -u url")
    parser.add_option(" -u",dest = "url",type="string") # set url 
    parser.add_option("-p",dest = "port",type="string") # set url 
    (options,args) = parser.parse_args()
    
    url = options.url
    port = options.port
    
    
    thanos_main(url,port)
