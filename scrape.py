import nltk
from newspaper import Article

# select a url of any news article
url = 'https://www.bbc.com/news/world-asia-56875805'
article = Article(url)
article.download()
article.parse()
#nltk.download('punkt')
article.nlp()

print(article.text)
print("Title",article.title)
print("date",article.keywords)
print("author",article.authors)