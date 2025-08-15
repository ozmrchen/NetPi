# NetPi Week 1 Lab Sheet — Network Fundamentals & Linux Basics

**Code Repository:** `https://github.com/ozmrchen/NetPi`

---

## Activity 1 — Identify Local Network Information

1. Open the **terminal** on your Raspberry Pi
2. Run the following command:
   ```bash
   ifconfig
   ```
3. Fill in the table below:

| Item            | Value |
| --------------- | ----- |
| IP Address      |       |
| MAC Address     |       |
| Default Gateway |       |

4. Now try the simpler command:
   ```bash
   ip addr show
   ```
   
**Question:** What's the difference between `ifconfig` and `ip addr show` output?

**Answer:** _______________________________________________

---

## Activity 2 — Find Your Hostname and Test Basic Connectivity

1. In the terminal, run:
   ```bash
   hostname
   ```
2. Record your hostname: _______________________________________________

3. Test if you can reach Google:
   ```bash
   ping -c 4 google.com
   ```
4. Record the average response time: _________ ms

5. Test another website:
   ```bash
   ping -c 4 github.com
   ```
6. Record the average response time: _________ ms

---

## Activity 3 — Simple Python Network Tool

1. Open **Thonny** on your Raspberry Pi
2. Run the **`network_info.py`** script:

```python
"""
Show basic network information using Python
"""
import socket

# Get computer name
computer_name = socket.gethostname()
print(f"Computer name: {computer_name}")

# Get IP address
ip_address = socket.gethostbyname(computer_name)
print(f"IP address: {ip_address}")
```

3. Compare the Python results with your CLI results:

| Method | Computer Name | IP Address |
|--------|---------------|------------|
| CLI (hostname) | | |
| Python | | |

**Question:** Are the results the same? 

**Answer:** _______________________________________________

---

## Activity 4 — Explore Network Routes

1. Find your default gateway:
   ```bash
   ip route show default
   ```
2. Record the gateway IP: _______________________________________________

3. Test connectivity to your gateway:
   ```bash
   ping -c 3 [gateway-ip]
   ```
   Replace `[gateway-ip]` with the IP you found above.

4. Check what DNS servers you're using:
   ```bash
   cat /etc/resolv.conf
   ```
5. Record your DNS server: _______________________________________________

---

## Activity 5 — Network Troubleshooting Commands

Try these useful network commands:

1. **Check active connections:**
   ```bash
   ss -tuln
   ```

2. **Test DNS lookup:**
   ```bash
   nslookup google.com
   ```

3. **Trace route to website:**
   ```bash
   traceroute google.com
   ```
   *(This might take a while - you can stop it with Ctrl+C)*

**Question:** How many "hops" did it take to reach Google? 

**Answer:** _______________________________________________

---

## Activity 6 — Simple Python Connectivity Test

1. Create and run this simple Python script:

```python
"""
Test if we can connect to a website
"""
import socket

print("Testing connection to Google...")

try:
    socket.create_connection(("google.com", 80), timeout=3)
    print("✅ Connection successful!")
except:
    print("❌ Connection failed")
```

2. Modify the script to test a different website
3. What website did you test? _______________________________________________
4. Did it work? _______________________________________________

---

## Homework — Compare CLI vs Python

**Task:** 
1. Use the `ping` command to test 3 different websites
2. Record the response times
3. Then modify the Python script from Activity 6 to test the same 3 websites

**Comparison Table:**

| Website | CLI Ping Time | Python Result |
|---------|---------------|---------------|
| | | |
| | | |
| | | |

**Reflection:** Which method (CLI or Python) gives you more information? Why?

**Answer:** _______________________________________________

---

## Key Commands Learned

- `ifconfig` - Show network interface information
- `hostname` - Show computer name  
- `ping` - Test connectivity and measure response time
- `ip route` - Show network routing information
- `nslookup` - Test DNS resolution
- `ss` - Show active network connections

## Python Concepts Introduced

- `socket.gethostname()` - Get computer name
- `socket.gethostbyname()` - Convert hostname to IP
- `socket.create_connection()` - Test if we can connect to a service

---

## Notes

This approach builds CLI familiarity first, then introduces Python as a tool to do similar tasks, helping students understand the connection between command-line networking and programming.