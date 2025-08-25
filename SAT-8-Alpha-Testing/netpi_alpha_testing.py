#!/usr/bin/env python3
"""
NetPi Network Scanner Tool - 25 Minute Implementation
Scans network targets and classifies hardware/network types
Based on VCE Applied Computing Week 1.1-1.3 concepts
"""
import socket
import subprocess
import sys
import time

# Constants
AUSTRALIAN_DOMAINS = ['.com.au', '.net.au', '.gov.au', '.edu.au']
COMMON_ROUTER_IPS = ['192.168.1.1', '192.168.0.1', '10.0.0.1']


def validate_target(target: str) -> str:
    """
    Validate and clean target input
    Returns: cleaned target string
    Raises: ValueError for invalid input
    """
    # TODO: Implement validation logic
    # - Strip whitespace from target
    # - Check target is not empty
    # - Return cleaned target
    # Example: return target.strip() if target.strip() else raise ValueError()
    pass


def resolve_hostname(target: str) -> str:
    """
    Resolve hostname to IP address
    Returns: IP address string or None if failed
    """
    # TODO: Implement DNS resolution
    # - Use socket.gethostbyname(target)
    # - Catch socket.gaierror exception
    # - Return IP string or None
    pass


def classify_network_type(ip_address: str) -> str:
    """
    Classify IP address as WPAN, LAN, or WAN
    Returns: "WPAN", "LAN", "WAN", or "ERROR"
    """
    # TODO: Implement network classification
    # - Check for 127.x.x.x (return "WPAN")
    # - Check for 192.168.x.x or 10.x.x.x (return "LAN")
    # - Everything else return "WAN"
    # - Handle errors return "ERROR"
    pass


def test_connectivity(target: str) -> dict:
    """
    Test connectivity using ping command
    Returns: dict with status and response_time
    """
    # TODO: Implement ping testing
    # - Use subprocess.run() to execute ping command
    # - Windows: ['ping', '-n', '1', target]
    # - Linux/Mac: ['ping', '-c', '1', target]
    # - Return {"status": "SUCCESS/FAILED", "response_time": ms}
    pass


def classify_hardware(ip_address: str) -> str:
    """
    Classify likely hardware type based on IP
    Returns: "ROUTER", "UNKNOWN"
    """
    # TODO: Implement hardware classification
    # - Check if ip_address is in COMMON_ROUTER_IPS list
    # - Return "ROUTER" if found
    # - Return "UNKNOWN" otherwise
    pass


def scan_target(target: str) -> dict:
    """
    Complete scan of single target
    Returns: dict with all scan results
    """
    # TODO: Implement complete scanning workflow
    # 1. Call validate_target(target)
    # 2. Call resolve_hostname() to get IP
    # 3. Call classify_network_type()
    # 4. Call test_connectivity()
    # 5. Call classify_hardware()
    # 6. Return dictionary with all results
    pass


def main():
    """
    Main program function - Test your implementation
    """
    print("NetPi Network Scanner v1.0")
    print("=" * 30)

    # Test targets for demonstration
    test_targets = [
        "www.abc.net.au",  # Australian website
        "127.0.0.1",  # Localhost
        "192.168.1.1"  # Common router IP
    ]

    print("\nScanning test targets...")
    for target in test_targets:
        print(f"\nScanning {target}...")
        try:
            result = scan_target(target)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
