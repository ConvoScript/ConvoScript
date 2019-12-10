import socket
Close = False

def closeCommunication():
    global Close
    Close = True
def joinCommunication(ip):
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12345

    # connect to the server on local computer
    s.connect((ip, port))

    # receive data from the server
    while( not Close):
        print(s.recv(1024))
    s.close()

def openCommunication(p):
    # next create a socket object
    s = socket.socket()
    print("Socket successfully created")

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 12345

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))
    print("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)

        # send a thank you message to the client.
        c.send(b'Thank you for connecting')

        # Close the connection with the client
        while (not Close):
            c.send(input().encode())
        s.close()
