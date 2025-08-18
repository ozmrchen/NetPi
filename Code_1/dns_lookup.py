"""
Ask for a website and print its IPv4 address.
"""
import socket

def resolve(website: str) -> str:
    website = (website or "").strip()
    if not website:
        raise ValueError("Website cannot be blank.")
    return socket.gethostbyname(website)

if __name__ == "__main__":
    website = input("Enter a website (e.g., www.abc.net.au): ")
    ip = resolve(website)
    print(f"{website} resolves to {ip}")
