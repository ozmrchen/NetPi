from scapy.all import conf

# Check if there’s a default route through a private LAN range
_, gw, iface = conf.route.route("8.8.8.8")

if gw.startswith("192.168.") or gw.startswith("10."):
    print("✅ Connected to LAN")
else:
    print("❌ Not on a private LAN")