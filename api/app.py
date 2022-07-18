from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        if "name" in dic:
            message = "Hello, " + dic["name"] + "!"
        else:
            message = "replace app with weather?city={cityname} with no brackets. this will display the avg " \
                      "temperatures for you're selected cuty for the past 5 years starting from the current year "
        self.wfile.write(message.encode())
        return
