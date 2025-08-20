from scapy.all import IP, TCP, sr1

target = "127.0.0.1"     # localhost
ports = [22, 80, 443, 8080, 3306]  # common ports to test
open_ports = []

for port in ports:
    pkt = IP(dst=target)/TCP(dport=port, flags="S")   # TCP SYN
    reply = sr1(pkt, timeout=1, verbose=0)
    if reply and reply.haslayer(TCP) and reply[TCP].flags & 0x12:  # SYN-ACK
        open_ports.append(port)

print(f"Open ports: {len(open_ports)}")
for p in open_ports[:3]:   # Show first 3
    print(f"  {target}:{p}")