import requests
import json
from googlesearch import search

# function to get the link of the company using the name
def get_emails(tag, n, language):
    urls = [url for url in search(tag, num_results=n, lang=language)][:n]
    response = requests.get("https://api.hunter.io/v2/domain-search?domain="+urls[0]+"&api_key=48398ffff7e3b58d5148fe5c4c2be4646d671313")
    return response.json()


print(get_emails("Kulkarni Power Tools",5,"en"))

