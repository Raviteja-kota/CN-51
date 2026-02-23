import socket
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
public_ip = s.getsockname()[0]
s.close()
print("Hostname:", hostname)
print("Local IP:", local_ip)
print("Public IP:", public_ip)