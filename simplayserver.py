
# WebServeceを立ち上げます
# Ctrl + C + Return で終了させてください


import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer( ("", PORT ), Handler ) as httpd:
  print( "Serving at port", PORT )

  httpd.serve_forever()

