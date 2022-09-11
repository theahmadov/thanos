import socket 
from rich.console import Console
from rich.style import StyleStack
console = Console()

def clear_http(url):
    if(url.startswith('http://')):
        clear = url.split('http://')
        return clear[1]
    else:
        clear = url.split('https://')
        return clear[1]


def thanos_port(url,selection):
    ip = socket.gethostbyname(clear_http(url))
    ports = [20,21,22,23,53,25,40,44,69,80,139,137,443,444,445,4444,8080, 8443]
    console.print("\tPort \tAction \tService")
    if selection == "deep":
        for port in range(0,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            check = s.connect_ex((ip,port))
            if(check==0):
                version = socket.getservbyport(port, "tcp")
                print(f"{port}    open    {version}")
            s.close()
    else:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            check = s.connect_ex((ip,port))
            if(check==0):
                version = socket.getservbyport(port, "tcp")
                print(f"\t{port}   \topen    \t{version}")
            s.close()