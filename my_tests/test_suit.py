import pytest

@pytest.mark.smoke
def test_login_pagevalid_use():
    print('Login with valid user')

pytest.mark.regression 
@pytest.mark.smoke
def test_login_wrong_password():
    print('Login with valid password')
    
    
    # print test logs
    # pytest
    
    # created a html report
    # python -m pytest --html=my_report.html