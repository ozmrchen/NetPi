from scapy.all import IP, ICMP, sr1

host = "8.8.8.8"   # or your router
pkt = IP(dst=host)/ICMP()
reply = sr1(pkt, timeout=2, verbose=0)

print("✅ Reply from", reply.src if reply else "❌ No response")