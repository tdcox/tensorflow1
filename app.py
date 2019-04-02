#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
import word2vec
import os
import sys
from urllib.parse import urlparse, parse_qs

PORT_NUMBER = 8080
READY = False
current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
word2vec.word2vec_basic(os.path.join(current_path, 'log'))


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handler for GET requests"""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        query = urlparse(self.path).query
        word_list = parse_qs(query).get('word', None)
        word = word_list[0]
        print(word)
        if word:
            r = word2vec.associate(word)
        else:
            r = "Hello"
        self.wfile.write(bytes(r, "utf8"))


try:
    server = HTTPServer(('', PORT_NUMBER), MyHandler)
    print('Started httpserver on port', PORT_NUMBER)
    server.serve_forever()

except KeyboardInterrupt:
    server.server_close()
    print('Stopping server')
