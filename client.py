#The client sends a message to the server and then receives data writes it into a text file.

import socket                   # Import socket module

s = socket.socket()             # Create a socket object called s
host = socket.gethostname()     # Getting local hostname
port = 60000                    # Reserving a port for the service. Making use of an unreserved port.

s.connect((host, port))
s.send("Hello jobseeker!".encode())        #Sending message to client.

with open('received_file', 'wb') as f:  #Opening file
    print ('Opening file')               #Print confimation message file is opened.
    while True:                         #Keep connection open to accept jobs
        print('Job data being received')
        jdata = s.recv(1024)             #Receive data into data variable
        print('data=', jdata)        #Print data on the screen.
        if not jdata:                    #If there is no job available then break.
            break
        f.write(jdata)                   #Write data into a file

f.close()                               #Close file.
print('Successfully closed the file')
s.close()                               #Close the connection to the server.
print('Connection closed')
