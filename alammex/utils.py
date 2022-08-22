import requests

def fetch_api_data(chain, api, params):
    subdomain = 'app' if chain == 'mainnet' else 'testnet'
    response = requests.post("https://{subdomain}.alammex.com/api/{api}".format(subdomain=subdomain, api=api), json=params)
    return response.json()