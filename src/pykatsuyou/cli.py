#!/usr/bin/env python3

# Script for PyKatsuyou
# Pretty basic CLI so theres definitely room for improvement.

from pykatsuyou import getInflections
from tabulate import tabulate as tb
import sys

def main():
    cmdargs = sys.argv
    
    help_cmd = '\nUsage:\npykatsuyou [verb/adjective] [-h/-j/-l]\n*Must use dictionary form\n\nOptions:\n***A table is printed by default***\n-h (--help) = outputs this text\n-j (--json) = prints json\n-l (--list) = prints a list'

    if len(cmdargs) == 2:
        if cmdargs[1] == '-h' or cmdargs[1] == '--help':
            print(help_cmd)
        else:
            userInput = cmdargs[1]
            data = getInflections(userInput, dataframe=True)
            print(tb(data, headers='keys', tablefmt='pretty'))

    elif len(cmdargs) > 2:
        userInput = cmdargs[1]
        if '--json' in cmdargs or '-j' in cmdargs:
            data = getInflections(userInput, jsonIndent=2)
            print(data['json'])
        elif '--list' in cmdargs or '-l' in cmdargs:
            data = getInflections(userInput)
            print(data['list'])
    else:
        print('Missing a verb or adjective. Checkout the options below\n', help_cmd)
        