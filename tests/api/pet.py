import csv

import pytest     # motor / engine
import requests  # biblioteca para comunicar com APIs


base_url = 'https://petstore.swagger.io/v2'   #endereço da API
headers = {'Content-Type': 'application/json'}   # os dados serão no formato json


class Exceptionxception:
    pass


def ler_dados_csv():
    dados_csv = []  # criamos uma lista vazia
    nome_arquivo = 'C:\\Users\\Altec\\PycharmProjects\\133Pets\\vendors\\csv\\pets_positivo.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exceptionxception as fail:
        print(f'Falha não prevista: {fail}')

def testar_incluir_pet():
    # Configura
    # Dados de entrada: virão do pet1.json
    # Resultado Esperado
    status_code_esperado = 200
    nome_pet_esperado = 'mel'
    tag_esperada = 'castrado, vacinado'

# Executa
    resulta_obtido = requests.post(url=base_url + '/pet',
              data=open('C:\\Users\\Altec\\PycharmProjects\\133Pets\\vendors\\json\\pet1.json', 'rb'),
              headers=headers
              )
# Valida
    print(resulta_obtido)
    corpo_da_resposta = resulta_obtido.json()
    print(corpo_da_resposta)
    assert resulta_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada


def testar_consultar_pet():
    # Configura

    # DADOS DE ENTRADA
    pet_id = '385023'
    # RESULTADOS ESPERADOS
    status_code_esperado = 200
    nome_pet_esperado = 'mel'
    tag_esperada = 'castrado, vacinado'

    # Executa
    resultado_obtido = requests.get(
        url=base_url + '/pet/' + pet_id,
        headers=headers
    )
    # Valida
    print(resultado_obtido)
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['tags'][0]['name'] == tag_esperada


def testar_alterar_pet():
    status_code_esperado = 200
    nome_pet_esperado = 'mel'
    status_esperado = 'solded'

    resultado_obtido = requests.put(
    url=base_url + '/pet',
    data=open('C:\\Users\\Altec\\PycharmProjects\\133Pets\\vendors\\json\\pet2.json', 'rb'),
    headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert corpo_da_resposta["name"] == nome_pet_esperado
    assert corpo_da_resposta['status'] == status_esperado


def testar_deletar_pet():
  pet_id = '385023'
  status_code_esperado = 200
  code_esperado = 200
  type_esperado = 'unknown'

  resultado_obtido = requests.delete(
    url=base_url + '/pet/' + pet_id,
    headers=headers
  )
  assert resultado_obtido.status_code == status_code_esperado
  corpo_da_resposta = resultado_obtido.json()
  assert corpo_da_resposta['code'] == code_esperado
  assert corpo_da_resposta['type'] == type_esperado
  assert corpo_da_resposta['message'] == pet_id

@pytest.mark.parametrize('pet_id,category_id,category_name,name,tags_id,tags_name,status,status_code', ler_dados_csv())
def testar_incluir_pet_json_dinamico(pet_id,category_id,category_name,name,tags_id,tags_name,status,status_code):
    # 1 - Configura
    # 1.1 - Dados de entrada
    # Ultilizara o arquivo pets_positivo.csv

    # 1.2 - Resultados esperados
    # Ultilizara o arquivo pets_positivo.csv

    # 1.3 - Extra - Montar o Json dinamicamente a partir do CSV
    corpo_json = '{'
    corpo_json += f'  "id": {pet_id},'
    corpo_json += '  "category": {'
    corpo_json += f'    "id": {category_id},'
    corpo_json += f'    "name": {category_name}'
    corpo_json += '},'
    corpo_json += f'"name": {name},'
    corpo_json += '"string"'
    corpo_json += '],'
    corpo_json += '"photoUrls": ['
    corpo_json += '"tags": ['
    corpo_json += '{'
    corpo_json += f'    "id": {tags_id},'
    corpo_json += f'    "name": {tags_name}'
    corpo_json += '}'
    corpo_json += '],'
    corpo_json += f'"status": {status}'
    corpo_json += '}'


    # 2 - Executa
    resultado_obtido = requests.post(
        url=base_url + '/pet/',

    )
    #

    # 3 - Valida