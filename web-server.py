#!/usr/bin/python
import socket
import os
import sys

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

PORT = 80

serverSocket.bind(('',PORT))

serverSocket.listen(1)

while True:
        print "Ready to serve..."

        connection,addr = serverSocket.accept()
        try:
                message = connection.recv(2048)

                connection.send("Server connected!")
                addressMsg  = "\r\nClient (address,port): " + str(addr) + "\r\n"
                connection.send(addressMsg)

                connection.send("HTTP/1.1 200 OK \r\n\r\n")

                connection.close()
        except IOError:
                connection.send("HTTP/1.1 404 Not Found\r\n\r\n")
                connection.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
                connection.close()

serverSocket.close()