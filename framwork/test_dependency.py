import pytest
from pytest_dependency import depends

import conftest
import dependency

class TestCase:
    @pytest.mark.dependency
    def testlogin(self, setup):
        print("this is login method")
        assert False
    @pytest.mark.dependency(depends('TestCase::testSearch','TestCase::testlogin'))
    def testSearch(self, setup):
        print("this is search method")
        assert False

    @pytest.mark.dependency(depends('TestCase::testAdvance','TestCase::testlogin'))
    def testAdvance(self, setup):
        print("this is admvance method")
        assert False

    @pytest.mark.dependency(depends('TestCase::testlogout', 'TestCase::testAdvance'))
    def testlogout(self, setup):
        print("this is logout method")
        assert True

