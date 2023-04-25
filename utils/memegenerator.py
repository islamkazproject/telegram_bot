import random
import requests


def get_random_meme_url():
    response = requests.get('https://api.imgflip.com/get_memes')
    data = response.json()
    memes = data['data']['memes']
    random_meme = memes[random.randint(0, len(memes) - 1)]
    meme_url = random_meme['url']
    return meme_url
