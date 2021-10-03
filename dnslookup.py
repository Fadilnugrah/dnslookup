#!/usr/bin/python

from files import color
import requests
import json
import argparse, sys

cod = sys.argv[0]
parse = argparse.ArgumentParser(description=f"""
  {color.Color.red}*{color.Color.green}D N S lookup{color.Color.red}*
*{color.Color.green}v{color.Color.red}.{color.Color.green}hacker target{color.Color.red}*{color.Color.whiteNormal}
""")
parse.add_argument('-f', type=str, metavar='[file.txt]', help='files list.txt')
args = parse.parse_args()

class x:

    def __init__(self,url,domen):
        with open('result.txt','w') as w:
            with open(domen,'r') as a:
                self.xx = a.readlines()
                for y in self.xx:
                    try:
                        self.str = y.strip()
                        self.get = requests.get(url.format(self.str)).text
                        self.pft = (f'[*]{color.Color.red}result from{color.Color.green} {self.str.upper()}{color.Color.whiteNormal}');print(self.get)
                        print (self.pft)
                        w.write(self.pft+'\n'+self.get+'\n')

                    except Exception as er:
                        print(f'[!]{er}')
                        exit()


if args.f:
    url = ('https://api.hackertarget.com/dnslookup/?q={}')
    x(url,args.f)

else:
    print(f'[WARNING]invalid! usage:{color.Color.red} python {cod} -h')
    sys.exit()

