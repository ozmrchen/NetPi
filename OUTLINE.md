# VCE Applied Computing - Weeks 1-4 (Complete Outline)

## Week 1: Network Hardware & Commands (Based on Existing Files)

### Lesson 1.1: Network Hardware Components
- **Switches vs Routers**: Local device connection vs network interconnection
- **Data flow**: Following packets through network infrastructure
- **Real-world identification**: Spotting network hardware in school/home
- **Australian context**: NBN infrastructure, internet exchanges

### Lab 1.1: Discovering Network Hardware
- Use `ip` and `ifconfig` to examine network connections
- Identify default gateway (router) using `ip route`
- Trace data paths with `traceroute`
- Map physical and logical network topology

### Code Practice 1.1: Find Your Hardware
- **Python + Scapy**: Automated network discovery
- Socket programming for IP detection
- Router identification via routing tables
- 5-line script challenges for quick wins

### Lesson 1.2: Network Types in Practice  
- **WPAN, LAN, WAN**: Size, scope, and practical examples
- **How networks connect**: Personal → Local → Wide area
- **Australian examples**: Home Wi-Fi → School network → NBN → Internet
- **Security implications**: Different risks at different network levels

### Lab 1.2: Spotting Network Types
- Identify LAN vs WAN using IP addresses
- Test connection speeds (local vs internet)
- Find WPAN devices (Bluetooth, NFC)
- Network type classification exercises

### Code Practice 1.2: Network Type Detector
- **Automated classification**: LAN vs WAN identification
- Speed testing and comparison
- Network hop counting
- Simple network summarisation

### Lesson 1.3: Essential Linux Networking Commands
- **The Essential Four**: `ping`, `ss`, `ip`, `traceroute`
- **Systematic diagnosis**: Step-by-step network troubleshooting
- **Security applications**: Using commands for vulnerability assessment
- **Automation potential**: Commands that Python can enhance

### Lab 1.3: Essential Network Commands Practice
- Master `ping` for connectivity testing
- Use `ss` to check open ports and connections  
- Extract network info with `ip` commands
- Practice `traceroute` for path analysis

### Code Practice 1.3: Automate Network Commands
- **Python subprocess**: Running commands programmatically
- **Scapy integration**: Advanced packet manipulation
- Combined network health checks
- Port scanning automation

---

## Week 2: Vulnerability Scanning & Threat Detection

### Lesson 2.1: Cyber Security Threats & Vulnerability Types
- **Common attack vectors**: Malware, unauthorised access, data breaches
- **Vulnerability categories**: Network, system, application weaknesses
- **Detection methods**: Automated scanning vs manual assessment
- **Risk prioritisation**: Understanding CVSS scores and impact

### Lab 2.1: Network Vulnerability Assessment
- `nmap` port scanning fundamentals
- Service enumeration and banner grabbing
- Identifying misconfigurations and unnecessary services
- Documentation and reporting findings

### Code Practice 2.1: **Smart Vulnerability Analyzer** ⭐
- **Wow factor**: Converts raw nmap output into risk-scored reports
- Python modules: `subprocess`, `json`, `re`
- Automated vulnerability classification
- Plain-English threat explanations

---

## Week 3: Incident Response & Security Operations

### Lesson 3.1: Incident Response & Security Monitoring
- **Incident lifecycle**: Detection, analysis, containment, recovery
- **Monitoring strategies**: Proactive vs reactive security
- **Penetration testing ethics**: Legal boundaries and responsible disclosure
- **Security operations**: Building sustainable security practices

### Lab 3.1: Security Monitoring & Response Simulation
- Combine Week 1-2 tools for comprehensive assessment
- Practice incident response scenarios
- Create security monitoring workflows
- Develop standard operating procedures

### Code Practice 3.1: **Security Command Center** ⭐
- **Wow factor**: Interactive incident response guide with automation
- Integrate previous weeks' Python tools
- Timeline creation and incident tracking
- Automated response recommendations

---

## Week 4: Assessment & Portfolio

### Practical Assessment: Comprehensive Security Audit
- **Scenario-based assessment**: Real-world network security challenge
- **Tool integration**: Demonstrate mastery of CLI and Python tools
- **Professional reporting**: Document findings and recommendations
- **Ethical considerations**: Show understanding of legal/ethical boundaries

### Portfolio Components:
- Network discovery and mapping
- Vulnerability assessment report
- Custom Python security tools
- Incident response documentation

---

## Tool Summary
### CLI Tools
- **Week 1**: `ping`, `ss`, `ip`, `traceroute`
- **Week 2**: `nmap` (basic port scanning)

### Python Enhancement
- **Built-in modules**: `socket`, `subprocess`, `time`, `datetime`, `json`, `re`
- **One external package**: `rich` (terminal colours) + `scapy` (advanced networking)

## Learning Outcomes
✅ **Network security fundamentals** - Hardware understanding + practical skills  
✅ **Vulnerability scanning techniques** - CLI mastery + intelligent Python analysis  
✅ **Penetration testing methodologies** - Ethical framework + basic techniques  
✅ **Log analysis and incident response** - Automated analysis + guided procedures  
✅ **Technical threat detection methods** - Pattern recognition + risk assessment