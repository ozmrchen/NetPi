import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
print(f"My IP: {sock.getsockname()[0]}")
sock.close()