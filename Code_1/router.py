# router.py (macOS-friendly, no sudo)
from scapy.all import conf

# Route to an external IP; Scapy reads the OS routing table
_, gw, iface = conf.route.route("8.8.8.8")
print(f"Router: {gw} (via {iface})")