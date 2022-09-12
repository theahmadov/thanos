import urllib
def run(url):
    try:
        connect = urllib.request.urlopen("https://"+url)
        return "https://"
    except:
        return "http://"