"""
Simple HTTP server for frontend development.
Automatically finds an available port.
"""

import http.server
import socketserver
import socket
import webbrowser
from pathlib import Path

def find_free_port(start_port=8001, max_port=8100):
    """Find an available port."""
    for port in range(start_port, max_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    raise RuntimeError("No available port found")

def start_server(port=None):
    """Start HTTP server on available port."""
    if port is None:
        port = find_free_port()
    
    # Change to frontend directory
    frontend_dir = Path(__file__).parent
    os.chdir(frontend_dir)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            url = f"http://localhost:{port}"
            print(f"\n{'='*60}")
            print(f"Frontend server started!")
            print(f"URL: {url}")
            print(f"Press CTRL+C to stop")
            print(f"{'='*60}\n")
            
            # Try to open browser automatically
            try:
                webbrowser.open(url)
            except:
                pass
            
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 10013:  # Permission denied
            print(f"\nError: Port {port} is blocked or in use.")
            print(f"Trying alternative port...")
            start_server(port=None)
        else:
            raise

if __name__ == "__main__":
    import os
    start_server()
