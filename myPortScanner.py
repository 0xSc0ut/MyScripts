#!/usr/bin/python3

import sys, getopt
import os
import subprocess as sp

print ("IP Address:")
ip_address = raw_input()
print ("Output Directory:") 
outputdir = raw_input()

if (len(ip_address) !=0 and len(outputdir)!=0):
   os.mkdir(outputdir)
   getpath = os.getcwd()
   path= getpath + "/" + outputdir
   os.chdir(path)
#   os.system("pwd")
######################################
   masscan_cmd = "masscan -p1-65535,U:1-65535 " + ip_address  +" --rate=1000 -e tun0 -oL masscan.txt"
   print ('Executing masscan - Port Scanning :', masscan_cmd)
   os.system(masscan_cmd)
   print ('Masscan completed Successfully and saved to masscan.txt')
#######################################
   cmd = """awk 'BEGIN { OFS = "\t" ; ORS = "," } { if($3!="") print $3 }' masscan.txt | sed s/.$//"""
   p = sp.Popen(cmd, stdin=sp.PIPE, stdout = sp.PIPE, stderr = sp.PIPE,shell=True)
   ports_to_scan =""
   for l in p.stdout:
        ports_to_scan=l.decode()

   nmap_cmd = "nmap -A -p"+ ports_to_scan +" " + ip_address + " --max-rate=1000 -oN nmap.txt"
   os.system(nmap_cmd)
   print ("Starting Nmap : ",nmap_cmd)
   print("Nmap completed Successfully and saved to nmap.txt")
else:
   print ("Check your inputs!!")
