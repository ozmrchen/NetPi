# Week 2.1 Code Practice: Security Scanner

## Simple Security Automation
**Time:** 20 minutes | **Rule:** Maximum 5 lines per script!

---

## Script 1: Port Security Check (5 minutes)

Create `port_check.py`:

```python
import subprocess
result = subprocess.run(['ss', '-tuln'], capture_output=True, text=True)
open_ports = [line for line in result.stdout.split('\n') if 'LISTEN' in line]
risky_ports = [line for line in open_ports if ':22' in line or ':23' in line]
print(f"Open ports: {len(open_ports)} | Risky ports: {len(risky_ports)}")
```

**Run:** `python3 port_check.py`

---

## Script 2: Connectivity Tester (5 minutes)

Create `connection_test.py`:

```python
import subprocess
sites = ['google.com', 'facebook.com', 'github.com']
for site in sites:
    result = subprocess.run(['ping', '-c', '1', site], capture_output=True)
    status = "✅ Reachable" if result.returncode == 0 else "❌ Blocked"
    print(f"{site}: {status}")
```

**Run:** `python3 connection_test.py`

---

## Script 3: Security Risk Assessment (5 minutes)

Create `security_risk.py`:

```python
import subprocess
ports = subprocess.run(['ss', '-tuln'], capture_output=True, text=True)
port_count = len([l for l in ports.stdout.split('\n') if 'LISTEN' in l])
risk = "HIGH" if port_count > 10 else "MEDIUM" if port_count > 5 else "LOW"
print(f"Open ports: {port_count} | Security risk: {risk}")
```

**Run:** `python3 security_risk.py`

---

## Script 4: Quick Security Report (5 minutes)

Create `security_report.py`:

```python
import subprocess, socket
# Get network info
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
my_ip = sock.getsockname()[0]
# Check ports
ports = len([l for l in subprocess.run(['ss', '-tuln'], capture_output=True, text=True).stdout.split('\n') if 'LISTEN' in l])
print(f"🛡️ Security Report\nIP: {my_ip} | Open ports: {ports}")
```

**Run:** `python3 security_report.py`

---

## Challenge: Firewall Simulator

Create `firewall_sim.py`:

```python
def check_port_risk(port_num):
    risky_ports = [22, 23, 3389, 21]
    return "🔴 HIGH RISK" if port_num in risky_ports else "🟢 LOW RISK"

test_ports = [22, 80, 443, 23]
for port in test_ports:
    print(f"Port {port}: {check_port_risk(port)}")
```

**Run:** `python3 firewall_sim.py`

---

## What You Learned
- **Automated security scanning:** Python can check ports like a firewall
- **Risk assessment:** Count and categorise security threats
- **Connectivity testing:** Automate network reachability tests
- **Security reporting:** Combine multiple checks into reports

---

## Quick Test
1. What makes a port "risky"?
2. Why automate security checks?
3. How does this relate to firewall rules?
