import socket

# # # next create a socket object
# s = socket.socket()
# close = False
# #f = s.makefile()
# print ("Socket successfully created")
#
# # # reserve a port on your computer in our
# # # case it is 12345 but it can be anything
# port = 12345

def printer(p):
    print("Welcome to the intermediate code!")
    print("You sent: ", p)

# def joinComm(p,host):
#     #s.connect(('hostname', port))
#     #s.connect(('127.0.0.1', port))
#     s.connect((host, port))
#
#     # receive data from the server
#     while True:
#         if (close):
#             break
#         val = s.recv(1024)
#         if not (val == b''):
#             print(val)

def joinCommunication(ip):
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    port = 12345

    # connect to the server on local computer
    # s.connect(('127.0.0.1', port))
    s.connect((ip, port))

    # receive data from the server
    print(s.recv(1024))
    # close the connection
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
        c.close()

# def openComm(p):
#     s.bind(('', port))
#     print("socket binded to %s" % (port))
#     s.listen(5)
#     print("socket is listening")
#     print("Opening Communication with: ")
#     while True:
#         # Establish connection with client.
#         c, addr = s.accept()
#         print('Got connection from', addr)
#         c.send('Thanks for connecting')
#         while True:
#             tosend = input()
#             c.send(tosend.encode())

# def closeComm():
#     print("Closing Communication with: ")
#     s.close()

# def sendData(p,msg):
#     s.send(msg.encode())
#         #while True:
#          #   tosend = input()
#         #    c.send(tosend.encode())
