from scripts import thanos_port

def search(txt,lst):
    for i in range(len(lst)):
        if(txt==lst[i]):
            return True 
        else:
            pass
    return False


def run(url,thanos):
    if(search("deep",thanos)==True):
        if(search("port",thanos)==True):
            thanos_port.run(url,"deep")
    else:
        if(search("port",thanos)==True):
            thanos_port.run(url,"normal")
        