import socket


while True:
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 5000))

    msg = raw_input("Enter message: ")
    clientsocket.send(msg)
    clientsocket.close()
