import pytest

actual_result="Testing"
# Decorator ((using to skip a specific testcase.)
# @pytest.mark.skipif(a>100,reason="functionality is not working, developrs will be fix in next build.")

# Custom marker
@pytest.mark.TopPriority
@pytest.mark.regression
def test_tc_01_login_logout():
    print("sanity testcase start")
    print("testcase complete.")
    # assert actual_result=="Testing"
    assert actual_result != "Testing" ,"these two valuse must not be same"

@pytest.mark.TopPriority
@pytest.mark.regression
def test_tc_03_invalid_credentials():
    print("smoke testcase start")
    print("testcase complete.")
