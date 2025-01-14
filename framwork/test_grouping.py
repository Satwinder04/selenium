import pytest
import conftest


class TestCase:
    @pytest.mark.regression
    def testlogin(self, setup):
        print("this is login method reg")
        assert True

    @pytest.mark.positive
    def testSearch(self, setup):
        print("this is search method pos")
        assert True

    @pytest.mark.negative
    def testAdvance(self, setup):
        print("this is admvance method neg")
        assert True

    @pytest.mark.sanity
    @pytest.mark.regression
    def testlogout(self, setup):
        print("this is logout method reg and sanity")
        assert True
    @pytest.mark.sanity
    def testlogout(self, setup):
        print("this is logout method reg and sanity")
        assert True

