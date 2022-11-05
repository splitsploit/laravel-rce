from lib.color import *
from random import choice
x = '''
        /\\
        \\ \\
       \\ \\ \\
      \\ \\ \\
    /  \\ \\  /
   / /  \\/ / /
  / / /\\  / / /\\
  \\/ / /  \\/ / /
    / / /\\  / /
     /  \\ \\  /
       \\ \\ \\    # Coded by Zeerx7 @ XploitSec-ID
      \\ \\ \\     # zeerx7@gmail.com
       \\ \\      # 16-11-2021
        \\/      # Version 2.0

    { Laravel Environment Scanner + PHPUnit Rce }
'''
logo_color = choice([red, blue, cyan, purple, yellow])
banner = x.replace('/', logo_color+'/').replace('\\',logo_color+'\\').replace('#', green+'#').replace('{',cyan+'{')