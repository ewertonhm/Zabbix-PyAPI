from itertools import count
from requests import post
import logging


class Zabbix_PyAPI:
    def __init__(self, url, user, psw):
        self.url = url
        self.user = user
        self.psw = psw
        self.token = self.login()

    def zabbix_request(self, data):
        try:
            return post(self.url, json=data)
        except Exception as e:
            logging.error(e)
            return False

    def login(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.psw
            },
            "id": 1,
            "auth": None
        }
        response = self.zabbix_request(data)
        try:
            if count(response.json()['result'] > 0):
                return response.json()['result']
            else:
                return response.json()

        except Exception as e:
            logging.error(e)
            return response

    def request(self, method, params):
        data = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "auth": self.token,
            "id": 2
        }

        response = self.zabbix_request(data)
        return response.json()['result'][0]['groupid']
