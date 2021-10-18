from requests import post
from pprint import pprint
from json import load

def zabbix_request(data):
    zabbix = 'http://zabbix.monitor.redeunifique.com.br/api_jsonrpc.php'
    return post(zabbix,json=data)

def login():
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "",
            "password": ""
        },
        "id": 1,
        "auth": None
    }
    response = zabbix_request(data)
    return response.json()['result']

def get_hostgroup(auth, groupname):
    data = {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {
            "output": "extend",
            "filter": {
                "name": [
                    groupname
                ]
            }
        },
        "auth": auth,
        "id": 2
    }

    response = zabbix_request(data)
    return response.json()['result'][0]['groupid']

def get_hosts_by_groupid(auth, groupid):
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "groupids": groupid,
            "output": [
                "hostid",
                "host",
            ],
            "selectInventory": ["name"]
        },
        "id": 2,
        "auth": auth
    }

    response = zabbix_request(data)
    return response.json()['result']

def get_proxys(auth):
    data = {
        "jsonrpc": "2.0",
        "method": "proxy.get",
        "params": {
            "output": "extend"
        },
        "id": 2,
        "auth": auth
    }

    response = zabbix_request(data)
    proxys = []
    for r in response.json()['result']:
        data = {'host':r['host'],'id':r['proxyid']}
        proxys.append(data)
    return proxys

def get_host_by_hostid(auth,hostid):
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "filter": {
                "hostid": hostid
            },
            "output": [
                "hostid",
                "host",
                "description",
                "name",
                "proxy_hostid",
            ]
        },
        "id": 2,
        "auth": auth
    }

    response = zabbix_request(data)
    return response.json()['result']

def get_hosts_by_proxy(auth, proxyid):
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "proxyids": proxyid,
            "monitored_hosts":'0',
            "output": [
                "hostid",
                "host",
            ]
        },
        "id": 2,
        "auth": auth
    }

    response = zabbix_request(data)
    return response.json()['result']

def update_name(auth, hostid, name):
    data = {
        "jsonrpc": "2.0",
        "method": "host.update",
        "params": {
            "hostid": hostid,
            "inventory": {
                "name": name
            }
        },
        "auth": auth,
        "id": 3
    }
    response = zabbix_request(data)
    try:
        print(response.json()['result'])
    except Exception:
        pass

def update_proxy(auth, hostid, new_proxy):
    data = {
        "jsonrpc": "2.0",
        "method": "host.update",
        "params": {
            "hostid": hostid,
            "proxy_hostid":new_proxy
        },
        "auth": auth,
        "id": 3
    }
    response = zabbix_request(data)
    try:
        return response.json()['result']
    except Exception:
        pass

def disable_item(auth, itemid):
    data = {
        "jsonrpc": "2.0",
        "method": "item.update",
        "params": {
            "itemid": itemid,
            "status": 1
        },
        "auth": auth,
        "id": 3
    }
    response = zabbix_request(data)
    try:
        pass
        print(response.json()['result'])
    except Exception:
        pass

def enable_item(auth, itemid):
    data = {
        "jsonrpc": "2.0",
        "method": "item.update",
        "params": {
            "itemid": itemid,
            "status": 0
        },
        "auth": auth,
        "id": 3
    }
    response = zabbix_request(data)
    try:
        pass
        #print(response.json()['result'])
    except Exception:
        pass
