from scripts import thanos_port
from scripts import thanos_sub
from scripts import thanos_dir
def search(txt,lst):
    for i in range(len(lst)):
        if(txt==lst[i]):
            return True 
        else:
            pass
    return False


def run(url,thanos):
    if(thanos[0]=="x" or thanos[0]=="full"):
        thanos_port.run(url,"normal")
        thanos_sub.run(url,"normal")
        thanos_dir.run(url,"normal")

    else:
        if(search("deep",thanos)==True):
            if(search("port",thanos)==True):
                thanos_port.run(url,"deep")
            if(search("sub",thanos)==True or search("subdomain",thanos)==True):
                thanos_sub.run(url,"deep")
            if(search("dir",thanos)==True or search("directory",thanos)==True):
                thanos_dir.run(url,"deep")
        else:
            if(search("port",thanos)==True):
                thanos_port.run(url,"normal")
            if(search("sub",thanos)==True or search("subdomain",thanos)==True):
                thanos_sub.run(url,"normal")
            if(search("dir",thanos)==True or search("directory",thanos)==True):
                thanos_dir.run(url,"normal")