#!var/usr/env python

import subprocess

subprocess.check_call(["sudo","ifconfig"])
print("")
interface = raw_input("interface>")
mac = raw_input("mac>")
print("Changing MAC of "+ interface +"... to " + mac)
subprocess.check_call(["sudo","ifconfig",interface,"down"])
subprocess.check_call(["sudo","ifconfig",interface,"hw","ether",mac])
subprocess.check_call(["sudo","ifconfig",interface,"up"])
print("Mac successfully changed to "+ mac)
choice = raw_input("Would you like to change "+ interface +" to monitor mode(y/n)")
if choice == "y" :
    print("Changing "+ interface +" to monitor mode")
    subprocess.check_call(["sudo","ifconfig",interface,"down"])
    subprocess.check_call(["sudo","iwconfig",interface,"mode","monitor"])
    subprocess.check_call(["sudo","ifconfig",interface,"up"])
    print("Successfully "+ interface +" changed to monitor mode")
    subprocess.check_call(["sudo","iwconfig",interface])
else:
    print(interface+" not changed to monitor mode")






