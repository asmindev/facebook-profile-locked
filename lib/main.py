from .parser_html import Parsing
import requests
import re


class Main:
    def __init__(self):
        self.__cookies = {"cookie": None}
        self.__url = 'https://mbasic.facebook.com'

    # Validated cookie and get facebook account ID
    @property
    def validate_cookie(self):
        home = Parsing(requests.get(self.__url + '/me',
                                    cookies=self.__cookies).text)
        link = home.find_url('?returnuri')
        if link:
            return re.findall(r"id=(\d*)&", link)[0]
        return False

    # Change language
    def change_lang(self, code: str):
        data = Parsing(requests.get(self.__url + '/language.php',
                                    cookies=self.__cookies).text)
        return requests.get(self.__url + data.find_url(code)[0], cookies=self.__cookies)

    # Lock profile
    def lock_profile(self, id):
        params = {"entry_point": "profile_section",
                  "profile_id": id, "refid": "17"}
        url = "/private_sharing/home_view/"
        to_lock = Parsing(requests.get(self.__url + url,
                                       params=params, cookies=self.__cookies).text)
        form = to_lock.parsing_form('private_sharing')
        action = form.get('action')
        form.pop('action')
        requests.post(self.__url + action, data=form, cookies=self.__cookies)

    @property
    def cookies(self):
        return self.__cookies

    @cookies.setter
    def set_cookie(self, cookie: str):
        self.__cookies = {"cookie": cookie}
