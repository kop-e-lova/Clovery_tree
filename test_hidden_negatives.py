from api_lib import Orgstructure
from settings import *
from ids import *
import json
import pytest

correct_headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
upper_headers = {'ACCEPT': 'APPLICATION/JSON', 'CONTENT-TYPE': 'APPLICATION/JSON'}
mixed_headers = {'accept':'APPLICATION/JSON','CONTENT-TYPE': 'application/json' }
url = f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/"
upper_url = "https://API.CLOVERI.SKROY.ru/"
wrong_accept_headers = {'accept': 'text/html'}
wrong_content_type_headers = {'Content-Type': 'application/xml'}
tree = org_s.gt()
data_del_root = {"project_id": project_id, "item_type": item_type,
       "item": item, "hidden": True}
       #опциональный параметр, необходимость удалять/восстанавливать всех потомков, принимает
       # значения True или False, по дефолту установлено True:
       #"affect_descendants": True}

def test_delete_node_neg_no_id(url=f"https://api.cloveri.skroy.ru/api/v1/node/hidden/", headers=correct_headers, data=data_del_root):
    """ OS-API-Dn-7 Попытка удаления элемента структуры без указания его id в Path  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404

id = None
def test_delete_node_neg_id_None(url=f"https://api.cloveri.skroy.ru/api/v1/node/{id}/hidden/", headers=correct_headers, data=data_del_root):
    """ OS-API-Dn-48 Попытка удаления элемента. Значение id None (null)  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    #assert result == 'Node(s) deleted'
    #assert "'Content-Type': 'application/json'" in str(res_headers)

def test_delete_node_neg_id_wrong_format(url=f"https://api.cloveri.skroy.ru/api/v1/node/abd/hidden/", headers=correct_headers, data=data_del_root):
    """ OS-API-Dn-8 Попытка удаления элемента. Значение id неверного формата  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404

id= {"kjl":"lkjk"}
def test_delete_node_neg_id_wrong_format1(url=f"https://api.cloveri.skroy.ru/api/v1/node/{id}/hidden/", headers=correct_headers, data=data_del_root):
    """ OS-API-Dn-8-1 опытка удаления элемента. Значение id неверного формата dict  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    print(f'id удалённого элемента: {root_node_id}')
    assert status == 404

def test_delete_node_neg_id_in_body(url=f"https://api.cloveri.skroy.ru/api/v1/node//hidden/",
                                    headers=correct_headers,
                                    data={"id": 67,
                                          "project_id": project_id, "item_type": item_type,
       "item": item, "hidden": True}):
    """ OS-API-Dn-9 Удаление элемента структуры. Попытка отправить запрос с указанием id элемента
    в другом месте запроса (body) вместо path """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    print(f'id удалённого элемента: {root_node_id}')
    assert status == 404

def test_delete_node_neg_id_in_params(url=f"https://api.cloveri.skroy.ru/api/v1/node//hidden/?id=1907",
                                      headers=correct_headers, data=data_del_root):
    """ OS-API-Dn-10 Удаление элемента структуры. Попытка отправить запрос с указанием id элемента
    в query_params вместо path """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404

id = ''
def test_delete_node_neg_id_empty(url=f"https://api.cloveri.skroy.ru/api/v1/node/{id}/hidden/",
                                      headers=correct_headers, data=data_del_root):
    """ OS-API-Dn-10 Удаление элемента структуры. Попытка отправить запрос
    с указанием пустого id элемента """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404

id = 99999999999999999999999999
def test_delete_node_neg_id_non_existant(url=f"https://api.cloveri.skroy.ru/api/v1/node/{id}/hidden/",
                                      headers=correct_headers, data=data_del_root):
    """ OS-API-Dn-10 Удаление элемента структуры. Попытка отправить запрос
    с указанием несуществующего id элемента, выходящего за пределы bigint """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert result == {'error': 'does not exist object(s)'}


def test_delete_node_neg_id_in_headers(url=f"https://api.cloveri.skroy.ru/api/v1/node/hidden/",
                                      headers={'accept': 'application/json', 'Content-Type': 'application/json', 'id': "123"},
                                         data=data_del_root):
    """ OS-API-Dn-40 Удаление элемента структуры. Попытка отправить запрос
    с указанием id элемента в headers """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404

def test_delete_node_neg_no_obligatoty_fields(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={#"project_id": project_id,
                                     #"item_type": item_type,
                                     #"item": item,
                                     "hidden": True}):
    """ OS-API-Dn-12 Попытка удаления элемента без указания трёх обязательных параметров (project_id, item_type, item) в теле запроса  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field project_id is required', 'field item_type is required', 'field item is required']}

def test_delete_node_neg_no_project_id(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={#"project_id": project_id,
                                     "item_type": item_type,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-12 Попытка удаления элемента без project_id в теле запроса  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field project_id is required']}

def test_delete_node_neg_no_item_type(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     #"item_type": item_type,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-14 Попытка удаления элемента без item_type в теле запроса  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field item_type is required']}

def test_delete_node_neg_no_item(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": item_type,
                                     #"item": item,
                                     "hidden": True}):
    """ OS-API-Dn-15 Попытка удаления элемента без item в теле запроса  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field item is required']}

def test_delete_node_neg_wrong_field_name(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_ids": project_id,
                                     "item_type": item_type,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-16 Попытка удаления элемента c неправильным полем в теле  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    #assert result == {'errors': ['project_id field is required', 'project_ids not allowed', 'project_id has wrong format, must be uuid']}

#Project_id

def test_delete_node_neg_empty_project_id(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": "",
                                     "item_type": item_type,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-17 Попытка удаления элемента с пустыми значениями поля project_id  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['project_id has wrong format, must be uuid']}

def test_delete_node_neg_wrong_format_project_id(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": 123,
                                     "item_type": item_type,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-20 Попытка удаления элемента и отправления запроса со значением project_id неверного формата  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['project_id has wrong format, must be uuid']}

def test_delete_node_neg_None_project_id(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": None,
                                     "item_type": item_type,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-20 Попытка удаления элемента и отправления запроса со значением project_id None  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['project_id has wrong format, must be uuid']}

def test_delete_node_neg_another_project_id(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": "3e3028cd-3849-461b-a32b-90c0d6411dbb",
                                     "item_type": item_type,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-45 Попытка удаления элемента и отправления запроса с другим значением project_id  """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert result == {'error': 'does not exist object(s)'}

#item_type

def test_delete_node_neg_empty_item_type(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": "",
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-18 Попытка удаления элемента с пустыми значениями поля item_type
     fail 400, старый текст ошибки {'item_type': ['This field may not be blank.']} """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    #assert result ==

def test_delete_node_neg_wrong_format_item_type(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": 123,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-49 Попытка удаления элемента с пустыми значениями поля item_type """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['item_type has wrong format, must be str']}

def test_delete_node_neg_None_item_type(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": None,
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-24 Попытка удаления элемента и отправления запроса со значениями none
    (null) обязательного параметра item_type - fail!!!!!!!!!!!!!!!!
     400, старый текст {'item_type': ['This field may not be null.']}
     в тесте 04.06 -
     Response: {'error': 'does not exist object(s)'}
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    #assert result == {'errors': ['item_type has wrong format, must be str']}

def test_delete_node_neg_wrong_another_item_type(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": "item_type",
                                     "item": item,
                                     "hidden": True}):
    """ OS-API-Dn-46 Попытка удаления элемента и отправления запроса с несуществующим значением
    обязательного параметра item_type"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert result == {'error': 'does not exist object(s)'}

def test_delete_node_neg_empty_item(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": item_type,
                                     "item": "",
                                     "hidden": True}):
    """ OS-API-Dn-19 Попытка удаления элемента с пустыми значениями поля item
     fail 400, старый текст ошибки {'item': ['This field may not be blank.']} """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    #assert result ==

def test_delete_node_neg_wrong_format_item(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": item_type,
                                     "item": 123,
                                     "hidden": True}):
    """ OS-API-Dn-50 Попытка удаления элемента с неверным форматом item
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['item has wrong format, must be str']}

def test_delete_node_neg_None_item(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": item_type,
                                     "item": None,
                                     "hidden": True}):
    """ OS-API-Dn-25 Попытка удаления элемента с None item
    fail 400 старый текст ошибки {'item': ['This field may not be null.']}
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    #assert result ==

def test_delete_node_neg_another_item(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": item_type,
                                     "item": "item",
                                     "hidden": True}):
    """ OS-API-Dn-47 Попытка удаления элемента с None item
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert result == {'error': 'does not exist object(s)'}

def test_delete_node_neg_upper_fields_obligatory_parametres(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"PROJECT_ID": project_id,
                                     "ITEM_TYPE": item_type,
                                     "ITEM": item,
                                     "hidden": True}):
    """ OS-API-Dn-39 Удаление элемента структуры. Отправка запроса с ключами полей project_id, item_type, item
    в теле в верхем регистре
    failed - лишняя фраза в тексте ошибки 'project_id has wrong format, must be uuid']
     {'errors': ['project_id field is required', 'item_type field is required', 'item field is required',
     'PROJECT_ID not allowed', 'ITEM_TYPE not allowed', 'ITEM not allowed',
     'project_id has wrong format, must be uuid']}
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field project_id is required', 'field item_type is required', 'field item is required', 'field PROJECT_ID not allowed', 'field ITEM_TYPE not allowed', 'field ITEM not allowed']}

def test_delete_node_neg_upper_fields_All_parametres(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"PROJECT_ID": project_id,
                                     "ITEM_TYPE": item_type,
                                     "ITEM": item,
                                     "HIDDEN": True}):
    """ OS-API-Dn-51 Удаление элемента структуры. Отправка запроса с ключами полей project_id, item_type, item
    в теле в верхем регистре
    FAILED в теле в верхем регистре
    failed - лишняя фраза в тексте ошибки 'project_id has wrong format, must be uuid']

     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['project_id field is required', 'item_type field is required', 'item field is required', 'PROJECT_ID not allowed', 'ITEM_TYPE not allowed', 'ITEM not allowed', 'HIDDEN not allowed']}

def test_delete_node_neg_upper_fields_All_parametres(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"PROJECT_ID": project_id,
                                     "ITEM_TYPE": item_type,
                                     "ITEM": item,
                                     "HIDDEN": True}):
    """ OS-API-Dn-51 Удаление элемента структуры. Отправка запроса с ключами полей project_id, item_type, item
    в теле в верхем регистре
    FAILED в теле в верхем регистре
    failed - лишняя фраза в тексте ошибки 'project_id has wrong format, must be uuid']

     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field project_id is required', 'field item_type is required', 'field item is required', 'field hidden is required', 'field PROJECT_ID not allowed', 'field ITEM_TYPE not allowed', 'field ITEM not allowed', 'field HIDDEN not allowed']}

def test_hide_node_body_dict():
    """OS-API-Dn-42 Удаление элемента. Попытка запроса с телом запроса в формате dict"""
    res = requests.patch(url, headers=correct_headers, data=data_del_root)
    status = res.status_code
    res_headers = res.headers
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 400
    assert result == 'JSON parse error - Expecting value: line 1 column 1 (char 0)'

def test_hide_node_body_string():
    """OS-API-Dn-42 Удаление элемента. Попытка запроса с телом запроса в формате string"""
    res = requests.patch(url, headers=correct_headers, data=str(data_del_root))
    status = res.status_code
    res_headers = res.headers
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 400
    assert result == ('JSON parse error - Expecting property name enclosed in double quotes: line 1 '
 'column 2 (char 1)')

def test_delete_node_neg_parametres_in_headers(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers={'accept': 'application/json',
                                        'Content-Type': 'application/json',
                                        'project_id': project_id,
                                        'item_type': item_type,
                                        'item': item},
                               data={"hidden": True}):
    """ OS-API-Dn-41 Попытка запроса с  item, project_id, item_type в заголовках запроса
    failed - странный ответ: {'errors': ['project_id field is required', 'item_type field is required', 'item field is required', 'project_id has wrong format, must be uuid']}

     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field project_id is required', 'field item_type is required', 'field item is required']}

def test_delete_node_neg_empty_json(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={}):
    """ Удаление элемента. Попытка запроса с пустым json
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field project_id is required', 'field item_type is required', 'field item is required', 'field hidden is required']}

def test_hide_node_wrong_method():
    """OS-API-Dn-27 Удаление элемента. Попытка запроса с телом запроса в формате dict"""
    res = requests.put(url, headers=correct_headers, data=str(data_del_root))
    status = res.status_code
    res_headers = res.headers
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 405
    assert result == {'detail': 'Method "PUT" not allowed.'}

def test_delete_node_wrong_url(url=f"https://petfriends.skillfactory.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data=data_del_root):
    """ OS-API-Dn-30 Неверный url
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404


def test_delete_node_wrong_endpoint(url=f"https://api.cloveri.skroy.ru/api/a1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data=data_del_root):
    """ OS-API-Dn-31 Неверный эндпоинт
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404

def test_delete_node_no_headers(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=None,
                               data=data_del_root):
    """ OS-API-Dn-32 Неверный эндпоинт
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    #assert status == 404

def test_delete_node_wrong_content_type_in_headers(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=wrong_content_type_headers,
                               data=data_del_root):
    """ OS-API-Dn-33 Неверный content_type в заголовках
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 415
    assert result == 'Unsupported media type "application/xml" in request.'

def test_delete_node_extra_field(url=f"https://api.cloveri.skroy.ru/api/v1/node/{root_node_id}/hidden/",
                               headers=correct_headers,
                               data={"project_id": project_id,
                                     "item_type": item_type,
                                     "item": item,
                                     "hidden": True,
                                     "extra_field": 1}):
    """ OS-API-Dn-31 Попытка отправить запрос с лишним полем в теле запроса
     """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 422
    assert result == {'errors': ['field extra_field not allowed']}
