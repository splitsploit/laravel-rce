#!/usr/bin/python
from os import system
from sys import platform

purple = '\033[95m'
blue = '\033[94m'
cyan = '\033[96m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
end = '\033[0m'
bold = '\033[1m'
u = '\033[4m'

if platform == 'win32':
    system('color')
