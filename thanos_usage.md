# $${\color{red}Thanos}$$
- ### [Thanos - Scan](#thanos---scan)
- ### [Thanos - Installation](#thanos---installation)

## Thanos - Scan
<pre>
<b>Port Scan</b>      : python3 thanos.py [normal,save,port]https://example.com

<b>Subdomain Scan</b> : python3 thanos.py [normal,save,sub]https://example.com

<b>Directory Scan</b> : python3 thanos.py [normal,save,dir]https://example.com

<b>Record Traffic</b> : python3 thanos.py [normal,save,rec]https://example.com
</pre>

## Thanos - Installation
```bash
sudo apt upgrade
git clone https://github.com/thesaderror/thanos
cd thanos
pip3 install -r requirements.txt
sudo pip3 install -r requirements.txt
sudo python3 thanos.py thanos
```
