import socket
import threading
# Client code
def start_client(server_host='127.0.0.1', server_port=12345):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_host, server_port))

    def receive_messages():
        try:
            while True:
                message = client.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"[SERVER] {message}")
        except Exception as e:
            print(f"[ERROR] {e}")
        finally:
            client.close()

    receiver_thread = threading.Thread(target=receive_messages)
    receiver_thread.start()

    try:
        while True:
            message = input("You: ")
            if message.lower() == 'exit':
                client.send(message.encode('utf-8'))
                break
            client.send(message.encode('utf-8'))
    except KeyboardInterrupt:
        print("[DISCONNECT] Client exiting...")
        client.send("exit".encode('utf-8'))
    finally:
        client.close()



start_client()
