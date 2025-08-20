from scapy.all import IP, ICMP, TCP, sr1

# Test connectivity with ICMP
pkt = IP(dst="google.com")/ICMP()
reply = sr1(pkt, timeout=2, verbose=0)
ping_ok = reply is not None

# Check some common ports on localhost
target = "127.0.0.1"
test_ports = [22, 80, 443, 8080, 3306]
open_ports = []

for port in test_ports:
    syn = IP(dst=target)/TCP(dport=port, flags="S")
    ans = sr1(syn, timeout=1, verbose=0)
    if ans and ans.haslayer(TCP) and ans[TCP].flags == 0x12:  # SYN-ACK
        open_ports.append(port)

print(f"Internet: {'✅' if ping_ok else '❌'} | Open ports: {len(open_ports)}")
if open_ports:
    print("Ports:", ", ".join(str(p) for p in open_ports))