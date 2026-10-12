#!/usr/bin/env python3
"""Local preview that rebuilds static output when public or components change."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from build import ROOT, SOURCE, COMPONENTS, OUTPUT, main as build

lock = Lock()
snapshot = None


def changes():
    return tuple((str(p), p.stat().st_mtime_ns, p.stat().st_size)
                 for directory in (SOURCE, COMPONENTS)
                 for p in sorted(directory.rglob("*")) if p.is_file())


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(OUTPUT), **kwargs)

    def do_GET(self):
        global snapshot
        if self.path == "/__twp_preview":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"twp-preview-v1\n")
            return
        with lock:
            current = changes()
            if current != snapshot:
                build()
                snapshot = current
        super().do_GET()


if __name__ == "__main__":
    build()
    snapshot = changes()
    print("Preview at http://127.0.0.1:4174/", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 4174), Handler).serve_forever()
