import urllib.request
from newspaper import Article

url="https://newspaper.readthedocs.io/en/latest/"

article = Article(url,keep_article_html=True)
article.download()
article.parse()

print(article.text)