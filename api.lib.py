import json
from settings import *

class Orgstructure:
   
   def __init__(self):
       pass

   def gt(self):
       """Базовый на получение дерева - вспомогательный для других методов, заполненные все параметры"""
       headers = {'accept': 'application/json'}
       params = "project_id=3e3028cd-3849-461b-a32b-90c0d6411dba&item_type=orgstructure&item=start_project"
       res = requests.get("https://api.cloveri.skroy.ru/api/v1/nodes/", params=params, headers=headers)
       tree = ""
       try:
           tree = res.json()
       except json.decoder.JSONDecodeError:
           tree = res.text
       return tree

     def gn(self,id):
       """Базовый на получение дерева - вспомогательный для других методов, заполненные все параметры"""
       headers = {'accept': 'application/json'}
       params = "project_id=3e3028cd-3849-461b-a32b-90c0d6411dba&item_type=orgstructure&item=start_project"
       res = requests.get(f"https://api.cloveri.skroy.ru/api/v1/node/{id}/", params=params, headers=headers)
       status = res.status_code
       res_headers = res.headers
       node = ""
       try:
           node = res.json()
       except json.decoder.JSONDecodeError:
           node = res.text
       return status, node, res_headers

   def g_ch(self, parent_id) -> json:
       """Базовый на получение потомков родительского элемента,
       вспомогательный метод для других методов. Заполненные все параметры"""
       headers = {'accept': 'application/json'}
       params = "project_id=3e3028cd-3849-461b-a32b-90c0d6411dba&item_type=orgstructure&item=start_project"
       res = requests.get(f"https://api.cloveri.skroy.ru/api/v1/nodes/{parent_id}/", params=params, headers=headers)
       status = res.status_code
       children = ""
       try:
           children = res.json()
       except json.decoder.JSONDecodeError:
           children = res.text
       #return status
       return status, children

   def hide_node(self, url, headers, data):
       """Метод по скрытию и восстановлению узлов"""
       res = requests.patch(url, headers=headers, json=data)
       status = res.status_code
       res_headers = res.headers
       result = ""
       try:
           result = res.json()
       except json.decoder.JSONDecodeError:
           result = res.text
       return status, result, res_headers
