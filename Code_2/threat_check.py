import socket

RISKY = [22, 23, 80, 445, 3389, 5000, 8080, 8888]  # Common risky + development ports


def is_open(p, host="127.0.0.1", t=0.5):
    try:
        with socket.create_connection((host, p), timeout=t):
            return True
    except Exception:
        return False


for p in RISKY:
    print(f"Port {p}: {'🚨 OPEN' if is_open(p) else '✅ CLOSED'}")
