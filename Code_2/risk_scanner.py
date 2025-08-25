import subprocess


def sh(a):
    return subprocess.run(a, capture_output=True, text=True)


gw = "Unknown"
for ln in sh(["ip", "route"]).stdout.splitlines():
    if ln.startswith("default "):
        gw = ln.split()[2]
        break
ping1 = lambda h: sh(["ping", "-c", "1", "-W", "1", h]).returncode == 0
print(
    f"🏠 Local:{'✅' if ping1('127.0.0.1') else '❌'} | 🌐 Router:{'✅' if gw != 'Unknown' and ping1(gw) else '❌'} | 🌍 Internet:{'✅' if ping1('8.8.8.8') else '❌'}"
)
print(f"Gateway: {gw}")
