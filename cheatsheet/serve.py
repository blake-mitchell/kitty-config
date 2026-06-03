#!/usr/bin/env python3
"""Serve the kitty cheat sheet with live reload.

Serves the generated out/ tree over HTTP on 127.0.0.1:7045 and exposes /live,
an SSE endpoint that fires whenever any .html file under it changes. Pages
include a snippet that listens to /live and reloads themselves.
"""
import http.server
import pathlib
import time

ROOT = pathlib.Path(__file__).resolve().parent / "out"  # generated artifacts
PORT = 7045


def html_mtimes():
    return {p: p.stat().st_mtime for p in ROOT.rglob("*.html")}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path != "/live":
            return super().do_GET()
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        seen = html_mtimes()
        try:
            while True:
                time.sleep(0.5)
                now = html_mtimes()
                if now != seen:
                    seen = now
                    self.wfile.write(b"data: reload\n\n")
                    self.wfile.flush()
                else:  # keep-alive comment so dead connections surface
                    self.wfile.write(b": ping\n\n")
                    self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"serving {ROOT} on http://127.0.0.1:{PORT}")
    server.serve_forever()
