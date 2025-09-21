from http.server import SimpleHTTPRequestHandler, HTTPServer
import json, os

PORT = 4000

materials = [
    {"id": 1, "name": "Steel Scaffolding", "price_per_day": 50, "stock": 20},
    {"id": 2, "name": "Wooden Planks", "price_per_day": 10, "stock": 100},
    {"id": 3, "name": "Shuttering Plates", "price_per_day": 25, "stock": 50}
]
orders = []

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/materials":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(materials).encode())
        elif self.path == "/api/orders":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(orders).encode())
        else:
            if self.path == "/" or self.path.startswith("/frontend"):
                if self.path == "/":
                    path = "frontend/index.html"
                else:
                    path = self.path.lstrip("/")
                try:
                    with open(path, "rb") as f:
                        content = f.read()
                    self.send_response(200)
                    if path.endswith(".html"):
                        self.send_header("Content-Type", "text/html")
                    elif path.endswith(".css"):
                        self.send_header("Content-Type", "text/css")
                    elif path.endswith(".js"):
                        self.send_header("Content-Type", "application/javascript")
                    self.end_headers()
                    self.wfile.write(content)
                except FileNotFoundError:
                    self.send_error(404, "File not found")
            else:
                super().do_GET()

    def do_POST(self):
        if self.path == "/api/orders":
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                order = json.loads(body)
                orders.append(order)
                self.send_response(201)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Order placed"}).encode())
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    httpd = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Serving on http://0.0.0.0:{PORT}")
    httpd.serve_forever()
