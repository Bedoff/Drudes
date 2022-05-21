#!/usr/bin/env python
import os
import argparse
import serverstatus
import subprocess
import time
import sys

try:
    os.system("figlet test")
    os.system("clear")
except:
    os.system("apt-get install figlet")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def banner():
    os.system("clear")
    print(bcolors.BOLD)
    os.system("figlet D R U D E S")
    print("-----------------------"*2)
    print(bcolors.ENDC+"A HTTP Methods Scanner,"+bcolors.OKGREEN+"                 v1.0.0")
    print(bcolors.ENDC)

parser = argparse.ArgumentParser()
parser.add_argument('-u', type=str, required=True)
args = parser.parse_args()
link = args.u


banner()
time.sleep(1)
print(bcolors.WARNING+"[*]"+bcolors.ENDC+" Starting HTTP Methods Scanner For ("+link+")")


try:
    serverstatus = subprocess.check_output('curl -X GET -s -o /dev/null -w "%{http_code}" '+link, shell=True)
except:
    print(bcolors.FAIL+"[*]"+bcolors.ENDC+" Server is offline ("+link+")")
    time.sleep(2)
    sys.exit()

ths = open("temp.txt", "w")
ths.write(str(serverstatus))
ths.close()

statuscode = open("temp.txt","r")
statuscode=statuscode.read()

if statuscode =="b'200'":
    print(bcolors.WARNING+"[*]"+bcolors.ENDC+" Successfully Communicated With The Server ")
else:
    print(bcolors.FAIL+"[*]"+bcolors.ENDC+" Server is offline ("+link+")")
    time.sleep(2)
    sys.exit()

time.sleep(0.2)
ans=input(bcolors.OKBLUE+"[?]"+bcolors.ENDC+" Testing With GET,HEAD,POST,PUT,DELETE,CONNECT,OPTIONS,TRACE,PATCH Do You Really Want ? [Y/N] ")



def menu():
    print("")
    print(bcolors.OKBLUE+" Method       Code       Status")
    print("————————————————————————————————————"+bcolors.ENDC)


def get():
    serverstatus = subprocess.check_output('curl -X GET -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" GET          "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" GET          "+statuscode+"     OK")


def head():
    serverstatus = subprocess.check_output('curl -X HEAD -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" HEAD         "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" HEAD         "+statuscode+"     OK")


def post():
    serverstatus = subprocess.check_output('curl -X POST -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" POST         "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" POST         "+statuscode+"     OK")


def put():
    serverstatus = subprocess.check_output('curl -X PUT -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" PUT          "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" PUT          "+statuscode+"     OK")


def delete():
    serverstatus = subprocess.check_output('curl -X DELETE -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" DELETE       "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" DELETE       "+statuscode+"     OK")


def connect():
    serverstatus = subprocess.check_output('curl -X CONNECT -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" CONNECT      "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" CONNECT      "+statuscode+"     OK")


def options():
    serverstatus = subprocess.check_output('curl -X OPTIONS -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" OPTIONS      "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" OPTIONS      "+statuscode+"     OK")


def trace():
    serverstatus = subprocess.check_output('curl -X TRACE -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" TRACE        "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" TRACE        "+statuscode+"     OK")


def patch():
    serverstatus = subprocess.check_output('curl -X PATCH -s -o /dev/null -w "%{http_code}" '+link, shell=True)
    ths = open("temp.txt", "w")
    ths.write(str(serverstatus))
    ths.close()
    statuscode = open("temp.txt","r")
    statuscode=statuscode.read()
    
    if statuscode != "b'200'":
        print(bcolors.FAIL+" PATCH        "+statuscode+"     Bad Request")
    else:
        print(bcolors.OKGREEN+" PATCH        "+statuscode+"     OK")


if ans == "y" or ans == "Y":
    print("")

else:
    print(bcolors.FAIL+"[*]"+bcolors.ENDC+" You Chose Not To Continue, BYE")

menu()
print("")
get()
head()
post()
put()
delete()
connect()
options()
trace()
patch()

print("")
print("")