import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5000))
serversocket.listen(5)  # become a server socket, maximum 5 connections

#board = [[0 for x in range(3)] for x in range(3)]


msg_num = 0
while True:
    connection, address = serversocket.accept()
    result = ""
    data = connection.recv(1024)
    while len(data) > 0:
        result += data
        data = connection.recv(1024)

    if len(result) > 0:
        print "Message number " + str(msg_num) + ": " + result
        msg_num += 1