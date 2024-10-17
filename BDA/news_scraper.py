from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
from datetime import datetime


# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['nifty_it_news']
collection = db['news_collection']

def scrape_news_to_mongodb():
    url = 'https://www.moneycontrol.com/news/business/stocks/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}    

    # Fetch the webpage
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Find the body element with class 'page_container'
    body_container = soup.find('body', class_='page_container')
    if body_container:
        section_container = body_container.find('section', id='mid')
        if section_container:
            div_container = section_container.find('div', id='left')
            if div_container:
                category_list = div_container.find('ul', id='cagetory')
                if category_list:
                    news_articles = []
                    current_date = datetime.now().strftime('%m/%d/%Y')
                    list_items = category_list.find_all('li', class_='clearfix')
                    for list_item in list_items:
                        title_tag = list_item.find('h2').find('a')
                        title = title_tag.text if title_tag else 'No title found'
                        p_tags = list_item.find_all('p')
                        content = ' '.join([p.text for p in p_tags])
                        news_item = {
                            'Title': title,
                            'Description': content,
                            'Date': current_date
                        }
                        if not collection.find_one({'Title': title}):
                            collection.insert_one(news_item)
                            news_articles.append(news_item)
                    return news_articles
    return []

# Run the function and insert the scraped data into MongoDB
news_data = scrape_news_to_mongodb()
if news_data:
    print(f"Inserted {len(news_data)} new news articles into MongoDB.")
else:
    print("No new news articles to insert.")
