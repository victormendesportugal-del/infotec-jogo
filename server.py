import http.server, socketserver, socket, os
PORT=8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def lan_ip():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8",80)); ip=s.getsockname()[0]
    except OSError: ip="IP não detetado"
    finally: s.close()
    return ip
class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control","no-cache")
        super().end_headers()
with socketserver.TCPServer(("0.0.0.0",PORT),Handler) as httpd:
    print("\\n INFOTEC - servidor iniciado!")
    print(f" Neste PC: http://localhost:{PORT}")
    print(f" No telemóvel (mesma rede Wi-Fi/hotspot): http://{lan_ip()}:{PORT}")
    print(" Mantém esta janela aberta. CTRL+C para parar.\\n")
    httpd.serve_forever()
