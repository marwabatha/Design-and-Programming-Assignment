#The server recieves a message from the client and reads a text file and sends the data to the client.

import socket                   # Import socket module

port = 60000                    # Reserving an unreserved port.
ssocket = socket.socket()       # Create a socket object called ssocket
host = socket.gethostname()     # Get local machines name for host.
ssocket.bind((host, port))      # Binding to the port.
ssocket.listen(5)               # Waiting for the clients connection.

print ('Job seeker waiting')

while True:
    connect, addr = ssocket.accept()           # Establishing connection with job creator.
    print ('Got connection from', addr)
    data = connect.recv(1024)
    print('Job received', repr(data))       #Job confirmation.

    filename='mytext.txt'
    f = open(filename,'rb')                 #Opening file.
    x = f.read(1024)                        #Reading a file
    while (x):                              #While data exist run.
       connect.send(x)
       print('Sent data: ',repr(x))         #Prints the data present x
       x = f.read(1024)                     #Read from file in variable x
    f.close()

    print('Done receiving jobs')            #print message.
    connect.send('Thank you for connecting'.encode())
    connect.close()
