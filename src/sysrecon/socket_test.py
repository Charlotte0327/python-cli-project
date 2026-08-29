import socket 

target = "10.10.10.20"
port = "22"

try:
    socket.create_connection((target, port), timeout = 1)  # Don't wait longer than a second
    print("Port is open")

except ConnectionRefusedError:
    print("Port is closed")

except TimeoutError:
    print("Connection timed out")