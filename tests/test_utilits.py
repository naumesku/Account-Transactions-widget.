import pytest
from utilits_all import utils, config



def test_prepares_data_operations():
    assert utils.prepares_data_operations(config.PATH_OPERATIONS, 1) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}]
    assert utils.prepares_data_operations(config.PATH_OPERATIONS,2)== [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}]

def test_date_format():
    assert utils.date_format('2019-12-08T22:46:21.935582') == "08.12.2019"

def test_disguise_accounts():
    assert utils.disguise_accounts('Счет 90424923579946435907') == "  -> Счет **5907"
    assert utils.disguise_accounts('Счет 35158586384610753655', 'Visa Classic 2842878893689012') == "Visa Classic 2842 87** **** 9012 -> Счет **3655"
    assert utils.disguise_accounts('Счет 90424923579946435907','Счет 90424923579946435907') == "Счет **5907 -> Счет **5907"

