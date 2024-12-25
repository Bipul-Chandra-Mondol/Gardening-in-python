from dnslib import DNSRecord, RR, QTYPE, A
from socketserver import BaseRequestHandler, UDPServer

# Define the DNS Handler
class DNSHandler(BaseRequestHandler):
    def handle(self):
        # Receive the data and client address
        data, socket = self.request
        client_address = self.client_address

        # Parse the incoming DNS query
        query = DNSRecord.parse(data)
        qname = str(query.q.qname).strip(".")
        qtype = QTYPE[query.q.qtype]

        print(f"Received DNS query for {qname} of type {qtype} from {client_address}")

        # Build a simple DNS response
        response = query.reply()

        # Example response for A records
        if qtype == "A":
            # Respond with a fixed IP address (example: 127.0.0.1)
            ip_address = "127.0.0.1"
            response.add_answer(RR(qname, QTYPE.A, rdata=A(ip_address), ttl=300))

        # Send the DNS response
        socket.sendto(response.pack(), client_address)

# Define the DNS server
def start_dns_server(host="0.0.0.0", port=53):
    print(f"Starting DNS server on {host}:{port}")
    with UDPServer((host, port), DNSHandler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down the DNS server")

# Start the DNS server
if __name__ == "__main__":
    start_dns_server()
