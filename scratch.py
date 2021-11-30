import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

# does not execute JS
response = requests.get(YOUTUBE_TRENDING_URL)

with open('trending.html','w') as f:
  f.write(response.text)

soup = BeautifulSoup(response.text,'lxml')

print(soup.title.text)

video_divs = soup.find_all('div',class_='ytd-video-renderer')
print(len(video_divs))