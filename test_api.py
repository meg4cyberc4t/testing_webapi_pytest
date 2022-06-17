import pytest
from api import BulgakovApi

api_key = None


def test_sign_in():
    login = "MolchanovIA20@st.ithub.ru"
    password = "ЗачемВамМойПароль?) :D"
    code, user = BulgakovApi().sign_in(login, password)
    assert code == 200
    assert 'token' in user
    global api_key
    api_key = user['token']


def test_sign_out():
    code, _ = BulgakovApi().sign_out(api_key)
    assert code == 200
