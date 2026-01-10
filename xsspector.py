import argparse
import sys
import json

from core.url_parser import normalize_url
from core.param_discovery import extract_parameters
from core.path_analyzer import extract_path_params
from core.fragment_analyzer import extract_fragment_params
from core.scorer import calculate_score

def banner():
    print(r"""
Y8b Y8P  dP"8  dP"8 888 88e  888'Y88   e88'Y88 88P'888'Y88   e88 88e   888 88e  
 Y8b Y  C8b Y C8b Y 888 888D 888 ,'Y  d888  'Y P'  888  'Y  d888 888b  888 888D 
  Y8b    Y8b   Y8b  888 88"  888C8   C8888         888     C8888 8888D 888 88"  
 e Y8b  b Y8D b Y8D 888      888 ",d  Y888  ,d     888      Y888 888P  888 b,   
d8b Y8b 8edP  8edP  888      888,d88   "88,d88     888       "88 88"   888 88b, 

          XSSPECTOR – Advanced XSS Hunter
    """)

def parse_args():
    parser = argparse.ArgumentParser(
        description="XSSPECTOR – Advanced XSS Parameter Discovery Tool"
    )
    parser.add_argument("-d", "--domain", help="Target domain")
    parser.add_argument("-i", "--input", help="Input file (GAU / Wayback URLs)")
    parser.add_argument("--deep", action="store_true", help="Enable deep analysis")
    parser.add_argument("--json", action="store_true", help="Save JSON output")
    parser.add_argument("--output", default="output/results", help="Output file base")
    return parser.parse_args()

def load_urls(args):
    urls = []

    if args.input:
        with open(args.input) as f:
            urls = f.readlines()
    else:
        urls = sys.stdin.readlines()

    return urls

def main():
    banner()
    args = parse_args()
    urls = load_urls(args)

    results = []

    for url in urls:
        parsed = normalize_url(url)
        if not parsed:
            continue

        params = []
        params.extend(extract_parameters(parsed))
        params.extend(extract_path_params(parsed))
        params.extend(extract_fragment_params(parsed))

        if not params:
            continue

        risk = calculate_score([len(params)])

        results.append({
            "url": parsed.geturl(),
            "parameters": params,
            "risk": risk
        })

    # TXT output
    with open(args.output + ".txt", "w") as f:
        for r in results:
            f.write(f"{r['url']} | Risk: {r['risk']}\n")

    # JSON output
    if args.json:
        with open(args.output + ".json", "w") as jf:
            json.dump(results, jf, indent=4)

    print(f"[+] Scan complete. Results saved to {args.output}.*")

if __name__ == "__main__":
    main()
