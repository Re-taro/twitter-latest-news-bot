from credential import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET
from twython import Twython,TwythonError
import feedparser

RSS_URL='https://www.gizmodo.jp/index.xml'
news_dic=feedparser.parse(RSS_URL)
latest_entry=news_dic['entries'][0]
message=latest_entry.title+latest_entry.link

twitter=Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

try:
    twitter.update_status(status=message)
except TwythonError as e:
    print(e)