from scapy.all import conf, IP, ICMP, sr1
import socket

# My IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
my_ip = s.getsockname()[0]
s.close()

# Router (default gateway)
_, gw, iface = conf.route.route("8.8.8.8")

# WAN check
pkt = IP(dst="8.8.8.8")/ICMP()
wan = sr1(pkt, timeout=2, verbose=0)

print("WPAN: Bluetooth devices near me")
print(f"LAN : My IP {my_ip} → Router {gw}")
print("WAN : Internet reachable" if wan else "WAN : No reply")