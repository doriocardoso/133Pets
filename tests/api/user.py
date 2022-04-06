import pytest
import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {'Content-Type': 'application/json'}


def testar_incluir_user():
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = '123456789'


    resultado_obtido = requests.post(url=base_url + '/user',
                        data=open('C:\\Users\\Altec\\PycharmProjects\\133Pets\\vendors\\json\\user1.json', 'rb'),
                        headers=headers,
                        )

    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperado
    assert corpo_da_resposta['code'] == code_esperado





def testar_logar_user():
    type_esperado = 'unknown'
    status_code_esperado = 200
    '''message_esperado = 'logged in user session'''

    resultado_obtido = requests.get(
        url=base_url + '/user/' + 'login?username=andrecardoso&password=123456',
        headers=headers
    )
    corpo_da_resposta = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    '''assert corpo_da_resposta['message'] == message_esperado'''
    assert corpo_da_resposta['type'] == type_esperado
    print(corpo_da_resposta)


def testar_alterar_user():
    status_code_esperado = 200
    type_esperado = 'unknown'
    '''message_esperado = '''

    resultado_obtido = requests.put(
        url=base_url + '/user/' + 'andrecardoso',
        data=open('C:\\Users\\Altec\\PycharmProjects\\133Pets\\vendors\\json\\user2.json', 'rb'),
        headers=headers
        )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    '''assert corpo_da_resposta['message'] == message_esperado'''

def testar_deletar_user():
    status_code_esperado = 200
    type_esperado = 'unknown'
    message_esperado = 'andrecardosodesa'

    resultado_obtido = requests.delete(
        url=base_url + '/user/' + 'andrecardosodesa',
        headers=headers
    )

    corpo_da_resposta = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == status_code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == message_esperado
    print(corpo_da_resposta)






