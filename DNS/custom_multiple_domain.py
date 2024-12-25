from dnslib import DNSRecord, QTYPE, RR, A, DNSHeader
import socket
import socketserver

# Get the local IP address of the machine
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# DNS server configuration - Add your custom domain mappings here
DOMAIN_TO_IP = {
    'example.com': '192.168.1.100',
    'sub.example.com': '192.168.1.101',
    'test.local': local_ip,
    'mycustomdomain.com': '192.168.1.102'
}

class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        try:
            # Parse the DNS request
            request = DNSRecord.parse(data)
            qname = str(request.q.qname)[:-1]  # Remove trailing dot from domain name
            print(f"Received request for: {qname}")

            # Check if the domain is in our mapping
            if qname in DOMAIN_TO_IP:
                ip = DOMAIN_TO_IP[qname]
                reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1),
                                  q=request.q)
                reply.add_answer(RR(qname, QTYPE.A, rdata=A(ip), ttl=60))
                socket.sendto(reply.pack(), self.client_address)
                print(f"Resolved {qname} to {ip}")
            else:
                # Respond with NXDOMAIN if domain is not found
                reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1, rcode=3),
                                  q=request.q)
                socket.sendto(reply.pack(), self.client_address)
                print(f"Domain {qname} not found in DNS records")
        except Exception as e:
            print(f"Error handling request: {e}")

if __name__ == "__main__":
    # Start the DNS server
    server_address = ('', 53)  # Port 53 for DNS
    try:
        with socketserver.UDPServer(server_address, DNSHandler) as server:
            print(f"DNS Server running on {local_ip}")
            server.serve_forever()
    except PermissionError:
        print("Permission denied: You must run this script as an administrator/root to bind to port 53.")
    except Exception as e:
        print(f"Failed to start DNS server: {e}")
