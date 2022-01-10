from http.server import BaseHTTPRequestHandler
from urllib.request import urlretrieve
from PIL import Image

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        #urlretrieve()
        #message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        #self.wfile.write(message.encode())
        return