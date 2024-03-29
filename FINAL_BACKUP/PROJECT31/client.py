#client.py
import socket
import threading
nickname = input("Choose your unique identifier : ").strip()
while not nickname.isdigit():
    nickname = input("Your unique identifier must be a digit: ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = int(input('PORT NUMBER: ').strip())
my_socket.connect((host, port))
def thread_sending():
    while True:
        message_to_send = input('Enter Your Message :\n')
        if message_to_send:
            message_with_nickname = nickname + " : " + message_to_send
            my_socket.send(message_with_nickname.encode())
        
def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)
        
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()