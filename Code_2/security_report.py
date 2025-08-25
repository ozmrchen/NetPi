import socket, datetime


def openp(p):
    try:
        with socket.create_connection(("127.0.0.1", p), timeout=0.5):
            return True
    except Exception:
        return False


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "Unknown"
R = {22: "SSH", 23: "TELNET", 80: "HTTP", 3389: "RDP"}
ops = [p for p in R if openp(p)]
surf = "HIGH" if len(ops) > 2 else "MEDIUM" if ops else "LOW"
print(
    f"\n🔍 SECURITY SCAN REPORT - {datetime.datetime.now():%Y-%m-%d %H:%M}\n📍 System IP: {ip}\n🔓 Open risky ports: {len(ops)}\n🎯 Attack surface: {surf}"
)
print(
    "⚠️  Exposed services: " + ", ".join(f"{p}({R[p]})" for p in ops)
    if ops
    else "✅ No risky services detected"
)
