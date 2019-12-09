import socket

# # next create a socket object
s = socket.socket()
close = False
#f = s.makefile()
print ("Socket successfully created")
  
# # reserve a port on your computer in our 
# # case it is 12345 but it can be anything 
port = 12345

def printer(p):
    print("Welcome to the intermediate code!")
    print("You sent: ", p)

def joinComm(p):
    #s.connect(('hostname', port))
    s.connect(('127.0.0.1', port))

    # receive data from the server
    while True:
        if (close):
            break
        val = s.recv(1024)
        if not (val == b''):
            print(val)


def openComm(p):
    s.bind(('', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("socket is listening")
    print("Opening Communication with: ")

def closeComm():
    print("Closing Communication with: ")
    s.close()

def sendData():
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send('Thanks for connecting')
        while True:
            tosend = input()
            c.send(tosend.encode())



def ping():
    print("Ping to: ")
