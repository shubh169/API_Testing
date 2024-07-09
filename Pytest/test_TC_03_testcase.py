import pytest

@pytest.fixture(scope='module')
def my_fixture():
    print("\nThis is our fixture.Run before the testcase.")
    print("_________________________________")
    yield
    print("\n_________________________________")
    print("Close the DB.")

@pytest.mark.sanity
def test_tc_01_login_logout(my_fixture):
    print("sanity testcase start")
    print("testcase complete.")

@pytest.mark.smoke
def test_tc_03_invalid_credentials(my_fixture):
    print("smoke testcase start")
    print("testcase complete.")
