import socket
from scapy.all import conf

# My IP (no traffic sent)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_ip = s.getsockname()[0]
s.close()

# Default gateway via OS routing table
_, gw, iface = conf.route.route("8.8.8.8")

print(f"Me: {my_ip} → Router: {gw} (iface {iface})")