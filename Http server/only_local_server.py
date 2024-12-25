from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_localhost_server(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8000)  # Serve only on localhost (127.0.0.1)
    httpd = server_class(server_address, handler_class)
    print("Serving HTTP on localhost (127.0.0.1) at port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_localhost_server()

# hit on browser: 127.0.0.1:8000