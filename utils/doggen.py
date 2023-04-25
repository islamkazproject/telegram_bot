import requests


def get_random_dog():
    response = requests.get('https://random.dog/woof.json')
    data = response.json()
    return data['url']