#!usr/bin/env python

import subprocess
import optparse
import sys


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
        print("[+] " + option.interface + " MAC successfully changed to " + option.new_mac)


(options, args) = get_args()

change_mac(options)
