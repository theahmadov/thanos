from rich.console import Console
from rich.style import Style
import optparse 
from lib_error.check import check_error
from datetime import datetime

console = Console()

class conf:
    bar = ['■', '█','▄','▌','▐']


def thanos_main(url):
    console.print("Thanos started succesfully. Checking some errors. Please wait some time...",style="green")
    check_report = check_error(url)
    console.print(f"Starting Thanos scan! Time : {datetime.now()}")
if __name__ == '__main__':

    parser = optparse.OptionParser(f"thanos -u url")
    parser.add_option("-u",dest = "url",type="string") # set url 
    (options,args) = parser.parse_args()
    
    url = options.url
    
    
    thanos_main(url)
