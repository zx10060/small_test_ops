import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b'Hello Kefir!')

httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()