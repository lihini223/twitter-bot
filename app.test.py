from app import TwitterBot
import pytest

class Test_Twitterbot_Login:
    
    @pytest.fixture()
    def twitterbot(self):
    	return TwitterBot()
    
    def test_login_1(self, twitterbot):
        twitterbot.login()

