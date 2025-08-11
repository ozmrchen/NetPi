"""
dns_lookup.py
Ask for a website and print its IPv4 address.
"""
import socket

def main():
    website = input("Enter a website (e.g., www.abc.net.au): ").strip()
    try:
        ip = socket.gethostbyname(website)
        print(f"{website} resolves to {ip}")
    except socket.gaierror as e:
        print(f"DNS lookup failed for '{website}': {e}")

if __name__ == "__main__":
    main()
