import pytest

@pytest.mark.sanity
def test_tc_01_login_logout():
    print("sanity testcase start")
    print("testcase complete.")

@pytest.mark.smoke
def test_tc_03_invalid_credentials():
    print("smoke testcase start")
    print("testcase complete.")
