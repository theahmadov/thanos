from rich.console import Console
from rich.style import StyleStack
import requests

console = Console()
class error:
    code = {
    100 : ('Could not found <url>...', 'Could not found url to start scan. Please use --u <url> parameter to set url.'),
    101 : ('Try to connect internet...', 'Internet error occured. Try to connect internet and try again.'),
    102 : ('Url adress could not resolved...', 'Url adress could not resolved. Try to use http:// or https:// methods , also use correct url.')
    }

class config:
    conf_style = {
        100 : "bold"
    }
    connect = "https://google.com/"

def print_error(error_code):
    return f"""
    thanos error_code : {error_code}
    Error : \t{error.code[error_code][0]}
    Desc. : \t{error.code[error_code][1]}
    """

def check_http(url):

    if(url.startswith("http") or url.startswith("https")):            
        try:
            connect = requests.get(url)
        except:
            return False 
        return True
    else:
        return False


def internet():
    try:
        connect = requests.get(config.connect)
    except:
        return False
    return True

def check_error(url):
    console.print("Checking internet connection...")
    if(internet() == False):
        console.print(print_error(101), style=config.conf_style[100])
    console.print("Checking url adress...")
    if(url==None):
        console.print(print_error(100), style=config.conf_style[100])
    if(check_http(url)==False):
        console.print(print_error(102), style=config.conf_style[100])
