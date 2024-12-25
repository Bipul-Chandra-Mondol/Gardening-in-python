import socket
import threading

# Server code
def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")

    try:
        while True:
            # Receive data from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message or message.lower() == 'exit':
                print(f"[DISCONNECT] {address} disconnected.")
                break

            print(f"[{address}] {message}")

            # Echo back the message to the client
            response = f"Server received: {message}"
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] {address} - {e}")
    finally:
        client_socket.close()

# Start the server
def start_server(host='0.0.0.0', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        
start_server()
