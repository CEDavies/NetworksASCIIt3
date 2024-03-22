import socket

def main():
    host = '127.0.0.1'
    port = 15001
    start_server(host, port)

def start_server(host, port):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to a specific address and port
    server_socket.bind((host, port))
    
    print(f"Server listening on {host}:{port}")

    while True:
        # Receive data from the client
        data, addr = server_socket.recvfrom(1024)
        print(f"Connected to {addr}")

        # Check if the received data is 'Hello, Server!'
        if data.decode('utf-8') == 'Hello, Server!':
            # Send a response back to the client
            response = 'Hello, Client!'
            server_socket.sendto(response.encode('utf-8'), addr)

main()
