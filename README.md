# ZabbixPyAPI

A simple python lib for using the Zabbix API

## Uso/Exemplos

```python
import Zabbix_PyAPI from ZabbixPyAPI

api = Zabbix_PyAPI('zabbixurl.com/api_jsonrpc.php','zabbix_login','zabbix_psw')

params = {
    "groupids":"1547",
    "output":["name"]
}

api.request("host.get", params)
```
