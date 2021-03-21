import requests
import json
import config
from googlesearch import search

# function to get the link of the company using the name
def get_emails(tag, n, language):
    urls = [url for url in search(tag, num_results=n, lang=language)][:n]
    response = requests.get("https://api.hunter.io/v2/domain-search?domain="+urls[0]+"&api_key="+config.api_secret)
    return response
    
def get_linkedIn(tag, n, language):
    urls = [url for url in search(tag, num_results=n, lang=language)][:n]
    return urls[0]

print(get_emails("Kulkarni Power Tools",5,"en"))

