from scripts import thanos_port
from scripts import thanos_sub
from scripts import thanos_dir
from scripts import thanos_rec
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
    ###############################
    #     Save mode : full        #
    ###############################
    if(save==False):
        if(thanos[0]=="x" or thanos[0]=="full"):
            thanos_port.run(url,"normal",False)
            thanos_sub.run(url,"normal",False)
            thanos_dir.run(url,"normal",False)

        else:
                ###############################
                #         mode : deep         #
                ###############################

            if(search("deep",thanos)==True):
                if(search("port",thanos)==True or search("portscan",thanos)==True): thanos_port.run(url,"deep",False)
                if(search("sub",thanos)==True or search("subdomain",thanos)==True): thanos_sub.run(url,"deep",False)
                if(search("dir",thanos)==True or search("directory",thanos)==True): thanos_dir.run(url,"deep",False)
                if(search("rec",thanos)==True or search("record",thanos)==True):    thanos_rec.run(url,False)
            else:
                
                ###############################
                #         mode : normal       #
                ###############################

                if(search("port",thanos)==True or search("portscan",thanos)==True): thanos_port.run(url,"normal",False)
                if(search("sub",thanos)==True or search("subdomain",thanos)==True): thanos_sub.run(url,"normal",False)
                if(search("dir",thanos)==True or search("directory",thanos)==True): thanos_dir.run(url,"normal",False)
                if(search("rec",thanos)==True or search("record",thanos)==True):    thanos_rec.run(url,False)
    else:
        
        ###############################
        #     Save mode : full        #
        ###############################
        output = ""
        if(thanos[0]=="x" or thanos[0]=="full"):
            output+=thanos_port.run(url,"normal",False)
            output+=thanos_sub.run(url,"normal",False)
            output+=thanos_dir.run(url,"normal",False)
            output+=thanos_rec.run(url,False)

        else:
            
            ###############################
            #     Save mode : deep        #
            ###############################
            if(search("deep",thanos)==True):
                if(search("port",thanos)==True or search("portscan",thanos)==True): output+=thanos_port.run(url,"deep",True)
                if(search("sub",thanos)==True or search("subdomain",thanos)==True): output+=thanos_sub.run(url,"deep",True)
                if(search("dir",thanos)==True or search("directory",thanos)==True): output+=thanos_dir.run(url,"deep",True)
                if(search("rec",thanos)==True or search("record",thanos)==True):    output+=thanos_rec.run(url,True)

            ###############################
            #     Save mode : normal      #
            ###############################

            else:
                if(search("port",thanos)==True or search("portscan",thanos)==True): output+=thanos_port.run(url,"normal",True)
                if(search("sub",thanos)==True or search("subdomain",thanos)==True): output+=thanos_sub.run(url,"normal",True)
                if(search("dir",thanos)==True or search("directory",thanos)==True): output+=thanos_dir.run(url,"normal",True)
                if(search("rec",thanos)==True or search("record",thanos)==True):    output+=thanos_rec.run(url,True)
        return output