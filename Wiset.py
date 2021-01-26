#!usr/bin/env python

import subprocess
import optparse
import sys
import re


def get_args():
    option_parser = optparse.OptionParser()
    option_parser.add_option("-i", "--interface", dest="interface", help="helps to choose interface")
    option_parser.add_option("-m", "--mac", dest="new_mac", help="new mac address for interface")
    return option_parser.parse_args()


def check_args(option):
    if not option.interface:
        sys.exit("[-] Please enter interface argument, use -h or --help for more info")
    elif not option.new_mac:
        sys.exit("[-] Please enter new mac address as argument, use -h or --help for more info")
    return True


def change_mac(option):
    if check_args(options):
        subprocess.call(["ifconfig", option.interface, "down"])
        subprocess.call(["ifconfig", option.interface, "hw", "ether", option.new_mac])
        subprocess.call(["ifconfig", option.interface, "up"])


def check_mac_change(option):
    ifconfig_result = subprocess.check_output(["ifconfig", option.interface])
    mac_regex = r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"
    mac_check_result = re.search(mac_regex, str(ifconfig_result))
    if mac_check_result:
        if mac_check_result.group(0) == option.new_mac:
            print("[+] " + option.interface + " MAC successfully changed \n[+] Current Mac: " + mac_check_result.group(0))
        else:
            print("[-] " + option.interface + " MAC is not changed/ error while reading MAC address please try again")
            print("[+] Current Mac: " + mac_check_result.group(0))
    else:
        print("[-] MAC not found")


(options, args) = get_args()
change_mac(options)
check_mac_change(options)
