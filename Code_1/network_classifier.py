def classify_ip(ip):
    if ip.startswith('192.168.') or ip.startswith('10.'):
        return "LAN"
    else:
        return "WAN"

my_ip = "192.168.1.100"  # Replace with yours
print(f"{my_ip} is {classify_ip(my_ip)}")