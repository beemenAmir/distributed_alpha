import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
clients = []
clientid = 0
while True:
    #  Wait for next request from client
    message = socket.recv().decode("utf-8")
    if message =="connected":
        socket.send(b"recieved")
        message2 = socket.recv().decode("utf-8")
        if message2 in clients:
            pass
        else:
            clients.append(message2)
        print(clients)
        socket.send(b"recieved")
    print(message)

       # print(f"Received request:clientID[{clientid}] {message}")
   # if clientid ==2:
       # print("2 clients are connected")

    #  Do some 'work'
    time.sleep(1)
