import socket


def board_print(table):
    for row in table:
        for value in row:
            print str(value) + " ",
        print
    print "-------------"


board = [[0 for x in range(3)] for x in range(3)]
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5000))
serversocket.listen(5)  # become a server socket, maximum 5 connections


msg_num = 0
while True:
    connection, address = serversocket.accept()
    result = ""
    data = connection.recv(1024)
    while len(data) > 0:
        result += data
        data = connection.recv(1024)

    if len(result) > 0:
        x = int(result[0])
        y = int(result[1])
        board[x][y] = 1
        board_print(board)