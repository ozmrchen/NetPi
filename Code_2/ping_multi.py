"""
ping_multi.py
Ping a small set of hosts 4 times each and print summaries.
Works on Raspberry Pi OS (uses `ping -c`).
"""
import subprocess

HOSTS = ["192.168.1.1", "www.google.com", "www.bom.gov.au"]  # edit LAN IP

def ping(host):
    result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
    return result.returncode, result.stdout

if __name__ == "__main__":
    for h in HOSTS:
        code, out = ping(h)
        print(f"\n=== {h} (rc={code}) ===")
        print(out)