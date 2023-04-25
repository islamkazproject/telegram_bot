import requests


def get_random_answer():
    response = requests.get('https://yesno.wtf/api')
    data = response.json()
    return data['answer']

