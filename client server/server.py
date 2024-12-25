import socket

def run_server():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8000
    server.bind((server_ip,port))
    server.listen(0)
    print(f"Listen on {server_ip} : {port}")
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}: {client_address[1]}")
    # Received data from client while true
    while True:
        request = client_socket.recv(1024)
        request = request.decode("UTF-8")   # convert bites into string
        if request.lower() == 'close':
            client_socket.send("closed".encode("UTF-8"))
            break
    print(f"Received Client Msg : {request}")
    client_socket.close()
    print("connection to client closed")
if __name__ == "__main__":
    run_server()