# Simple DNS Server in Python

def dns_server():
    # Pre-defined DNS records
    dns_records = {
        "example.com": "93.184.216.34",
        "google.com": "142.250.190.46",
        "facebook.com": "31.13.71.36",
        "github.com": "140.82.121.4"
    }

    print("\nSimple DNS Server")
    print("Type 'exit' to quit the server.\n")

    while True:
        # Get domain name input from the user
        domain = input("Enter a domain name: ").strip()

        if domain.lower() == 'exit':
            print("Exiting DNS Server. Goodbye!")
            break

        # Resolve domain name
        ip_address = dns_records.get(domain)
        if ip_address:
            print(f"IP Address for {domain}: {ip_address}\n")
        else:
            print(f"Domain {domain} not found in DNS records.\n")

# Run the DNS server function
dns_server()
