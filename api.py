import requests


class BulgakovApi:
    BASEURL = "https://ithub.bulgakov.app/api/"

    # signIn
    def sign_in(self, login, password):
        res = requests.post(self.BASEURL + 'auth/signIn', json={"email": login, "password": password})
        return res.status_code, res.json()

    def sign_out(self, token):
        res = requests.get(self.BASEURL + "auth/signOut", headers={"Authorization": f"Bearer {token}"})
        return res.status_code, None
