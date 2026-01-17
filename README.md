# XSSPECTOR 😈
**Proof-Based XSS Intelligence Engine**

XSSPECTOR is an advanced XSS parameter discovery and exploitation verification tool that:
- Extracts parameters from WaybackURLs / GAU
- Injects unique execution markers
- Detects proof-based JavaScript execution
- Logs confirmed vulnerable endpoints

---

## ⚡ Features
- Unique Payload Markers
- Execution Proof System
- Endpoint Logging
- JSON Evidence Reports
- Kali + Windows Support
- Bug Bounty Ready

---

## 🛠 Installation

### Kali Linux / Linux
```bash
sudo apt install python3-venv -y
git clone https://github.com/Mr-cookie404/xsspector.git
cd xsspector

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt



###Usage
gau target.com | python xsspector.py --deep --json

waybackurls target.com | python xsspector.py --deep --json

