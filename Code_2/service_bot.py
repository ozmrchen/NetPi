import socket, contextlib

COMMON = [21, 22, 23, 53, 80, 110, 143, 443, 993, 995]
N = {
    "21": "FTP",
    "22": "SSH",
    "23": "TELNET",
    "53": "DNS",
    "80": "HTTP",
    "443": "HTTPS",
}


def openp(p):
    with contextlib.suppress(Exception):
        with socket.create_connection(("127.0.0.1", p), timeout=0.5):
            return True
    return False


ops = [p for p in COMMON if openp(p)]
for p in ops:
    print(f"🔓 Port {p} ({N.get(str(p), 'Unknown')})")
print(f"\n📊 Security Score: {max(0, 10 - len(ops))}/10")
