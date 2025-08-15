You're absolutely right! That's way too overwhelming for beginners. Let me redesign this with much simpler, bite-sized code examples.

# Week 2.1 Code Practice: Simple Network Security Checker

## Code Practice Overview
Learn network security concepts through small, simple Python scripts. Each example is under 10 lines and focuses on one concept.

**Time Required:** 45 minutes  
**Python Level:** Complete Beginner  
**Rule:** No code example longer than 10 lines!

---

## Part 1: Can We Connect? (10 minutes)

### Step 1.1: Test One Connection

Create `test_connection.py`:

```python
# test_connection.py
import socket

print("Testing if Google is reachable...")
sock = socket.socket()
result = sock.connect_ex(('google.com', 80))

if result == 0:
    print("✅ Google is reachable!")
else:
    print("❌ Cannot reach Google")
    
sock.close()
```

**Run it:** `python3 test_connection.py`

**Questions:**
1. What does the number `80` mean?
2. What would happen if Google was down?

---

## Part 2: Check One Port (10 minutes)

### Step 2.1: Is Someone Home?

Create `check_port.py`:

```python
# check_port.py
import socket

# Check if port 22 is open on your computer
sock = socket.socket()
sock.settimeout(1)  # Wait 1 second max

result = sock.connect_ex(('localhost', 22))

if result == 0:
    print("🟢 Port 22 is OPEN")
    print("Someone is listening!")
else:
    print("🔴 Port 22 is CLOSED")
    print("Nobody home!")

sock.close()
```

**Run it:** `python3 check_port.py`

**Experiment:**
- Try port 80: `('localhost', 80)`
- Try port 443: `('localhost', 443)`
- Try port 9999: `('localhost', 9999)`

---

## Part 3: Check Multiple Ports (10 minutes)

### Step 3.1: Loop Through Ports

Create `scan_ports.py`:

```python
# scan_ports.py
import socket

ports_to_check = [22, 80, 443, 8080]

print("Checking common ports...")

for port in ports_to_check:
    sock = socket.socket()
    sock.settimeout(0.5)
    result = sock.connect_ex(('localhost', port))
    
    if result == 0:
        print(f"Port {port}: 🟢 OPEN")
    else:
        print(f"Port {port}: 🔴 CLOSED")
    
    sock.close()
```

**Run it:** `python3 scan_ports.py`

**Modify it:**
- Add port 3000 to the list
- Change `localhost` to `google.com`
- Try different websites

---

## Part 4: Make It a Function (10 minutes)

### Step 4.1: Reusable Code

Create `port_function.py`:

```python
# port_function.py
import socket

def is_port_open(host, port):
    """Check if a port is open. Returns True or False."""
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Test the function
print("Testing our function...")
print(f"Google port 80: {is_port_open('google.com', 80)}")
print(f"Google port 22: {is_port_open('google.com', 22)}")
print(f"Local port 22: {is_port_open('localhost', 22)}")
```

**Run it:** `python3 port_function.py`

**Questions:**
1. Why do we return `True` or `False`?
2. What's the advantage of using a function?

---

## Part 5: Security Report (10 minutes)

### Step 5.1: Simple Security Check

Create `security_check.py`:

```python
# security_check.py
import socket

def check_security(host):
    """Check if common risky ports are open"""
    risky_ports = [22, 23, 3389]  # SSH, Telnet, Remote Desktop
    
    print(f"Security check for {host}:")
    
    for port in risky_ports:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            print(f"⚠️  Port {port} is OPEN - could be risky!")
        else:
            print(f"✅ Port {port} is CLOSED - good!")

# Check your own computer
check_security('localhost')
```

**Run it:** `python3 security_check.py`

**Discussion:**
- Which ports should worry a network administrator?
- Why is port 22 sometimes risky?

---

## Mini Challenges (5 minutes each)

### Challenge 1: Website Checker
```python
# website_checker.py
import socket

websites = ['google.com', 'abc.net.au', 'github.com']

for site in websites:
    sock = socket.socket()
    sock.settimeout(2)
    result = sock.connect_ex((site, 443))
    
    if result == 0:
        print(f"✅ {site} has HTTPS")
    else:
        print(f"❌ {site} no HTTPS found")
    
    sock.close()
```

### Challenge 2: Port Guesser
```python
# port_guesser.py
import socket

# Try to find ANY open port on your system
for port in range(8000, 8010):
    sock = socket.socket()
    sock.settimeout(0.1)
    result = sock.connect_ex(('localhost', port))
    
    if result == 0:
        print(f"🎉 Found open port: {port}")
        break
    
    sock.close()
else:
    print("No open ports found in range 8000-8010")
```

---

## What You've Learned

**Network Concepts:**
- Ports are like doors on a computer
- Open ports = services running
- Closed ports = nothing listening
- Some ports are riskier than others

**Python Skills:**
- Using the `socket` library
- Functions that return True/False
- Loops to check multiple items
- Basic error handling with timeouts

**Security Thinking:**
- Fewer open ports = better security
- Network scanning is how attackers explore
- Firewalls block ports to protect systems

---

## Quick Quiz

**Answer in one sentence:**

1. What does `result == 0` mean when checking a port?

2. Why do we use `sock.settimeout(1)`?

3. Which is more secure: 5 open ports or 1 open port?

4. What would a firewall do with an open port 23 (Telnet)?

---

## Extension: Build Your Own

Pick ONE to try:

**Option A: Speed Test**
```python
# How fast can you check 10 ports?
import time
start_time = time.time()
# ... your port checking code ...
end_time = time.time()
print(f"Took {end_time - start_time:.2f} seconds")
```

**Option B: Save Results**
```python
# Save results to a file
with open('scan_results.txt', 'w') as f:
    f.write("My security scan results:\n")
    # ... your scanning code ...
    f.write(f"Port {port}: {status}\n")
```
