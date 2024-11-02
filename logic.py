import requests
def get_joke():
    API_URL = "https://geek-jokes.sameerkumar.website/api?format=json"
    res = requests.get(API_URL).json()
    return res['joke']