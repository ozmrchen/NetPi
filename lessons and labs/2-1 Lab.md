# Week 2.1 Lab: Exploring Network Security Components

## Lab Overview
In this lab, you'll explore your computer's network connections, understand what services are running, and get hands-on experience with basic network security tools.

**Time Required:** 45 minutes  
**Environment:** GitHub Codespaces or Raspberry Pi 4  
**Difficulty:** Beginner

---

## Learning Objectives
By the end of this lab, you will be able to:
- Use command-line tools to examine network connections
- Identify running network services on your system
- Understand what network traffic looks like
- Recognise normal vs suspicious network activity

---

## Pre-Lab Setup

### Option A: GitHub Codespaces
1. Open your NetPi repository in Codespaces
2. Open a new terminal
3. You're ready to go!

### Option B: Raspberry Pi 4
1. Boot your Raspberry Pi and open Terminal
2. Ensure you're connected to the network
3. Test connectivity: `ping -c 3 google.com`

---

## Part 1: Discovering Your Network Connections

### Step 1.1: Check Active Network Connections

Let's see what network connections your computer currently has:

```bash
# Modern way to view network connections
ss -tuln
```

**What you're seeing:**
- `t` = TCP connections
- `u` = UDP connections  
- `l` = Listening (waiting for connections)
- `n` = Show numbers instead of names

**Your Output Should Look Like:**
```
State    Recv-Q   Send-Q     Local Address:Port      Peer Address:Port
LISTEN   0        511        0.0.0.0:8080           0.0.0.0:*
LISTEN   0        128        127.0.0.1:22           0.0.0.0:*
```

### Step 1.2: Understanding the Output

**Record your observations:**

1. **How many LISTEN connections do you see?** ________________

2. **What ports are your system listening on?** ________________

3. **Which connections are only local (127.0.0.1)?** ________________

### Step 1.3: Alternative Method (Older Command)

Try the traditional command:

```bash
# Traditional way (older systems)
netstat -tuln
```

**Question:** Do you see the same information? What's different?

---

## Part 2: Identifying Running Services

### Step 2.1: What's Using Those Ports?

Let's find out what programs are using network ports:

```bash
# Show processes using network connections
ss -tulnp
```

The `p` flag shows the **process** (program) using each port.

**Note:** You might see "users:()" for some connections - this means you don't have permission to see that process information.

### Step 2.2: Research Common Ports

Look up what these common ports are used for:

| Port Number | Service Name | What It's Used For |
|-------------|--------------|-------------------|
| 22          |              |                   |
| 80          |              |                   |
| 443         |              |                   |
| 8080        |              |                   |

**Hint:** Search online for "port 22 service" etc.

---

## Part 3: Testing Network Connectivity

### Step 3.1: Basic Connectivity Tests

Test if you can reach different servers:

```bash
# Test basic connectivity
ping -c 3 google.com
ping -c 3 abc.net.au
ping -c 3 8.8.8.8
```

**Record your results:**
- Google: ⏱️ Average time: _______ ms
- ABC News: ⏱️ Average time: _______ ms  
- Google DNS: ⏱️ Average time: _______ ms

### Step 3.2: Trace Network Path

See the path your data takes to reach a destination:

```bash
# Trace route to ABC News (Australian site)
traceroute abc.net.au
```

**Questions:**
1. How many "hops" (steps) does it take? ________________
2. Can you identify your router/gateway? ________________
3. Do you see any Australian network names? ________________

---

## Part 4: Understanding Network Security

### Step 4.1: Check HTTP vs HTTPS

Let's see the difference between secure and insecure connections:

```bash
# Check website security headers
curl -I http://neverssl.com
echo "--- SECURE SITE ---"
curl -I https://www.abc.net.au
```

**Compare the outputs:**
- What's different in the headers?
- Which one would a firewall treat differently?

### Step 4.2: Simulate a Simple Port Scan

**⚠️ Important:** Only scan your own system!

```bash
# Scan your own system for open ports
# This shows what an attacker might see
nc -zv localhost 1-1000 2>&1 | grep succeeded
```

**What you found:**
- List the open ports: ________________
- Should these be open? Why/why not?

---

## Part 5: Monitoring Network Activity

### Step 5.1: Real-Time Connection Monitoring

Open a second terminal and run:

```bash
# Terminal 1: Monitor connections in real-time
watch -n 2 'ss -tuln | wc -l'
```

```bash
# Terminal 2: Create some network activity
curl https://www.google.com
curl https://github.com
ping -c 5 reddit.com
```

**Observation:** Did the number of connections change?

### Step 5.2: Check System Logs (If Available)

```bash
# Look for network-related log entries
sudo tail -20 /var/log/syslog | grep -i network
```

**Note:** This might not work in Codespaces due to permissions.

---

## Reflection Questions

### Security Analysis

1. **Firewall Perspective:** If you were configuring a firewall for your system, which ports would you:
   - ✅ **Allow:** ________________________________
   - ❌ **Block:** ________________________________

2. **Threat Detection:** What network activity might indicate a security problem?
   _______________________________________________

3. **Normal vs Suspicious:** From what you observed, what seems like normal network behaviour?
   _______________________________________________

### Real-World Applications

4. **School Network:** How might your school's network administrator use these tools?
   _______________________________________________

5. **Home Network:** What could you check at home to ensure your Wi-Fi is secure?
   _______________________________________________

---

## Extension Activities (If Time Permits)

### Advanced: Create a Network Summary Script

Create a simple bash script to summarise your network status:

```bash
# Create file: network_summary.sh
nano network_summary.sh
```

```bash
#!/bin/bash
echo "=== Network Security Summary ==="
echo "Date: $(date)"
echo "Listening Ports: $(ss -tln | wc -l)"
echo "Active Connections: $(ss -tn | wc -l)"
echo "Can reach Google: $(ping -c 1 google.com > /dev/null && echo 'YES' || echo 'NO')"
echo "=== End Summary ==="
```

```bash
# Make it executable and run
chmod +x network_summary.sh
./network_summary.sh
```

---

## Lab Submission

**Complete this summary:**

1. **Number of listening ports found:** ________________
2. **Most concerning open port (if any):** ________________
3. **Average ping time to Australian site:** ________________
4. **One thing that surprised you:** ________________________________
5. **One security improvement you'd suggest:** ________________________________

**Save your terminal output:**
```bash
# Save your findings
ss -tulnp > my_network_connections.txt
ping -c 3 abc.net.au >> my_network_connections.txt
```

---

## Troubleshooting

**If commands don't work:**
- `ss` not found → try `netstat -tuln`
- `traceroute` not found → try `tracepath`
- Permission denied → some commands need `sudo` (not available in Codespaces)
- No internet → check your connection with `ping 8.8.8.8`

**Need help?** Ask your teacher or a classmate!

---

## Next Steps

In our next **Code Practice** session, we'll build a Python script that automates some of these checks and creates our own simple network security scanner!