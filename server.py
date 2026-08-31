#Simple server for capturing network traffic
#Runs with: pyhton3 server.py


from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'{"status": "ok"}\n')
        else:
            self.send_response(200)
            self.send_header('COntent-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello Wonderful Word\n')

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        print(f'Received POST in {self.path}: {body}')

        self.send_response(201)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Received data\n')

    def do_PUT(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        print(f'Received PUT in {self.path}: {body}')

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Updated\n')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    print('Server online in: http://0.0.0.0:8000 (Ctrl + C to stop)')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Lost connection due to Keyboard Interruption')
    finally:
        server.server_close()