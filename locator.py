import requests
import argparse
import json
import sys

a=argparse.ArgumentParser()
# Add the arguements for terminal use
a.add_argument("--ipaddress", "-i", help="Provide IP or Domain")
#parse_args() interprests the CLI commands as arguements provided in object a
b=a.parse_args()
#ipaddress acts an object of b, which was provided as an arguement
ip=b.ipaddress

if(ip==None):
    print("Please provide a proper IP or Domain name")

url= "http://ip-api.com/json/" + str(ip)
request=requests.get(url)
data= json.loads(request.text)

def find(address):
    if address['status'] == 'success':
        print("STATUS :", address['status'])
        print("IP :", address['query'])
        print("COUNTRY :", address['country'])
        print("COUNTRY CODE :", address['countryCode'])
        print("ZIP CODE :", address['zip'])
        print("REGION :", address['region'])
        print("REGION NAME:", address['regionName'])        
        print("CITY :", address['city'])
        print("LATITUDE :", address['lat'])
        print("LONGITUDE :", address['lon'])
        print("TIMEZONE :", address['timezone'])
        print("ISP :", address['isp'])
    else:
        print("STATUS :", address['status'])
        print("IP :", address['query'])
        print("MESSAGE :", address['message'])

find(data)
        
