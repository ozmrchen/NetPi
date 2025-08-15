# Week 2.1 Lab: Basic Security Checking

## Lab Overview
Use your essential commands to check network security. Find open ports, test connections, and spot potential issues.

**Time Required:** 30 minutes  
**Focus:** Security assessment with `ss`, `ping`, `ip`

---

## Part 1: Check Open Ports (10 minutes)

### Step 1.1: What's Listening?

```bash
# See all open ports (firewall perspective)
ss -tuln
```

**Count and record:**
- Total listening ports: _______
- Ports open to everyone (0.0.0.0): _______
- Local-only ports (127.0.0.1): _______

### Step 1.2: Security Assessment

```bash
# Check for common risky ports
ss -tuln | grep :22     # SSH
ss -tuln | grep :23     # Telnet  
ss -tuln | grep :80     # Web server
ss -tuln | grep :3389   # Remote Desktop
```

**Security questions:**
- Found port 22 (SSH)? Should it be open? _______
- Found port 23 (Telnet)? This is high risk: _______
- Any web servers running? _______

---

## Part 2: Test Network Access (10 minutes)

### Step 2.1: Connectivity Security Test

```bash
# Test if you can reach suspicious/blocked sites
ping -c 1 facebook.com
ping -c 1 reddit.com
ping -c 1 gaming-site.com
```

**Results:** Which sites can you reach? _______

**Question:** Why might some be blocked?

### Step 2.2: Internal Network Scan

```bash
# Test other devices on your network
ping -c 1 192.168.1.1    # Router
ping -c 1 192.168.1.2    # Possible other device
ping -c 1 192.168.1.100  # Another possible device
```

**Devices found:** _______

---

## Part 3: Network Security Info (10 minutes)

### Step 3.1: Your Network Configuration

```bash
# Check your network setup
ip addr show | grep inet
ip route show default
```

**Record:**
- Your IP: _______
- Network range: _______
- Router IP: _______

### Step 3.2: Interface Security

```bash
# Check network interfaces
ip link show
```

**Security check:**
- Using wired (eth0) or wireless (wlan0)? _______
- Which is more secure? _______

---

## Security Assessment Summary

**Rate your network security:**

| Security Check | Result | Risk Level |
|----------------|--------|------------|
| Open ports count | _______ | High/Medium/Low |
| SSH port open | Yes/No | _______ |
| Web servers running | Yes/No | _______ |
| Network type | Wired/Wireless | _______ |

---

## Quick Security Questions

1. **Which is more secure - 3 open ports or 10 open ports?** _______

2. **Should port 22 be open on a home computer?** _______

3. **Is wireless or wired more secure?** _______

4. **If you found 20 devices on your network, is that good or bad?** _______

---

## Lab Results

**Most concerning finding:** _______________________

**Best security practice you observed:** _______________________

**One thing you'd change:** _______________________

---