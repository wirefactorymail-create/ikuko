#!/usr/bin/env python3
"""No-cache HTTP server for local development."""
import http.server

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # suppress access logs

if __name__ == '__main__':
    http.server.test(HandlerClass=NoCacheHandler, port=3000, bind='')
