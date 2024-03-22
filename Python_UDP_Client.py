import socket

def main():
    host = '127.0.0.1'
    port = 15001
    start_client(host, port)

def start_client(host, port):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send a message to the server
    message = 'Hello, Server!'
    client_socket.sendto(message.encode('utf-8'), (host, port))

    # Receive the response from the server
    response, server_address = client_socket.recvfrom(1024)
    print(f"Server says: {response.decode('utf-8')}")

    # Close the socket
    client_socket.close()


main()
