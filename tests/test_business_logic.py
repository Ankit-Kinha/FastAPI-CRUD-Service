from app.utils import normalize_title

def test_normalize_title():
    assert normalize_title(" Hello World ") == "hello-world"
    assert normalize_title("MULTI   SPACE Test") == "multi-space-test"
