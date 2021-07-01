import requests
from googlesearch import search
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from domHttpx import cli
from domHttpx.colors import Color
from domHttpx.write import info,error


class Domain:
    def __init__(self, keyword, amount):
        self.keyword = keyword
        self.amount = amount

    def dorking(self):
        args = cli.parse_argument()
        results = search(self.keyword, num=int(self.amount), start=0, stop=None, pause=0)
        counter = 0

        for result in results:
            counter += 1
            x = urlparse(result)

            normal = x.scheme + '://' + x.netloc
            domain = x.netloc
            

            if args.domain:
                dom_result = domain

            elif args.real_path == True and args.scode == True:
                r = requests.get(result)
                if r.status_code == 200:
                    if '?' in result:
                        dom_result = normal + x.path + '?' + x.query + f' [{Color.CGREEN2}{r.status_code}{Color.ENDC}]'
                    else:
                        dom_result = normal + x.path + f' [{Color.CGREEN2}{r.status_code}{Color.ENDC}]'
                elif r.status_code == 500:
                    dom_result = normal + f' [{Color.CYELLOW2}{r.status_code}{Color.ENDC}]'
                else:
                    dom_result = normal + f' [{Color.CRED2}{r.status_code}{Color.ENDC}]'

            elif args.title: #belum fix
                r = requests.get(result)
                soup = BeautifulSoup(r.text, 'html.parser')
                if '?' in result:
                    dom_result = normal + x.path + "?" + x.query + f' [{soup.title.string}]'
                else:    
                    dom_result = normal + x.path + f' [{soup.title.string}]'

            elif args.real_path:
                if '?' in result:
                    dom_result = normal + x.path + "?" + x.query
                else:    
                    dom_result = normal + x.path

            elif args.scode:
                r = requests.get(result)
                if r.status_code == 200:
                    dom_result = normal + f' [{Color.CGREEN2}{r.status_code}{Color.ENDC}]'
                elif r.status_code == 500:
                    dom_result = normal + f' [{Color.CYELLOW2}{r.status_code}{Color.ENDC}]'
                else:
                    dom_result = normal + f' [{Color.CRED2}{r.status_code}{Color.ENDC}]'

                
            else:
                dom_result = normal
            
            print(dom_result)

            if counter == int(self.amount): # untuk menghitung amount
                break

        info('Total domain ' + str(counter))
