import requests
import bs4
url="https://www.istockphoto.com/photos/product"
response = requests.get(url)
print(response.text)