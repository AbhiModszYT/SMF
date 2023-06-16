#!/usr/bin/env python

import pygeoip
import socket
import getopt
import sys
import json

APP_NAME = "ip Tracker"
VERSION = "1.0"
BANNER = """
                                      Hey there!
                                    101.188.67.134
                                     is that you?
█████╗ ███╗   ███╗██████╗  ██████╗ ████████╗
██╔══██╗████╗ ████║██╔══██╗██╔═══██╗╚══██╔══╝
███████║██╔████╔██║██████╔╝██║   ██║   ██║   
██╔══██║██║╚██╔╝██║██╔══██╗██║   ██║   ██║   
██║  ██║██║ ╚═╝ ██║██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝  ╚═════╝    ╚═╝   
                                             
   {} v{}
 GitHub           : AbhiModszYT
 Teleram Channel  : @AbhiModszYT_Return
 Teleram Channel  : @t.me/AmBotYT
 Teleram UserName : @AM_YTBOTT
 Coded by         : AMBOT
 Teams            : None
"""

HELP_USAGE = """
usage: python ip Tracker.py [options]
options:
-v --version shows the current version
-t --target  the target host
-h --help    shows the help usage
"""

OPTIONS = "hvt:"
LONG_OPTIONS = ["help", "version", "target="]

DB_FILE = "Am.dat"
target = None


def usage():
    print(HELP_USAGE)


def version():
    print(f"{APP_NAME} v{VERSION}")


def parseargs(argv):
    try:
        opts, args = getopt.getopt(argv, OPTIONS, LONG_OPTIONS)
        if len(opts) == 0:
            print("[!] No arguments given")
            print("[!] Use --help for help usage")
            sys.exit(0)

        for opt, arg in opts:
            if opt in ("-v", "--version"):
                version()
                sys.exit(0)

            elif opt in ("-h", "--help"):
                usage()
                sys.exit(0)

            elif opt in ("-t", "--target"):
                global target
                target = arg

        if target is None or not target:
            print("[!] No target given")
            print("[!] Use --help for help usage")
            sys.exit(0)

    except getopt.GetoptError as error:
        print("\n")
        print(error)
        usage()
        sys.exit(0)


def gethostaddr():
    host_addr = None

    try:
        host_addr = socket.gethostbyname(target)
    except:
        pass

    return host_addr


def main(argv):
    parseargs(argv)
    print(BANNER.format(APP_NAME, VERSION))

    print("[+] Resolving host...")
    host = gethostaddr()
    if host is None or not host:
        print("[!] Unable to resolve host {}".format(target))
        print("[!] Make sure the host is up: ping -c1 {}\n".format(target))
        sys.exit(0)

    print("[+] Host {} has address: {}".format(target, host))
    print("[+] Tracking host...")

    query = pygeoip.GeoIP(DB_FILE)
    result = query.record_by_addr(host)

    if result is None or not result:
        print("[!] Host location not found")
        sys.exit(0)

    print("[+] Host location found:")
    print(json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1:])
