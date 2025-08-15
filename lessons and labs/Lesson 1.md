# NetPi Week 1 Lesson — Network Fundamentals & Linux Basics

**Self-Study Guide for Lab Sheet Activities**

---

## 🎯 Learning Goals

By the end of this lesson, you will:

- Understand what an IP address, hostname, and MAC address are
- Know how to use basic Linux networking commands
- Write simple Python code to gather network information
- Test network connectivity using both CLI and Python

---

## 📚 Background Knowledge You Need

### What is Networking?

Think of networking like the postal system:

- **Your computer** is like your house
- **IP Address** is like your postal address (e.g., 192.168.1.100)
- **Hostname** is like the name on your mailbox (e.g., "raspberrypi")
- **MAC Address** is like a unique serial number for your network card
- **Router/Gateway** is like the local post office that forwards mail
- **DNS** is like a phone book that converts names (google.com) to addresses (172.217.164.142)

### Key Terms Explained

- **IP Address**: A unique number that identifies your computer on the network (like 192.168.1.50)
- **Hostname**: A human-friendly name for your computer (like "raspberrypi" or "johns-laptop")
- **MAC Address**: A permanent hardware identifier for your network card
- **Gateway**: The router that connects your local network to the internet
- **DNS**: Domain Name System - converts website names to IP addresses
- **Ping**: A test to see if another computer is reachable and how fast it responds

---

## 🔧 Getting Started

### Opening the Terminal

1. **On Raspberry Pi**: Click the terminal icon (black square) in the taskbar
2. **In Codespaces**: Terminal is already open at the bottom

### Opening Thonny (Python Editor)

1. **On Raspberry Pi**: Menu → Programming → Thonny Python IDE
2. **In Codespaces**: Create a new `.py` file and edit it

---

## 📖 Activity 1 Guide — Network Information

### Understanding `ifconfig`

The `ifconfig` command shows all your network interfaces (like ethernet and WiFi cards).

```bash
ifconfig
```

**What you'll see:**

```
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255
        ether b8:27:eb:xx:xx:xx  txqueuelen 1000  (Ethernet)
```

**How to read this:**

- `eth0` = Name of your ethernet (wired) network interface
- `inet 192.168.1.100` = **Your IP Address**
- `ether b8:27:eb:xx:xx:xx` = **Your MAC Address**
- `UP,RUNNING` = Interface is active and working

### Finding Your Gateway

The gateway is your router - the device that connects you to the internet.

```bash
ip route show default
```

**Example output:**

```
default via 192.168.1.1 dev eth0
```

- `192.168.1.1` = **Your Gateway IP** (usually ends in .1 or .254)

### Common Issues & Solutions

❌ **"Command not found"**: Try `ip a` instead of `ifconfig`  
❌ **"No output"**: Your network interface might be down  
❌ **"Permission denied"**: This shouldn't happen with these commands

---

## 📖 Activity 2 Guide — Hostname and Ping

### Finding Your Computer Name

```bash
hostname
```

This shows the name your computer uses on the network. It's usually something like `raspberrypi` or `codespace-xxxx`.

### Testing Connectivity with Ping

Ping sends a small message to another computer and measures how long it takes to get a reply.

```bash
ping -c 4 google.com
```

**What the flags mean:**

- `-c 4` = Send only 4 ping packets (otherwise it continues forever)
- `google.com` = The target we're testing

**Understanding ping output:**

```
64 bytes from google.com (172.217.164.142): icmp_seq=1 ttl=54 time=23.4 ms
```

- `time=23.4 ms` = **Response time** (lower is faster)
- `icmp_seq=1` = Packet number (helps detect lost packets)

**At the end you'll see:**

```
4 packets transmitted, 4 received, 0% packet loss
round-trip min/avg/max/stddev = 20.1/23.4/28.1/2.8 ms
```

- `0% packet loss` = All packets reached the destination (good!)
- `avg/max/stddev = 23.4` = **Average response time**

### Common Issues & Solutions

❌ **"ping: google.com: Name or service not known"**: DNS problem - try `ping 8.8.8.8` instead  
❌ **"Network is unreachable"**: Check your internet connection  
❌ **"100% packet loss"**: Target might be blocking ping or network is down

---

## 📖 Activity 3 Guide — Python Network Basics

### Why Use Python for Networking?

- Automate repetitive tasks
- Get information in a format you can use in programs
- Build tools that work across different operating systems

### Understanding the Code

```python
import socket
```

This loads Python's networking library - like getting tools from a toolbox.

```python
computer_name = socket.gethostname()
```

This asks the operating system "What's my computer's name?" and stores the answer.

```python
ip_address = socket.gethostbyname(computer_name)
```

This asks "What IP address is associated with my computer name?"

### Running Python Code

1. **In Thonny**: Type the code, then click the green "Run" button
2. **In terminal**: Save as `test.py`, then run `python3 test.py`

### Common Issues & Solutions

❌ **"ModuleNotFoundError"**: The `socket` module should always be available  
❌ **"Name resolution error"**: Your computer's hostname might not be set up properly  
❌ **Different results from CLI**: This is normal - Python and CLI tools sometimes use different methods

---

## 📖 Activity 4 Guide — Network Routes and DNS

### Understanding Network Routes

Think of routes like directions:

```bash
ip route show default
```

This shows the path your computer takes to reach the internet.

### DNS (Domain Name System)

DNS converts human-readable names to IP addresses:

```bash
nslookup google.com
```

**You'll see:**

```
Server:    192.168.1.1
Address:   192.168.1.1#53

Non-authoritative answer:
Name:   google.com
Address: 172.217.164.142
```

- `Server: 192.168.1.1` = Your DNS server (usually your router)
- `Address: 172.217.164.142` = Google's actual IP address

### Active Network Connections

```bash
ss -tuln
```

Shows what network services are running on your computer:

- `t` = TCP connections
- `u` = UDP connections
- `l` = Listening (waiting for connections)
- `n` = Show numbers instead of names

---

## 📖 Activity 5 & 6 Guide — Python Connectivity Testing

### Understanding Socket Connections

```python
socket.create_connection(("google.com", 80), timeout=3)
```

**Breaking this down:**

- `google.com` = Target server
- `80` = Port number (80 is for web traffic)
- `timeout=3` = Give up after 3 seconds

### Try-Except Error Handling

```python
try:
    # Try to do something
    socket.create_connection(("google.com", 80), timeout=3)
    print("✅ Connection successful!")
except:
    # If it fails, do this instead
    print("❌ Connection failed")
```

This prevents your program from crashing if something goes wrong.

### Modifying the Code

To test a different website, just change the hostname:

```python
socket.create_connection(("github.com", 80), timeout=3)
```

---

## 🔧 Troubleshooting Guide

### Network Connection Issues

1. **Check physical connection** (ethernet cable, WiFi)
2. **Test with known good sites**: `ping 8.8.8.8` (Google's DNS)
3. **Check if DNS is working**: `nslookup google.com`
4. **Restart networking**: `sudo systemctl restart networking` (if allowed)

### Python Issues

1. **Import errors**: Make sure you're using `python3`, not `python`
2. **Syntax errors**: Check spelling and indentation
3. **Connection timeouts**: Try increasing timeout or testing different sites

### Command Not Found

- **Try alternatives**: `ip a` instead of `ifconfig`
- **Install missing tools**: `sudo apt install net-tools` (if you have permission)

---

## 🎯 Self-Check Questions

After completing the lab, you should be able to answer:

1. **What's the difference between your computer's IP address and its hostname?**
2. **Why might ping times vary between different websites?**
3. **What does it mean if `ping` shows "100% packet loss"?**
4. **How does Python's `socket.create_connection()` differ from the `ping` command?**
5. **What's the purpose of a default gateway?**

---

## 🚀 Going Further (Optional)

If you finish early, try these challenges:

### Challenge 1: Create a Network Scanner

Modify the Python code to test multiple websites at once.

### Challenge 2: Compare Different DNS Servers

Try changing your DNS to 8.8.8.8 and see if websites resolve faster.

### Challenge 3: Monitor Your Connection

Write a Python script that pings a website every 10 seconds and reports if it's up or down.

---

## 📝 Key Takeaways

- **CLI tools** like `ping` and `ifconfig` are powerful for network diagnostics
- **Python** can automate network tasks and present information clearly
- **IP addresses** are how computers find each other on networks
- **Ping** is a fundamental tool for testing connectivity
- **DNS** translates human-readable names to IP addresses
- **Understanding your network setup** helps troubleshoot problems

---

## 💡 Tips for Success

1. **Don't just copy commands** - read the explanations to understand what's happening
2. **Try variations** - change hostnames, try different websites
3. **Compare results** - CLI vs Python often show different perspectives on the same information
4. **Ask "why?"** - If something doesn't work, think about what might be causing it
5. **Practice** - The more you use these tools, the more comfortable you'll become

