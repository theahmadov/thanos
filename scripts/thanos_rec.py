from seleniumwire import webdriver
import socket 
from rich.console import Console
from rich.style import StyleStack
from lib_general import ishttp
import time 
from sys import platform

console = Console()

def clear_http(url):
    if(url.startswith('http://')):
        clear = url.split('http://')
        return clear[1]
    else:
        try:
            clear = url.split('https://')
            return clear[1]
        except:
            return url

def clear_tld(url):
    sp_dot = url.split('.')
    return sp_dot[0]

def run(url,save):
    output = ""
    if(platform == "win32" or platform == "win64"):
        if(save==False):
            console.print("\nThanos Report [Record]",style="blue on white")
            time.sleep(1)
            console.print("""
            Recording...
            [
                Webdriver : [FireFox]...
            ]""",style="red")
            driver = webdriver.Firefox(executable_path='./drivers/geckodriver.exe')
            driver.get(url)
            free_tld = clear_tld(clear_http(url))
            console.print(f"\nExtracted links :\n",style="blue on white")
            num=1
            for request in driver.requests:
                if free_tld in request.url:
                    console.print(f"[{num}] {request.url}",style="blue on yellow")
                    num+=1

        else:
            console.print("\nThanos Report [Record]",style="blue on white")
            output += "\nThanos Report [Record]"
            time.sleep(1)
            console.print("""
            Recording...
            [
                Webdriver : [FireFox]...
            ]""",style="red")
            output += """\n
            Recording...
            [
                Webdriver : [FireFox]...
            ]\n"""
            driver = webdriver.Firefox(executable_path='./drivers/geckodriver.exe')
            driver.get(url)
            free_tld = clear_tld(clear_http(url))
            console.print(f"\nExtracted links :\n",style="blue on white")
            output += f"\nExtracted links :\n"
            num = 1
            for request in driver.requests:
                if free_tld in request.url:
                    console.print(f"[{num}] {request.url}",style="blue on yellow")
                    output+=f"\n[{num}] {str(request.url)}"
                    num+=1
            return output
    else:
        console.print("[x] Your operating system does not support Thanos record module! Please wait updates or try another commands... [python thanos.py thanos]",style="red")
        # if(save==False):
        #     console.print("\nThanos Report [Record]",style="blue on white")
        #     time.sleep(1)
        #     console.print("""
        #     Recording...
        #     [
        #         Webdriver : [FireFox]...
        #     ]""",style="red")
        #     driver = webdriver.Firefox()
        #     driver.get(url)
        #     free_tld = clear_tld(clear_http(url))
        #     console.print(f"\nExtracted links :\n",style="blue on white")
        #     num=1
        #     for request in driver.requests:
        #         if free_tld in request.url:
        #             console.print(f"[{num}] {request.url}",style="blue on yellow")
        #             num+=1

        # else:
        #     console.print("\nThanos Report [Record]",style="blue on white")
        #     output += "\nThanos Report [Record]"
        #     time.sleep(1)
        #     console.print("""
        #     Recording...
        #     [
        #         Webdriver : [FireFox]...
        #     ]""",style="red")
        #     output += """\n
        #     Recording...
        #     [
        #         Webdriver : [FireFox]...
        #     ]\n"""
        #     driver = webdriver.Firefox()
        #     driver.get(url)
        #     free_tld = clear_tld(clear_http(url))
        #     console.print(f"\nExtracted links :\n",style="blue on white")
        #     output += f"\nExtracted links :\n"
        #     num = 1
        #     for request in driver.requests:
        #         if free_tld in request.url:
        #             console.print(f"[{num}] {request.url}",style="blue on yellow")
        #             output+=f"\n[{num}] {str(request.url)}"
        #             num+=1
        #     return output