import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone

URL = "https://b12.io/apply/submission"
SECRET = b"hello-there-from-b12"

payload = {
    "action_run_link": "REPLACE_ME",
    "email": "hrengifo318@gmail.com",
    "name": "Hector Rengifo",
    "repository_link": "https://github.com/swmd/b12-application",
    "resume_link": "https://drive.google.com/file/d/1OK63o_v5DzKi63sI5fm1xGDPY0v9aqRT/view?usp=sharing",
    "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
}

# Canonical JSON: sorted keys, no extra whitespace
body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

signature = hmac.new(SECRET, body, hashlib.sha256).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}",
}

response = requests.post(URL, data=body, headers=headers)
response.raise_for_status()

print(response.text)
