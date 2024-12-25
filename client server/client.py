import socket

def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8000
    # connect to the server
    client.connect((server_ip, port))
    print(f"Connected to server {server_ip}:{port}")
    
    while True:
        # Send message to the server
        message = input("Enter message to send (type 'close' to disconnect): ")
        client.send(message.encode("UTF-8"))  # convert string to bytes
        # Receive response from the server
        response = client.recv(1024)  # receive up to 1024 bytes
        response = response.decode("UTF-8")  # convert bytes to string
        print(f"Server response: {response}")
        # If the user sends 'close', break out of the loop
        if message.lower() == 'close':
            break
        # Close the connection
        client.close()
        print("Disconnected from server")
        
if __name__ == "__main__":
    run_client()