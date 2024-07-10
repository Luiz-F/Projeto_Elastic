import requests
import json
import pandas as pd
from time import sleep
headers = {'Content-Type': 'application/json'}

def pesquisar(index,palavra='null'):
    if palavra == 'null':
        url=f'https://localhost:9200/{index}/_search/'
        rows = []
        response = requests.get(url,auth=('elastic','X1BhM06tu*vKc2IQii*m'),verify='http_ca.crt')
        response_df = pd.DataFrame(response.json()['hits']['hits'])
        for i in response_df['_source']:
            rows.append(i)
        response_df2 = pd.DataFrame(raws,index=response_df['_id'])
        response_df2.index = response_df2.index.astype(int)
        response_df2.index.name = 'ID'
        print(response_df2.sort_values('ID')) 
    else:
        url=f'https://localhost:9200/{index}/_search?q={palavra}'
        response = requests.get(url,auth=('elastic','X1BhM06tu*vKc2IQii*m'),verify='http_ca.crt')
        response_json = response.json()
        rows=[]
        response_df = pd.DataFrame(response.json()['hits']['hits'])
        for i in response_df['_source']:
            rows.append(i)
        response_df2 = pd.DataFrame(raws,index=response_df['_id'])
        response_df2.index = response_df2.index.astype(int)
        response_df2.index.name = 'ID'
        print(response_df2) 
        


def cadastrar(index,id,nome,idade,cidade):
    url=f'https://localhost:9200/{index}/_doc/{id}'
    payload = {'nome':nome,'idade':idade,'cidade':cidade}
    #print(url,payload)
    response = requests.post(url,auth=('elastic','X1BhM06tu*vKc2IQii*m'),verify='http_ca.crt',data=json.dumps(payload),headers=headers)
    print(f'A pessoa {nome} foi cadastrada no index {index}, seguem os dados abaixo: ')
    print(pd.DataFrame(payload,index=[id]))


def deletar(index,id):
    url=f'https://localhost:9200/{index}/_doc/{id}'
    response = requests.delete(url,auth=('elastic','X1BhM06tu*vKc2IQii*m'),verify='http_ca.crt')
    print(response.json())

print("Qual operação voce desejar fazer no Elastic?")
print("""Digite a opção desejada:
      1: Consultar
      2: Inserir
      3: Deletar""")
opcao = input() 
if opcao == '1':
    print("Deseja buscar todos ou somente alguem especifico?")
    parametro = input("""
    1- Uma pessoa
    2- Todos 
    : """)
    index = input("Digite o index que deseja: ")
    while not index:
        index = input("Digite o index que deseja: ")
    if parametro == '1':
        palavra = input("Digite a palavra que deseja procurar: ")
        pesquisar(index,palavra)
    else:
        pesquisar(index)

elif opcao == '2':
    index = input("Digite o index que deseja: ")
    id = input("Digite o id que deseja criar: ")
    nome = input("Digite o nome: ")
    idade =input("Digite a idade: ")
    cidade = input("Digite a cidade: ")
    cadastrar(index,id,nome,idade,cidade)    
elif opcao == '3':
    index = input("Digite o index que deseja: ")
    while not index:
        index = input("Digite o index que deseja: ")
    pesquisar(index)
    id = input("Digite o id acima que deseja excluir: ")
    while not id:
        id = input("Digite o id que deseja excluir: ")
    deletar(index,id)
    sleep(3)
    pesquisar(index)


