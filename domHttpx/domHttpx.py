import requests
import socket
import os
from googlesearch import search
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from domHttpx import cli
from domHttpx.colors import Color
from domHttpx.write import success, info, error, tab, sc_200, sc_500, sc_other, title


class Domain:    
    def __init__(self, keyword, amount):
        self.keyword = keyword
        self.amount = amount

        self.normal_url = []
        self.domain_only = []
        self.real_path = []
        self.ip = []

        self.custom_path = []
        self.output_status_code = []
        self.output_title = []
        self.output_server = []

    def dork(self):
        results = search(self.keyword, num=int(self.amount), start=0, stop=None, pause=0)
        counter = 0

        for result in results:
            counter += 1
            parsed_url = urlparse(result)

            normal = parsed_url.scheme + '://' + parsed_url.netloc
            domain_only = parsed_url.netloc
            real_path = result
            ip = socket.gethostbyname(domain_only)

            self.normal_url.append(normal)
            self.domain_only.append(domain_only)
            self.real_path.append(real_path)
            self.ip.append(ip)
            
            if counter == int(self.amount): # untuk menghitung amount
                break
        
    def get_normal(self):
        self.dork()
        return self.normal_url

    def get_domain_only(self):
        self.dork()
        return self.domain_only
        
    def get_real_path(self):
        self.dork()
        return self.real_path

    def get_ip(self):
        self.dork()
        return self.ip

    def get_custom_path(self, path=None):
        self.dork()
        for dom_result in self.normal_url:
            self.custom_path.append(dom_result + '/' + path)
        
        return self.custom_path

    def get_status_code(self, url):
        for domain in url:
            r = requests.get(domain)
            if r.status_code == 200:
                status_code = sc_200(r.status_code)
            elif r.status_code == 500:
                status_code = sc_500(r.status_code)
            else:
                status_code = sc_other(r.status_code)

            url = domain + ' ' + status_code
            self.output_status_code.append(url)

        return self.output_status_code

    def get_title(self, url):
        for domain in url:
            r = requests.get(domain)
            soup = BeautifulSoup(r.text, 'html.parser')
            title = f"[{Color.CCYAN2}{soup.title.string}{Color.ENDC}]"
            url = domain + ' ' + title
            self.output_title.append(url)
        
        return self.output_title

    def get_server(self, url):
        for domain in url:
            r = requests.get(domain)
            server = f"[{Color.CRED2}{r.headers['server']}{Color.ENDC}]"
            url = domain + ' ' + server
            self.output_server.append(url)
        
        return self.output_server

    def save_output(self, filename, output):
        directory = "result"
        self.output = open(directory + '/' + filename, 'w')
        self.output.write('\n'.join(output))
        self.output.close()

    # def check_result(self):
    #     x = glob.glob('./result/*')
    #     for tes in x:
    #         print(tes)

    def show(self):
        args = cli.parse_argument()

        # if args.check_result == True:
        #     self.check_result()
        #     exit()

        if args.domain == True:
            dom_result = self.get_domain_only()
                
        elif args.real_path == True:
            dom_result = self.get_real_path()

        elif args.ip == True:
            dom_result = self.get_ip()

        elif args.path != None:
            dom_result = self.get_custom_path(args.path)

        else:
            dom_result = self.get_normal()


        if args.status_code == True:
            dom_result = self.get_status_code(dom_result)

        if args.title == True:
            dom_result = self.get_title(dom_result)

        if args.server == True:
            dom_result = self.get_server(dom_result)
            

        ''' Output '''
        if args.output != None:
            self.save_output(args.output, dom_result)
        
        
        counter = 0
        for show in dom_result:
            counter += 1
            print(show)


        if args.silent != True:
            tab() # print("\n")
            if 'http' not in show:
                info('Searching IP for %s keyword' % self.keyword)
                info('Found %i IP' % counter)
            else:
                info('Searching domain for %s keyword' % self.keyword)
                info('Found %i domain' % counter)
    
        