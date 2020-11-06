import pytest
from Form import Form
user = Form(login= "root", password= "root")
def test_two_element():
    assert user.user_name == 'root'
    assert user.user_password == 'root'
def test_four_element():
    user = Form(login= "Alex", password="some_pass",age = 25, url = 'https://itproger.com')
    assert user.user_name == 'Alex'
    assert user.user_password == 'some_pass'
    assert user.user_age == 25
    assert user.url == 'https://itproger.com'
def test_url():
    code = user.s_code(url = 'https://pypi.org')
    assert code == 200