# dns_lookup.py
import socket

website = input("Enter a website (e.g., www.google.com): ")
ip_address = socket.gethostbyname(website)
print(f"The IP address of {website} is {ip_address}")
