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

        # Weather data function
        def get_weather_temp():
            date_now = datetime.now()
            year = date_now.year
            month = date_now.month
            for i in range(3):
                year -= 1
                url = f'https://www.timeanddate.com/weather/usa/{dic["city"]}/historic?month={month}&year={year}'
                page = requests.get(url)
                soup = BeautifulSoup(page.text, 'html.parser')
                temp = soup.findAll(class_='sep-t')
                temp_text = []
                for row in temp:
                    cols = row.find_all('td')
                    temp_text = cols[0]
                temp_split = temp_text.text.split()
                string_text = ' '.join(temp_split)
                print(string_text)

        if "city" in dic:
            # parse the airport into the url
            # message = f'https://www.wunderground.com/history/daily/{dic["city"]}/date/{year}-{month}-{day}'
            # message = f'https://www.timeanddate.com/weather/usa/{dic["city"]}/historic?month={month}&year={year}'
            get_weather_temp()

        else:
            message = f"please enter in a city at the end of the url, EXAMPLE: ?city=seattle"
            self.wfile.write(message.encode())
        return
