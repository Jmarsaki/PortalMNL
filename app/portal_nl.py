# -*- coding: utf-8 -*-
"""Portal NL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lPAaZQ3wxMaKPYVfum8uSVQNt7pwvx2j
"""

# server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class RequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == "__main__":
    try:
        server = HTTPServer(('localhost', PORT), RequestHandler)
        print(f'Servidor iniciado en http://localhost:{PORT}')
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServidor detenido')
        server.server_close()