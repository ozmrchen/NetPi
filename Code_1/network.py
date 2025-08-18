# show_path.py — real (no hard-coded router), works on macOS & Linux without sudo
from scapy.all import conf
import socket

def my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))         # doesn’t send traffic; picks the outbound iface
        return s.getsockname()[0]
    finally:
        s.close()

def default_gateway():
    # Ask OS routing table which gateway/interface would reach 8.8.8.8
    _, gw, iface = conf.route.route("8.8.8.8")
    return gw, iface

me = my_ip()
gw, iface = default_gateway()

if gw == "0.0.0.0":
    print(f"Me: {me} → (direct on {iface}) → Internet")
else:
    print(f"Me: {me} → Router: {gw} (via {iface}) → Internet")