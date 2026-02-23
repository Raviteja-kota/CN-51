import socket

host = input("Hostname: ")
port = int(input("Port: "))

s = socket.socket()
s.settimeout(3)

result = s.connect_ex((host, port))
print("OPEN" if result == 0 else "CLOSED")

s.close()
