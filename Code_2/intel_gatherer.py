import socket, subprocess


def sh(a):
    return subprocess.run(a, capture_output=True, text=True).stdout


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    try:
        s.connect(("8.8.8.8", 80))
        my_ip = s.getsockname()[0]
    except Exception:
        my_ip = "Unknown"
hops = sum(
    1 for ln in sh(["traceroute", "-m", "5", "8.8.8.8"]).splitlines()[1:] if ln.strip()
)
svc = sh(["ss", "-tuln"])
open_all = svc.count("0.0.0.0:")
print(
    f"🏠 My IP: {my_ip}\n🛣️  Internet hops: {hops}\n🌍 Services open to world: {open_all}\n⚠️  Risk level: {'HIGH' if open_all > 3 else 'MEDIUM' if open_all > 0 else 'LOW'}"
)
