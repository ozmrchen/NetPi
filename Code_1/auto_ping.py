from scapy.all import IP, ICMP, sr1

hosts = ['127.0.0.1', '192.168.1.1', 'google.com']

for host in hosts:
    pkt = IP(dst=host)/ICMP()   # build ICMP echo request
    reply = sr1(pkt, timeout=2, verbose=0)
    print(f"{host}: {'✅ UP' if reply else '❌ DOWN'}")