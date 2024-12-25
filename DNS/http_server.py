from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set cseseven.html as the default file
        if self.path == '/':
            self.path = '/cseseven.html'
        return super().do_GET()

# Set up the server
if __name__ == "__main__":
    port = 80  # Use port 80 for HTTP
    server_address = ("", port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Serving HTTP on port {port} (http://localhost:{port}/)")
    httpd.serve_forever()
