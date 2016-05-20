
from http.server import HTTPServer,SimpleHTTPRequestHandler
from socketserver import BaseServer
import ssl

httpd = HTTPServer(('0.0.0.0', 1443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, ssl.PROTOCOL_SSLv2 ,certfile='cert.pem', server_side=True)
httpd.serve_forever()
