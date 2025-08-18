from scapy.all import IP, ICMP, sr1
import time

router_ip = "192.168.0.1"   # replace with your router IP
wan_ip = "8.8.8.8"          # Google DNS as WAN target

def ping(host):
    # Build an IP packet to 'host' carrying an ICMP Echo Request (ping)
    pkt = IP(dst=host)/ICMP()
    start = time.time()
    # sr1() → send packet and return first answer only
    reply = sr1(pkt, timeout=2, verbose=0)
    if reply:
        return (time.time() - start) * 1000
    else:
        return None

lan_time = ping(router_ip)
wan_time = ping(wan_ip)

print(f"LAN: {lan_time:.1f} ms" if lan_time else "LAN: no reply")
print(f"WAN: {wan_time:.1f} ms" if wan_time else "WAN: no reply")