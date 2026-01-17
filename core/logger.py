import json
from datetime import datetime

LOG_FILE = "xss_hits.json"

def log_hit(context):
    context["timestamp"] = datetime.utcnow().isoformat()

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(context, indent=2) + "\n")

    print("\n🔥 XSS EXECUTION CONFIRMED")
    print(f"Final URL : {context['final_url']}")
    print(f"Parameter : {context['parameter']}")
    print(f"Payload   : {context['payload']}")
    print(f"Status    : {context['status']}")
    print(f"Proof     : {', '.join(context['proof'])}")
    print("-" * 60)
