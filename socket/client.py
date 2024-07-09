import socket
import select
import sys

server = socket.socket(socket.AS_INET,socket.SOCK_STREAM)

if len(sys.argv) !=3:
    print("correst usage: script ,Ip address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = str(sys.argv[1])
server.connect((IP_address,Port))

while True:
    sockets_list(sys.stdin, server)

    read_socket,write_socket,error_socket = select.select(sockets_list,[],[])

    for socks in read_socket:
        if socks == server:
            message = socks.recv(2048)
            print(message)
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()

server.close()
