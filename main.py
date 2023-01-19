# This code creates a GUI using tkinter where a user can enter a server's name or IP address, specify their port,
# and input a lowercase sentence. This code imports the socket library to create a socket and connect it to the
# specified server and port. When the button "Connect" is pressed, the code runs the function connect() which creates
# a socket, connects it to the server and port, sends the specified lowercase message and prints the modified
# message. If the program does not connect in time, it will show a "timeout error" message. The GUI includes labels
# and an entry box for the user to input their server name/IP address, port, and lowercase sentence, as well as a
# "Connect" button to start the process.process

import socket
import tkinter as tk

window = tk.Tk()
window.title('Speedy Socket')
window.configure(background='#D7E9B9', padx=30, pady=50)

# Labels
l1 = tk.Label(window, text='Example: www.hostname.com',
              font=('Arial Bold', 18), bg='#FFFBAC', fg="#000000", anchor="w")
l2 = tk.Label(window, text='Server Name or IP address:',
              font=('Arial Bold', 18), bg='#FFFBAC', fg="#000000", anchor="w")
l1.grid(column=0, row=0)
l2.grid(column=0, row=1)

serverName = tk.StringVar()
serverName.set("www.example.com")
e1 = tk.Entry(window, textvariable=serverName, width=30, bg='#FFD495', fg="#000000")
e1.grid(column=1, row=1, pady=5)

# Port
l3 = tk.Label(window, text='Server Port:',
              font=('Arial Bold', 18), bg='#FFFBAC', fg="#000000", anchor="w")
l3.grid(column=0, row=2)

serverPort = tk.IntVar()
serverPort.set(80)
e2 = tk.Entry(window, textvariable=serverPort, width=30, bg='#FFD495', fg="#000000")
e2.grid(column=1, row=2, pady=5)

# Message
l4 = tk.Label(window, text='Input lowercase sentence:',
              font=('Arial Bold', 18), bg='#FFFBAC', fg="#000000", anchor="w")
l4.grid(column=0, row=3)

message = tk.StringVar()
message.set("hello world")
e3 = tk.Entry(window, textvariable=message, width=30, bg='#FFD495', fg="#000000")
e3.grid(column=1, row=3, pady=5)


# Connect
def connect():
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # uses TCP instead of UDP
        clientSocket.connect((serverName.get(), serverPort.get()))  # specify serverName and serverPort
        clientSocket.send(message.get().encode())
        modifiedMessage = clientSocket.recv(2048)
        print(modifiedMessage.decode())
        clientSocket.close()
    except TimeoutError:
        print("Timeout error: The operation timed out")


b1 = tk.Button(window, text="Connect", command=connect, bg='#FAAB78', font=('Arial Bold', 18))
b1.grid(column=1, row=4)

window.mainloop()

