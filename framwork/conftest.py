import pytest
@pytest.fixture()
def setup():
    print("launcting browser...")
    yield
    print("closing the browser")
