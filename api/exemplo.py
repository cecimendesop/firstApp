import requests


def exemplo_cep():
    cep = "16700045"
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dadoscep = response.json()
        print(f"Logradouro: {dadoscep['logradouro']}")
        print(f"Bairro: {dadoscep['bairro']}")
        print(f"Localidade: {dadoscep['localidade']}")
        print(f"Estado: {dadoscep['uf']}")
        print(f"Região: {dadoscep['regiao']}")
        print(f"CEP: {dadoscep['cep']}")

        print(f"IBGE: {dadoscep['ibge']}")
    else:
        print(f"Erro: {response.status_code}")


def exemplo_get(id):
    url = f" https://jsonplaceholder.typicode.com/posts/{id}"
    response_get = requests.get(url)
    if response_get.status_code == 200:
        dados_get_postagem = response_get.json()
        print(f"Título: {dados_get_postagem['title']}")
        print(f"Conteúdo: {dados_get_postagem['body']}")
    else:
        print(f"Erro: {response_get.status_code}")


def exemplo_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    nova_postagem = {"title": "Novo título",
                     "body": "Novo conteúdo",
                     "userId": 1
                     }

    response_post = requests.post(url, json=nova_postagem)
    if response_post.status_code == 201:
        dados_post = response_post.json()
        print(f"Título: {dados_post['title']}")
        print(f"Conteúdo: {dados_post['body']}")
    else:
        print(f"Erro: {response_post.status_code}")


def exemplo_put(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    nova_postagem = {
        "id": 1,
        "title": "Novo título",
        "body": "Novo conteúdo",
        "userId": 1
    }
    antes = requests.get(url)
    response_put = requests.put(url, json=nova_postagem)
    if response_put.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f"Titulo Antes: {dados_antes['title']}")
            print(f"Conteúdo antes: {dados_antes['body']}")
        else:
            print(f"Erro: {response_put.status_code}")
        dados_put = response_put.json()
        print(f"Título: {dados_put['title']}")
        print(f"Conteúdo: {dados_put['body']}")

    else:
        print(f"Erro: {response_put.status_code}")

# exemplo_get(12)
# exemplo_post()
exemplo_put(6)
