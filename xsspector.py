#!/usr/bin/env python3

import argparse
import sys
from urllib.parse import urlparse, parse_qs

from core.executor import fire
from core.verifier import verify_execution
from core.logger import log_hit
from core.payloads import generate_payload

BANNER = """
██╗  ██╗███████╗███████╗██████╗ ███████╗ ██████╗████████╗ ██████╗ ██████╗ 
╚██╗██╔╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
 ╚███╔╝ ███████╗███████╗██████╔╝█████╗  ██║        ██║   ██║   ██║██████╔╝
 ██╔██╗ ╚════██║╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
██╔╝ ██╗███████║███████║██║     ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

Proof-Based XSS Intelligence Engine
"""

def extract_params(url):
    parsed = urlparse(url)
    return parse_qs(parsed.query)

def main():
    print(BANNER)

    parser = argparse.ArgumentParser(description="XSSPECTOR - Advanced XSS Parameter Hunter")
    parser.add_argument("--deep", action="store_true", help="Enable deep scanning mode")
    parser.add_argument("--json", action="store_true", help="Enable JSON logging")

    args = parser.parse_args()

    print("📥 Waiting for URLs from stdin...\n")

    for line in sys.stdin:
        url = line.strip()
        if not url:
            continue

        params = extract_params(url)
        if not params:
            continue

        print(f"🔎 Scanning: {url}")

        for param in params:
            payload, marker = generate_payload()

            attack_params = params.copy()
            attack_params[param] = payload

            result = fire(url, attack_params)

            if not result:
                continue

            proof = verify_execution(result["text"], marker)

            if proof:
                log_hit({
                    "url": url,
                    "final_url": result["final_url"],
                    "parameter": param,
                    "payload": payload,
                    "status": result["status"],
                    "proof": proof
                })

if __name__ == "__main__":
    main()
