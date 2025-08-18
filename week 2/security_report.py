from find_my_ip import get_local_ip
import socket

def check_common_ports():
    """Check a few common ports on localhost to see if they're open."""
    common_ports = [22, 80, 443, 8080]  # SSH, HTTP, HTTPS, Alt HTTP
    open_ports = []
    
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Quick timeout to avoid delays
            result = sock.connect_ex(("127.0.0.1", port))
            sock.close()
            if result == 0:  # 0 means the port is open
                open_ports.append(port)
        except socket.error:
            pass  # Skip errors quietly for simplicity
    
    return open_ports

# Generate a simple security report
print("🛡️ Security Report")
ip = get_local_ip()
print(f"Local IP Address: {ip}")

ports = check_common_ports()
print(f"Open Ports: {len(ports)}")
if ports:
    print(f"Ports in use: {ports}")
else:
    print("No common ports (22, 80, 443, 8080) are open.")