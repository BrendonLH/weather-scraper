import requests
from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        if "airport" in dic:
            # message = "Hello, " + dic["airport"] + "!"
            message = f'https://www.wunderground.com/history/daily/{dic["airport"]}/date/2022-7-17'
        else:
            message = "Hello, stranger!"
        self.wfile.write(message.encode())
        return

        # weather_url = 'https://www.wunderground.com/history/daily/airport/date/2022-7-17'

        # def get_citations_needed_count(url):
        #     page = requests.get(url)
        #     soup = BeautifulSoup(page.content, 'html.parser')
        #     prettier_soup = soup.findAll(text='citation needed')
        #     citations_count = len(prettier_soup)
        #     print(f'{citations_count} citations needed')
        #
        # def get_citations_needed_report(url):
        #     page = requests.get(url)
        #     soup = BeautifulSoup(page.content, 'html.parser')
        #     prettier_soup = soup.findAll(text='citation needed')
        #     single_parent = prettier_soup[0]
        #     soup_parents = single_parent.findParent('p')
        #     soup_text = soup_parents.text.split()
        #     string_text = ' '.join(soup_text)
        #     print(string_text)
        #
        # get_citations_needed_count(corgi_url)
        # get_citations_needed_report(corgi_url)


