#client.py
import socket
import threading
unique_name = input("Enter identifier: ").strip()
while not unique_name:
    unique_name = input("Your Identifier Must Be A Number: ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = 8001

my_socket.connect((host, port))

def thread_sending():
    while True:
        message_to_send = input('Enter Your Message to Send: ')
        if message_to_send:
            message_with_unique_name = unique_name + " : " + message_to_send
            my_socket.send(message_with_unique_name.encode())
        
def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)
        
thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()