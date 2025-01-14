import pytest
import conftest


class TestCase:
    @pytest.mark.run(order=1)
    def testlogin(self, setup):
        print("this is login method")
        assert True

    @pytest.mark.run(order=2)
    def testSearch(self, setup):
        print("this is search method")
        assert True

    @pytest.mark.run(order=3)
    def testAdvance(self, setup):
        print("this is admvance method")
        assert True

    @pytest.mark.run(order=4)
    def testlogout(self, setup):
        print("this is logout method")
        assert True

