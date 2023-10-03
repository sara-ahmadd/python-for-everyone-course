import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind a host and a port to the initiated socket
sock.connect(("data.pr4e.org", 80))

cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()

sock.send(cmd)

while True:
    data = sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

sock.close()

# with url libray
import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in fhandle:
    print(line.decode().strip())