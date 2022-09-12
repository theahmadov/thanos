# Thanos

**Thanos is python based website vulnerability scanner. You can use it to get report of vulnerabilities of your website.
Also if there is bug or error etc. thanos will report you with large explanation. Try learn to use it correctly. 
There is all options you need to scan deeply...**

## Install

- [x] Debian [Kali,Parrot,Ubuntu,Mint,KDE]
```
curl  -s https://raw.githubusercontent.com/thesaderror/thanos/main/install_debian.sh | bash
```

## Usage
```
Thanos 1.3

-SCAN :
    -port : python3 thanos.py [normal,port]example.com
    |
    |__ Description : Port scanning
    
    -subdomain : python3 thanos.py [normal,sub]example.com
    |
    |__ Description : Find subdomains of website
    
    -directory : python3 thanos.py [normal,dir]example.com
    |
    |__ Description : Get all directories of website
    
    -record : python3 thanos.py [normal,record]example.com
    |
    |__ Description : Record website and extract hidden links

-SAVE :
    save output : python3 thanos.py [normal,port,dir,sub]example.com

Update : python3 thanos.py update
Full : python3 thanos.py [x]example.com
```
