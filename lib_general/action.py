from scripts import thanos_port

def search(txt,lst):
    for i in range(len(txt)):
        if(lst[i]==txt):
            return True 
    return False


def run(url,thanos):
    if(search("deep",thanos)==True):
        if(search("port",thanos)==True):
            thanos_port.run(url,"deep")