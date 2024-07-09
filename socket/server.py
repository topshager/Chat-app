#server - side funtionality
import socket
import select
import sys
from _thread import *


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET - address domain of the socket.
#SOCK_STREAM - DATA IS READ IN CONTINUES FLOW.

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)




if len(sys.argv) != 3:
    print("correct usage: script, IP address, port number")
    exit()



IP_address = str(sys.argv[1])
#when running the server script   using command line argument's eg. python3 server.py 127.0.0.1 8080 ->argv[1] = 127.0.0.1

Port = int(sys.argv[2])
#port will be argv[2] = 8080

server.bind((IP_address,Port))
#binding the defined port and ip to server
server.listen(100)
#serer is in listening mode ,maximum que size
list_of_clients = []


def clientthread(conn,addr):
    conn.send("welcome to this chatroom")

    while True:
        try:
            message = conn.recv(2048)
            if message:
                print("<" + addr[0] + ">" + message)
                message_to_send = "<" + addr[0] +">" + message
                broadcast(message_to_send,conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(message,connection):
    for client in list_of_clients:
        if client !=connection:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + "connected")
    start_new_thread(clientthread,(conn,addr))


conn.close()
server.close()
