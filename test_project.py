from project import get_accepted_currencies, simplify, verify_input, get_code, convert_to_euros
import pytest

def test_get_accepted_currencies():
    ...

def test_simplify():
    assert simplify("12.34 USD") == "12.34USD"
    assert simplify("50,000CAN") == "50000CAN"
    assert simplify("yen 0.21 ") == "YEN0.21"
    assert simplify("250, 000.67") == "250000.67"
    assert simplify("   ₣123   ") == "₣123"

def test_verify_input():
    assert verify_input("12USD") == (12, "USD")
    assert verify_input("£0.25") == (0.25, "GBP")
    
    with pytest.raises(SystemExit):
        verify_input("250000.67")

    with pytest.raises(SystemExit):
        verify_input("CAN124")
    

def test_get_code():
    assert get_code("$") == "USD"
    assert get_code("₣") == "INR"
    assert get_code("₴") == "UAH"

    with pytest.raises(SystemExit):
        get_code("₩")

    with pytest.raises(SystemExit):
        get_code("*")

def test_convert_to_euros():
    ...