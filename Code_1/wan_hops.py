from scapy.all import IP, ICMP, sr1

target = "google.com"
max_hops = 5

print(f"Tracing route to {target} (max {max_hops} hops):")

for ttl in range(1, max_hops + 1):
    pkt = IP(dst=target, ttl=ttl) / ICMP()
    reply = sr1(pkt, timeout=2, verbose=0)

    if reply is None:
        print(f"{ttl}: * (no reply)")
        continue

    print(f"{ttl}: {reply.src}")

    if reply.type == 0:  # Echo reply → destination reached
        break