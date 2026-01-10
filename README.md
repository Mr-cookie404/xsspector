🛠 Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/xsspector.git
cd xsspector

2️⃣ Install Requirements
pip3 install -r requirements.txt


Python Version:
✅ Python 3.8 or higher recommended


🔹 Basic Usage (stdin)
gau example.com | python3 xsspector.py

🔹 Deep Scan + JSON Output
gau example.com | python3 xsspector.py --deep --json

🔹 Using Wayback URLs
waybackurls example.com | python3 xsspector.py --deep

🔹 Scan from File
python3 xsspector.py -i urls.txt --deep --json

🔹 Custom Output Name
python3 xsspector.py -i urls.txt --deep -o my_xss_results


This will generate:

my_xss_results.txt
my_xss_results.json

🧠 CLI Options
Option	Description
-i, --input 	Input file containing URLs
-d, --domain   	Target domain (optional)
--deep	        Enable advanced analysis (JS, DOM, mutations)
--json	        Save results in JSON format
-o, --output	Output file name (default: output/results)

TXT Output
https://target.com/search?q=test | Risk: HIGH

JSON Output
{
  "url": "https://target.com/search",
  "parameter": "q",
  "type": "DOM-XSS",
  "context": "innerHTML",
  "mutation": "q[]=<svg/onload=alert(1)>",
  "reflection": true,
  "risk": "HIGH",
  "confidence": 0.92
}
