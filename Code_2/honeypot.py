import http.server, socketserver

print("🍯 Starting honeypot on http://localhost:9999")
print("🍯 Open browser to localhost:9999 then watch the logs!")
with socketserver.TCPServer(("", 9999), http.server.SimpleHTTPRequestHandler) as server:
    server.serve_forever()
