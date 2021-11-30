import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    print(f'[x] Creating chrome driver object for selenium')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_videos(driver):
    print('[x] Fetching YouTube trending videos page')
    driver.get(YOUTUBE_TRENDING_URL)
    VIDEO_DIV_TAG = 'ytd-video-renderer'
    videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
    return videos


def parse_video(video):
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')

    thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    channel_tag = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel_name = channel_tag.text

    description_tag = video.find_element(By.ID, 'description-text')
    description = description_tag.text

    return {
        'title': title,
        'url': url,
        'channel_name': channel_name,
        'thumbnail_url': thumbnail_url,
        'description': description
    }


if __name__ == "__main__":
    YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

    driver = get_driver()
    videos = get_videos(driver)

    print('[x] Parsing Videos')
    videos_data = [parse_video(video) for video in videos]

    videos_df = pd.DataFrame(videos_data)
    videos_df.to_csv('videos.csv', index=False)
    print('[x] Trending videos data stored as a CSV file!')
