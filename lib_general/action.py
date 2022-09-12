from scripts import thanos_port
from scripts import thanos_sub
from scripts import thanos_dir
from rich.console import Console
from rich.style import StyleStack
console = Console()
def search(txt,lst):
    for i in range(len(lst)):
        if(txt==lst[i]):
            return True 
        else:
            pass
    return False


def run(url,thanos,save):
    if(save==False):
        if(thanos[0]=="x" or thanos[0]=="full"):
            thanos_port.run(url,"normal",False)
            thanos_sub.run(url,"normal",False)
            thanos_dir.run(url,"normal",False)

        else:
            if(search("deep",thanos)==True):
                if(search("port",thanos)==True):
                    thanos_port.run(url,"deep",False)
                if(search("sub",thanos)==True or search("subdomain",thanos)==True):
                    thanos_sub.run(url,"deep",False)
                if(search("dir",thanos)==True or search("directory",thanos)==True):
                    thanos_dir.run(url,"deep",False)
            else:
                if(search("port",thanos)==True):
                    thanos_port.run(url,"normal",False)
                if(search("sub",thanos)==True or search("subdomain",thanos)==True):
                    thanos_sub.run(url,"normal",False)
                if(search("dir",thanos)==True or search("directory",thanos)==True):
                    thanos_dir.run(url,"normal",False)
    else:
        output = ""
        if(thanos[0]=="x" or thanos[0]=="full"):
            
            output+=thanos_port.run(url,"normal",False)

            output+=thanos_sub.run(url,"normal",False)
            
            output+=thanos_dir.run(url,"normal",False)

        else:
            if(search("deep",thanos)==True):
                if(search("port",thanos)==True):
                    output+=thanos_port.run(url,"deep",True)
                if(search("sub",thanos)==True or search("subdomain",thanos)==True):
                    output+=thanos_sub.run(url,"deep",True)
                if(search("dir",thanos)==True or search("directory",thanos)==True):
                    output+=thanos_dir.run(url,"deep",True)
            else:
                if(search("port",thanos)==True):
                    
                    output+=thanos_port.run(url,"normal",True)
                    
                if(search("sub",thanos)==True or search("subdomain",thanos)==True):
        
                    output+=thanos_sub.run(url,"normal",True)

                if(search("dir",thanos)==True or search("directory",thanos)==True):
                    
                    output+=thanos_dir.run(url,"normal",True)
        return output