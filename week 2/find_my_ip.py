import socket

def get_local_ip():
    """Get the local IP address by connecting to a public DNS server."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except socket.error as e:
        return f"Error: {e}"
    

if __name__ == "__main__":
    print(f"My IP Address: {get_local_ip()}")