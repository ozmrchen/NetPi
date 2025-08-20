# test_dns_lookup_simple.py
# Pytest tests for dns_lookup.resolve()
# Run: pytest -q

import pytest
import dns_lookup  # your dns_lookup.py

# Simple valid test case for quick check.
# Input data: "www.abc.net.au"
# Expected output: a non-empty string (IP address, e.g., "203.x.x.x")
def test_valid():
    ip = dns_lookup.resolve("www.abc.net.au")
    assert isinstance(ip, str) and len(ip) > 0

# Valid websites should return a non-empty string (an IP).
# Input data: ["www.abc.net.au", "www.google.com"]
# Expected output: each resolves to a non-empty string (IP address)
@pytest.mark.parametrize("website", ["www.abc.net.au", "www.google.com"])
def test_valid_returns_ip(website):
    ip = dns_lookup.resolve(website)
    assert isinstance(ip, str) and len(ip) > 0

# Blank inputs should raise ValueError.
# Input data: ["", "   ", "\n", "\t"]
# Expected output: ValueError is raised
@pytest.mark.parametrize("value", ["", "   ", "\n", "\t"])
def test_blank_raises(value):
    with pytest.raises(ValueError):
        dns_lookup.resolve(value)