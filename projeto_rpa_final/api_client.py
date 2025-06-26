import requests

def obter_piada():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('value', '')
    else:
        raise Exception("Erro ao acessar a API.")
