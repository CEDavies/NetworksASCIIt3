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
    start_client(host, port)

def start_client(host, port):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send a message to the server
    message = 'Hello Server! This is Client. Wanna play tic-tac-toe?'
    print ("Sending this message to Server: ")
    print (message)
    client_socket.sendto(message.encode('utf-8'), (host, port))

    # Receive the response from the server
    response, server_address = client_socket.recvfrom(1024)
    print(f"Server says: {response.decode('utf-8')}")

    board = initialize_board()
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    print ("You are the Client, client plays as O and goes second")
    player = "O"

    boo = True
    #game actually starts here
    
    while True:
        # receive move from Server
        response, server_address = client_socket.recvfrom(1024)
        print(f"Server move: {response.decode('utf-8')}")
        move = response.decode('utf-8')

        #checks if server move is a digit 1-9, if so, prints it on board
        if move.isdigit() and 1 <= int(move) <= 9:
            row = (int(move) - 1) // 3
            col = (int(move) - 1) % 3
            if board[row][col] == " ":
                board[row][col] = "X"
                print_board(board)

                # check for win/tie
                # if any row, column, or diagonal has the same contents, that means a win
                # for loop iterates through rows/columns
                for i in range (0,3):
                    if board[i][0] == board[i][1] == board[i][2] != " ":
                        print ("Server wins!")
                        boo = False
                        break
                    if board[0][i] == board[1][i] == board[2][i] != " ":
                        print ("Server wins!")
                        boo = False
                        break
                # checking the two digonals for a win
                if board[0][0] == board[1][1] == board[2][2] != " ":
                    print ("Server wins!")
                    boo = False
                    break
                if board[0][2] == board[1][1] == board[2][0] != " ":
                    print ("Server wins!")
                    boo = False
                    break
                # if there are no empty spaces, but no winner, must be a tie
                if not any(" " in row for row in board):
                    print ("Tie game, no winner!")
                    boo = False
                    break
        if not boo:
            break
        
        while True:
            # pick move to send to server
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

            # send move to server
            client_socket.sendto(move.encode('utf-8'), (host, port))
            print ("SENDING MOVE TO SERVER")

            # check for win/tie
            for i in range (0,3):
                if board[i][0] == board[i][1] == board[i][2] != " ":
                    print ("You win!")
                    boo = False
                if board[0][i] == board[1][i] == board[2][i] != " ":
                    print ("You win!")
                    boo = False
            if board[0][0] == board[1][1] == board[2][2] != " ":
                print ("You win!")
                boo = False
            if board[0][2] == board[1][1] == board[2][0] != " ":
                print ("You win!")
                boo = False
            if not any(" " in row for row in board):
                print ("Tie game, no winner!")
                boo = False
                break
            break
        if not boo:
            break
    # Close the socket
    client_socket.close()
main()
