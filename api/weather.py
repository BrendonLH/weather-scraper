import requests
from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler
from urllib import parse
from datetime import datetime


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # get current date to parse into the urls
        date_now = datetime.now()
        year = date_now.year
        month = date_now.month
        day = date_now.day
        print(f'--------CURRENT {date_now.year} DATE--------')

        # loop through 10 years of dates starting from current date.

        # Weather data function
        def get_weather_temp(url):
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            table = soup.findAll('div')
            for div in table:
                row = div.find('tr')
                print(row)

        if "airport" in dic:
            # parse the airport into the url
            message = f'https://www.wunderground.com/history/daily/{dic["airport"]}/date/{year}-{month}-{day}'
            get_weather_temp(message)

        else:
            message = f"please enter in airport at the end of the url, EXAMPLE: ?airport=SEA"
        self.wfile.write(message.encode())
        return
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
