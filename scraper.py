import requests
from bs4 import BeautifulSoup
import json

def get_article_urls(page_url, session):
    response = session.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    urls = [article.find('header').find('a').get('href') for article in articles if article.find('header').find('a')]
    return urls

# Function to set up the requests session
def setup_session():
    session = requests.Session()
    return session

# Main scraping function
def scrape_articles(urls_list):
    session = setup_session()
    all_article_urls = []

    for url in urls_list:
        print(f"Scraping {url}")
        article_urls = get_article_urls(url, session)
        all_article_urls.extend(article_urls)

    return all_article_urls

def handler(event, context):
    urls_list = [
        'https://clearseasresearch.com/blog/'
    ]
    article_urls = scrape_articles(urls_list)
    return {"statusCode": 200, "body": json.dumps(article_urls)}