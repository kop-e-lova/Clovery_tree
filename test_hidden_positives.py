from api_lib import Orgstructure
from settings import *


correct_headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
upper_headers = {'ACCEPT': 'APPLICATION/JSON', 'CONTENT-TYPE': 'APPLICATION/JSON'}
mixed_headers = {'accept':'APPLICATION/JSON','CONTENT-TYPE': 'application/json' }
url = "https://api.cloveri.skroy.ru/api/v1/node/3051/hidden/"
wrong_accept_headers = {'accept': 'text/html'}
org_s = Orgstructure()
tree = org_s.gt()
data_del_root = {"project_id": project_id, "item_type": item_type,
       "item": item, "hidden": True, "affect_descendants": True}
       #опциональный параметр, необходимость удалять/восстанавливать всех потомков, принимает
       # значения True или False, по дефолту установлено True:
       #"affect_descendants": True}

def test_delete_node(url=url,headers=correct_headers, data=data_del_root):
    """OS-API-Dn-1 Базовый тест на удаление - элемент без дочек. Id элемента 3051 - pass"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_hidden_3051_node():
    status, result, res_headers = org_s.gn(3051)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert result == {'error': 'does not exist object(s)'}

def test_hidden_in_tree_node_3051():
    result = org_s.gt()
    print(f"Response: {result}")
    #for n in result[0]: assert "3051" in n
    #ids = [n['id'] for n in result]
    #print(ids)
    #assert 3051 in ids
    assert 3051 not in [n['id'] for n in result]

def test_restore_node(url=url, headers=correct_headers,
                     data={"project_id": project_id, "item_type": item_type,
       "item": item, "hidden": None}):
    """OS-API-Rn-1 Базовый тест на восстановление - элемент без дочек Id элемента 3051"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_get_3051_node():
    status, result, res_headers = org_s.gn(3051)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_get_in_tree_node_3051():
    result = org_s.gt()
    print(f"Response: {result}")
    #for n in result[0]: assert "3051" in n
    #ids = [n['id'] for n in result]
    #print(ids)
    #assert 3051 in ids
    assert 3051 in [n['id'] for n in result]

#Удаление/восстановление родительского элемента и его потомков

def test_delete_parent_node(url="https://api.cloveri.skroy.ru/api/v1/node/2916/hidden/",
                            headers=correct_headers, data=data_del_root):
    """OS-API-Dn- Базовый тест на yдаление - элемента с дочками. Id элемента 2916 """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_hidden_2916_node():
    #Проверка невозможности получения узла методом get_node
    status, result, res_headers = org_s.gn(2916)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 404
    assert result == {'error': 'does not exist object(s)'}

def test_hidden_in_tree_node_2916():
    # Проверка отсутствия узла в дереве
    result = org_s.gt()
    print(f"Response: {result}")
    assert 2916 not in [n['id'] for n in result]

def test_hidden_in_tree_descendants_node_2916():
    # Проверка отсутствия потомков узла 2916 в дереве
    #Параметр affect_descendants_установлен по умолчанию
    result = org_s.gt()
    print(f"Response: {result}")
    ids = [n['id'] for n in result]
    assert 2917 and 2918 not in [n['id'] for n in result]

def test_unsuccesful_get_descendants_2916():
    #Проверка видимости потомков восстановленного родительского узла методом get_descendants
    #Значение affect_descendants_установлено по умолчанию
    status, result = org_s.g_ch(2916)
    print(f"Code: {status}")
    print(f"Response: {result}")
    assert status == 404
    #ids = [n['id'] for n in result]
    #assert 2917 and 2918 in ids

def test_restore_parent_node(url="https://api.cloveri.skroy.ru/api/v1/node/2916/hidden/",
                             headers=correct_headers,data={"project_id": project_id,
                                                           "item_type": item_type,
                                                           "item": item, "hidden": None}):
    """OS-API-Rn-Восстановление - элемента с дочками элемента 2916"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_get_2916_node():
    status, result, res_headers = org_s.gn(2916)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_available_in_tree_descendants_node_2916():
    # Проверка наличия потомков узла 2916 в дереве
    #Параметр affect_descendants_установлен по умолчанию
    result = org_s.gt()
    print(f"Response: {result}")
    ids = [n['id'] for n in result]
    assert 2917 and 2918 in [n['id'] for n in result]

def test_get_descendants_2916():
    #Проверка видимости потомков восстановленного родительского узла методом get_descendants
    #Значение affect_descendants_установлено по умолчанию
    status, result = org_s.g_ch(2916)
    print(f"Code: {status}")
    print(f"Response: {result}")
    assert status == 200
    ids = [n['id'] for n in result]
    assert 2917 and 2918 in ids

#Параметр affect_descendants

#Восстановление ранее удаленного дочернего элемента постредсвом восстановления родителя

#Удаление дочернего элемента 2917, удаление родителя 2016,
# восстановление родителя 2916 (affect_descendants=True), проверка восстановления узла 2917

def test_delete_2917(url="https://api.cloveri.skroy.ru/api/v1/node/2917/hidden/",
                                headers=correct_headers, data=data_del_root):
        status, result, res_headers = org_s.hide_node(url, headers, data)
        print(f"Code: {status}")
        print(f"Response: {result}")
        print(f'Response headers: {res_headers}')
        assert status == 200
        assert result == 'Node(s) deleted'
        assert "'Content-Type': 'application/json'" in str(res_headers)

def test_delete_2916(url="https://api.cloveri.skroy.ru/api/v1/node/2916/hidden/",
                headers=correct_headers, data=data_del_root):
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_restore_2916(url="https://api.cloveri.skroy.ru/api/v1/node/2916/hidden/",
                             headers=correct_headers,data={"project_id": project_id,
                                                           "item_type": item_type,
                                                           "item": item, "hidden": None}):
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'

def test_get_2916_1_node():
    status, result, res_headers = org_s.gn(2916)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_get_2917_node():
    status, result, res_headers = org_s.gn(2917)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200

#affect_descendants=False
#Удаляем 2916 (родительский элемент), проверяем видимость в tree 2917 и 2918

def test_delete_2916_2(url="https://api.cloveri.skroy.ru/api/v1/node/2916/hidden/",
                headers=correct_headers, data={"project_id": project_id, "item_type": item_type,
       "item": item, "hidden": True, "affect_descendants": False}):
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_impossible_get_descendants_2916_1():
    #Невозможности получить потомков от узла 2916
    status, result = org_s.g_ch(2916)
    print(f"Code: {status}")
    print(f"Response: {result}")
    #assert status == 404
    assert result == {'error': 'does not exist object(s)'}

def test_available_in_tree_descendants_node_2916_1():
    # Проверка наличия потомков узла удаленного 2916 в дереве
    #Параметр affect_descendants_установлен по умолчанию
    result = org_s.gt()
    print(f"Response: {result}")
    ids = [n['id'] for n in result]
    assert 2917 and 2918 in [n['id'] for n in result]

def test_get_2917_node_1():
    #Проверка отображения в дереве потомка 2017 удаленного узла 2916 при affect_descendants=False
    status, result, res_headers = org_s.gn(2917)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_get_2918_node_1():
    # Проверка отображения в дереве потомка 2018 удаленного узла 2916 при affect_descendants=False
    status, result, res_headers = org_s.gn(2918)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200

def test_restore_2916_extra(url="https://api.cloveri.skroy.ru/api/v1/node/2916/hidden/",
                             headers=correct_headers,data={"project_id": project_id,
                                                           "item_type": item_type,
                                                           "item": item, "hidden": None, "affect_descendants": False}):
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'

def test_get_descendants_2916_1():
    #Невозможности получить потомков от узла 2916
    status, result = org_s.g_ch(2916)
    print(f"Code: {status}")
    print(f"Response: {result}")
    assert status == 200


#Прочие проверки

def test_delete_node_upper_URL(url="https://API.CLOVERI.SKROY.ru/api/v1/node/3548/hidden/",headers=correct_headers, data=data_del_root):
    """OS-API-Dn-3 Позитивный сценарий. Удаление любого существующего элемента по его id.
    Отправка запроса с URL в верхнем регистре Id элемента 3548 - pass"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_restore_node_upper_url(url="https://API.CLOVERI.SKROY.ru/api/v1/node/3548/hidden/",
                             headers=correct_headers,data={"project_id": project_id,
                                                           "item_type": item_type,
                                                           "item": item, "hidden": None}):
    """OS-API-Rn-Восстановление - элемента UPPER URL (вспомогательный тест)Id элемента 3548"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_delete_child_node(url="https://api.cloveri.skroy.ru/api/v1/node/109/hidden/",
                            headers=correct_headers, data=data_del_root):
    """OS-API-Dn-4 Базовый тест на yдаление - дочернего элемента. Id элемента 109 """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_restore_child_node(url="https://api.cloveri.skroy.ru/api/v1/node/109/hidden/",
                             headers=correct_headers,data={"project_id": project_id,
                                                           "item_type": item_type,
                                                           "item": item, "hidden": None}):
    """OS-API-Rn-4  Восстановление дочернего элемента. Id 109"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_delete_node_upper_headers(url="https://api.cloveri.skroy.ru/api/v1/node/109/hidden/",
                            headers=upper_headers, data=data_del_root):
    """OS-API-Dn-5 Удаление существующего элемента. Отправка запроса с заголовков в верхнем регистре .
    Id элемента 109 """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_restore_upper_headers(url="https://api.cloveri.skroy.ru/api/v1/node/109/hidden/",
                             headers=upper_headers,data={"project_id": project_id,
                                                           "item_type": item_type,
                                                           "item": item, "hidden": None}):
    """OS-API-Rn-5  Восстановление существующего элемента. Отправка запроса с заголовков в верхнем регистре
    Id 109"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_delete_node_mixed_headers(url="https://api.cloveri.skroy.ru/api/v1/node/109/hidden/",
                            headers=mixed_headers, data=data_del_root):
    """OS-API-Dn-6 Удаление существующего элемента. Отправка запроса с заголовков в смешанном регистре .
    Id элемента 109 """
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_restore_mixed_headers(url="https://api.cloveri.skroy.ru/api/v1/node/109/hidden/",
                             headers=mixed_headers,data={"project_id": project_id,
                                                           "item_type": item_type,
                                                           "item": item, "hidden": None}):
    """OS-API-Rn-6  Восстановление существующего элемента. Отправка запроса с заголовков в смешанном регистре
    Id 109"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_delete_another_fields_order(url="https://api.cloveri.skroy.ru/api/v1/node/109/hidden/",
                             headers=mixed_headers,data={"item_type": item_type,
                                                         "project_id": project_id,
                                                           "item": item, "hidden": True}):
    """OS-API-Dn-6  Удаление элемента. Другой порядок полей в запросе
    Id 109"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) deleted'
    assert "'Content-Type': 'application/json'" in str(res_headers)

def test_restore_another_fields_order(url="https://api.cloveri.skroy.ru/api/v1/node/109/hidden/",
                             headers=mixed_headers,data={"item_type": item_type,
                                                         "project_id": project_id,
                                                           "item": item, "hidden": None}):
    """OS-API-Rn-6  Восстановление элемента. Другой порядок полей в запросе
    Id 109"""
    status, result, res_headers = org_s.hide_node(url, headers, data)
    print(f"Code: {status}")
    print(f"Response: {result}")
    print(f'Response headers: {res_headers}')
    assert status == 200
    assert result == 'Node(s) restored'
    assert "'Content-Type': 'application/json'" in str(res_headers)
