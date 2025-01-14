import pytest
import conftest
# import dependancy
class TestCase:

    def testlogin(self,setup):
        print("this is login method")
    @pytest.mark.skip
    def testlogout(self,setup):
        print("this is logout method")