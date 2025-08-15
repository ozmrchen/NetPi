# Week 2.1 Lesson: Network Security Components

## Learning Objectives
By the end of this lesson, you will be able to:
- Explain what a firewall does and why it's important
- Identify different types of network security threats
- Understand how intrusion detection works
- Recognise security components in real-world networks

---

## What is Network Security?

Think of network security like protecting your home. You wouldn't leave your front door wide open with a sign saying "Welcome, take anything you want!" Networks need similar protection.

**Network security** is about protecting:
- **Data** (your personal information, photos, messages)
- **Systems** (computers, phones, servers)
- **Access** (who can connect and what they can do)

### Australian Context
In Australia, we have strict privacy laws (Privacy Act 1988) that require organisations to protect personal data. When Optus had their data breach in 2022, it affected 9.8 million customers because their network security failed.

---

## Firewalls: Your Digital Security Guard

### What is a Firewall?

A **firewall** is like a security guard at the entrance of a building. It checks everyone coming and going, and only lets through people who are supposed to be there.

#### Real-World Analogy
Imagine your school has a security guard who:
- ✅ Lets students and teachers enter during school hours
- ❌ Stops strangers from wandering in
- ✅ Allows authorised visitors with appointments
- ❌ Blocks people trying to enter at 2 AM

A firewall does the same thing for network traffic.

### How Firewalls Work

Firewalls examine **every piece of data** (called packets) trying to enter or leave a network. They check:

1. **Where is it coming from?** (Source IP address)
2. **Where is it going?** (Destination IP address)  
3. **What type of data is it?** (Port number and protocol)
4. **Is this allowed?** (Check against security rules)

### Types of Firewall Rules

**ALLOW Rules** (Green Light 🟢)
- Let web browsing traffic through (port 80, 443)
- Allow email to be sent (port 25, 587)
- Permit file sharing within the office network

**BLOCK Rules** (Red Light 🔴)
- Stop suspicious connection attempts
- Block access to gaming sites during work hours
- Prevent unauthorised remote access

**Example Rules in Plain English:**
```
Rule 1: ALLOW web browsing from any computer to the internet
Rule 2: BLOCK all connections to social media from 9am-5pm
Rule 3: ALLOW email servers to communicate
Rule 4: BLOCK all other incoming connections
```

---

## Intrusion Detection: The Security Camera System

### What is Intrusion Detection?

An **Intrusion Detection System (IDS)** is like a security camera system that watches for suspicious activity. It doesn't stop intruders directly, but it **alerts security** when something looks wrong.

#### What IDSs Look For:
- **Unusual login attempts** (someone trying 100 different passwords)
- **Strange network patterns** (massive data downloads at 3 AM)
- **Known attack signatures** (recognising common hacking techniques)
- **Abnormal behaviour** (a computer suddenly sending thousands of emails)

### Real Example: School Network
Your school's IDS might notice:
- A student's laptop suddenly trying to access the server room network
- Hundreds of failed password attempts on the student portal
- Large file downloads during exam time (possible cheating?)

---

## Network Monitoring: Keeping Watch

Network monitoring is like having a security team that constantly watches CCTV footage. They look for:

### Normal Network Activity
- Students browsing educational websites
- Teachers accessing the school database
- Email being sent and received
- Printers receiving documents

### Suspicious Network Activity
- Computers trying to connect to unknown external servers
- Unusual amounts of data being transferred
- Network connections at strange times
- Multiple failed login attempts

---

## Common Network Security Threats

### 1. Unauthorised Access
**What it is:** Someone gaining access to a network they shouldn't be on
**Example:** A person connecting to your home Wi-Fi and accessing your files
**Protection:** Strong passwords, encryption, firewalls

### 2. Malware
**What it is:** Malicious software that damages or steals information
**Example:** A virus that copies all your photos and sends them to criminals
**Protection:** Antivirus software, firewalls, careful downloading

### 3. Data Interception
**What it is:** Someone "listening in" on your network communications
**Example:** Hackers at a café intercepting your online banking details
**Protection:** HTTPS websites, VPNs, encrypted connections

### 4. Denial of Service (DoS)
**What it is:** Overwhelming a network so legitimate users can't access it
**Example:** Flooding a school's website with fake requests so students can't log in
**Protection:** Traffic filtering, load balancing

---

## Australian Examples

### Telstra's Network Security
Telstra protects their mobile network using:
- Firewalls to block malicious traffic
- Intrusion detection to spot unusual patterns
- Monitoring systems watching millions of connections

### University Networks
Australian universities like Melbourne Uni use:
- Campus-wide firewalls protecting student data
- Wi-Fi networks with multiple security layers
- Monitoring systems that detect if someone's computer gets infected

---

## Quick Check: Understanding Firewalls

**Scenario:** Your home has Wi-Fi that your family uses for streaming Netflix, video calls, and schoolwork.

1. **What would a firewall ALLOW?**
2. **What should a firewall BLOCK?**
3. **What might trigger an intrusion detection alert?**

<details>
<summary>Click for answers</summary>

**ALLOW:**
- Netflix streaming (legitimate entertainment)
- Video calls for school/work
- Web browsing for homework
- Online gaming during free time

**BLOCK:**
- Unknown devices trying to connect
- Attempts to access your computer files from the internet
- Suspicious downloads or uploads
- Known malicious websites

**IDS ALERTS:**
- Someone trying to guess your Wi-Fi password
- A device suddenly uploading gigabytes of data
- Multiple connection attempts from the same unknown source
- Unusual network activity at 3 AM when everyone's asleep

</details>

---

## Coming Up Next

In our **Lab session**, we'll explore what network security looks like in practice using command-line tools to examine network connections and understand what's happening on our networks.

In **Code Practice**, we'll build a simple Python tool to check what services are running on our computer - like being our own security guard!

---

## Key Terms to Remember

- **Firewall:** Security system that controls network traffic based on rules
- **IDS:** Intrusion Detection System - monitors for suspicious activity  
- **Network Monitoring:** Continuously watching network activity for problems
- **Unauthorised Access:** Someone connecting to a network without permission
- **Malware:** Malicious software designed to damage or steal information