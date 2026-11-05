"""Tiny demo service for Shipyard."""
from http.server import BaseHTTPRequestHandler, HTTPServer

GREETING = "Hello from Shipyard demo"
FOOTER = "v11"


def render() -> str:
    return f"{GREETING} ({FOOTER})\n"


def health() -> str:
    return "ok\n"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (health() if self.path == "/health" else render()).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
