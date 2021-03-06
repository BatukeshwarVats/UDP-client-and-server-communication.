import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
address_2=('127.0.0.1', 3535)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

def send_to_client(a):
    localPort_2=1025
    UDPServerSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP,localPort_2))
    bytesToSend=str.encode(a)
    UDPServerSocket.sendto(bytesToSend,address_2)


def delet(a,b):
    try:
        session = open('data.txt', 'r')
        lines = session.readlines()
        session.close()
        for line in lines:
            if a in line and b in line:
                lines.remove(line)
        session_2 = open('data.txt', 'w')
        for line in lines:
            session_2.write(line)
        session_2.close()
        send_to_client("success")

    except:
        msg_reply = "failure"
        send_to_client(msg_reply)


def searc_1(a):
     try:
        session=open("data.txt",'r')
        for x in session:
            if a in x:
                y=x.split("&")
                del y[-1]
                p=""
                for l in y:
                    p=p+l
                    p=p+"&"
                send_to_client(p)
     except:
         msg_reply = "failure"
         send_to_client(msg_reply)


def entry(a,b,c,d,e,f):
    try:
        session=open("data.txt",'a')
        session.write(a+"&"+b+"&"+c+"&"+d+"&"+e+"&"+f+"\n")
        session.close()
        msg_reply = "success"
        send_to_client(msg_reply)
    except:
        msg_reply = "failure"
        send_to_client(msg_reply)

while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = format(message)
    clientIP = format(address)
    msg_recieved=clientMsg.split("&")
    if msg_recieved[0]=="b'1":
        entry(msg_recieved[1],msg_recieved[2],msg_recieved[3],msg_recieved[4],msg_recieved[5],msg_recieved[6][:-1])
    elif msg_recieved[0]=="b'2":
        searc_1(msg_recieved[2][:-1])
    elif msg_recieved[0]=="b'3":
        delet(msg_recieved[1],msg_recieved[2][:-1])