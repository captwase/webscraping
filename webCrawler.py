import requests
from bs4 import BeautifulSoup

urls = input("Enter the url: ")
for url in urls:
    print(urls)
    response =  requests.get("http://" + urls)
    soup = BeautifulSoup(response.text, "html.parser")

    metas = soup.find_all('meta')
    title = soup.find_all('title')

    for meta in metas:
        if 'name' in meta.attrs:
            if meta.attrs['name'] == 'description':
                print('description')
                print(meta.attrs['content'])
                
            if meta.attrs['name'] == 'keywords':
                print('keywords')
                print(meta.attrs['content'])
                
                
        if 'property' in meta.attrs:
            if meta.attrs['property'] == 'og:description':
                print('d2')
                print(meta.attrs['content'])
                
            if meta.attrs['property'] == 'og:keywords':
                print('k2')
                print(meta.attrs['content'])
                
                
        print("title",title[0].string)