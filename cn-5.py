import socket
import requests

# Local IP
local_ip = socket.gethostbyname(socket.gethostname())

# Public IP
public_ip = requests.get("https://api.ipify.org").text

print("Local IP:", local_ip)
print("Public IP:", public_ip)