#Simple server for capturing network traffic

'''
In the first execution:
1. Generating the certfile:
    openssl req -x509 -newkey rsa:2048 -nodes \
    -keyout key.pem -out cert.pem -deys 365 \
    -subj "/CN=localhost" \
    -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"

2. Runing the server:
    python3 server.py

3. Testing in other terminal:
    curl --cacert cer.pem https://localhost:8443/status
'''

import ssl
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
    server = HTTPServer(('0.0.0.0', 8443), Handler)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    server.socket = context.wrap_socket(server.socket, server_side=True)

    print('Server online in: https://0.0.0.0:8443 (Ctrl + C to stop)')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Lost connection due to Keyboard Interruption')
    finally:
        server.server_close()