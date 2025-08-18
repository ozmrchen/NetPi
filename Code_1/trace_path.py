from scapy.all import IP, ICMP, sr1

target = "google.com"
max_hops = 5
hops = 0

for ttl in range(1, max_hops + 1):
    pkt = IP(dst=target, ttl=ttl)/ICMP()   # send ICMP Echo with TTL
    reply = sr1(pkt, timeout=2, verbose=0)
    if reply:
        hops += 1
        if reply.type == 0:  # Echo reply → reached destination
            break

print(f"Path to {target}: {hops} hops")
if hops > 10:
    print("Long path - might be slow")