import socket

#creating a socket, probably related to internet standard
#default socket types, does not required mostly
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#trying to connect to the server
mysock.connect(('localhost', 9000))
#changing Unicode(python) to UTF-8(compressed internet code)
cmd = 'GET http://localhost:9000 HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd) #sending the request

while True:
    data = mysock.recv(512) #recv >> take in the data until the number in the function is done
    if len(data) < 1: #breaks when there is no data 
        break
    print(data.decode(), end = '') #decoding the data as Unicode again and printing it 

mysock.close()