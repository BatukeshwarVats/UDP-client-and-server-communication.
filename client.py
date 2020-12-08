print('''
	==================================
	|      [Datacontroller] ==> :)   |
	|--------------------------------|
	|  CoDeD By- Batukeshwar vats    |
	|________________________________|
	''')

import socket


def listen():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 3535))
    msgFromServer = sock.recvfrom(1024)
    global msg_rec
    msg_rec = msgFromServer[0]
    print(msg_rec)


def send_msg(msg):
    msgFromClient = msg
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = ("127.0.0.1", 20001)
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.sendto(bytesToSend, serverAddressPort)

do = input('''
		Choose any:
		1 - Store Information
		2 - Search
		3 - Delete your informations
		==> ''')

if do == '1':
    fname = input("Enter first name :")
    lname = input("Enter last name :")
    uname = input("Enter user name :")
    contact = input("Enter your Contact number :")
    emailid = input("Enter your Email-Id :")
    password = input("Enter your password :")
    msg = "1" + "&" + fname + "&" + lname + "&" + uname + "&" + contact + "&" + emailid + "&" + password
    send_msg(msg)
    while True:
        listen()

if do == '2':
    do = input('''
    		Choose any:
    		1 - Searchby username
    		2 - Searchby first name
    		==> ''')
    if do == '1':
        uname_s = input("Enter your username :")
        msg = "2" + "&" + "1" + "&" + uname_s
        send_msg(msg)
        while True:
            listen()

    if do == '2':
        fname_s = input("Enter your first name :")
        msg = "2" + "&" + "2" + "&" + fname_s
        send_msg(msg)
        while True:
            listen()


if do == '3':
    uname_d = input("Enter your username :")
    password_d = input("Enter your password :")
    msg = "3" + "&" + uname_d + "&" + password_d
    send_msg(msg)
    while True:
        listen()
