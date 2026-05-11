import requests

def test_homepage():
    r = requests.get("http://localhost:5000")
    assert r.status_code == 200

def test_submit_page():
    r = requests.get("http://localhost:5000/submit")
    assert r.status_code == 200
