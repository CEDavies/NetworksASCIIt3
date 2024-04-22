import socket

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

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

    # Receive data from the client
    data, addr = server_socket.recvfrom(1024)
    print(f"Connected to {addr}")
    print("Received a message from Client: ")
    print(f"Client says: {data.decode('utf-8')}")
    
    # Check if the received data is 'Hello, Server!'
    if data.decode('utf-8') == 'Hello Server! This is Client. Wanna play tic-tac-toe?':
        # Send a response back to the client
        response = 'Yes please!'
        print ("Responding to Client: ")
        print (response)
        server_socket.sendto(response.encode('utf-8'), addr)

    board = initialize_board()
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    print ("You are the Server, server plays as X and goes first")
    player = "X"

    boo = True
    #game actually starts here
    
    while boo:
        while boo:
            # pick move to send to client
            move = input(f"Player {player}, enter your move (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9:
                    
                row = (int(move) - 1) // 3
                col = (int(move) - 1) % 3
                if board[row][col] == " ":
                    board[row][col] = player
                    print_board(board)
                else:
                    print("That position is already taken. Try again.")
                    continue
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            # send move to Client
            server_socket.sendto(move.encode('utf-8'), addr)
            print ("SENDING MOVE TO CLIENT")

            # check for win/tie
            for i in range (0,3):
                if board[i][0] == board[i][1] == board[i][2] != " ":
                    print ("You win!")
                    boo = False
                    break
                if board[0][i] == board[1][i] == board[2][i] != " ":
                    print ("You win!")
                    boo = False
                    break
            if board[0][0] == board[1][1] == board[2][2] != " ":
                print ("You win!")
                boo = False
                break
            if board[0][2] == board[1][1] == board[2][0] != " ":
                print ("You win!")
                boo = False
                break
            #check for tie
            if not any(" " in row for row in board):
                print ("Tie game, no winner!")
                boo = False
                break
            break
        if not boo:
            break
        
        # receive move from client
        data, addr = server_socket.recvfrom(1024)
        print ("RECEIVING MOVE FROM CLIENT")
        print(f"Client move: {data.decode('utf-8')}")
        move = data.decode('utf-8')

        if move.isdigit() and 1 <= int(move) <= 9:
            row = (int(move) - 1) // 3
            col = (int(move) - 1) % 3
            if board[row][col] == " ":
                board[row][col] = "O"
                print_board(board)

                # check for win/tie
                for i in range (0,3):
                    if board[i][0] == board[i][1] == board[i][2] != " ":
                        print ("Client wins!")
                        boo = False
                        break
                    if board[0][i] == board[1][i] == board[2][i] != " ":
                        print ("Client wins!")
                        boo = False
                        break
                if board[0][0] == board[1][1] == board[2][2] != " ":
                    print ("Client wins!")
                    boo = False
                    break
                if board[0][2] == board[1][1] == board[2][0] != " ":
                    print ("Client wins!")
                    boo = False
                    break

                if not any(" " in row for row in board):
                    print ("Tie game, no winner!")
                    boo = False
                    break
        if not boo:
            break
main()
