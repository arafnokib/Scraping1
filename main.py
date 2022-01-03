from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

url = "https://www.youtube.com/c/Freecodecamp/videos"
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, 'html.parser')
driver = webdriver.Chrome('/Users/arafnokib/Downloads/Whitehat/Python/WebScraping/web4/chromedriver', options=chrome_options)
driver.get(url)

time.sleep(10)

#titles = driver.find_elements_by_class_name('yt-simple-endpoint style-scope ytd-grid-video-renderer')
#vids = driver.find_elements_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[3]')
vids = driver.find_elements_by_class_name('style-scope ytd-grid-renderer')

vid_details = []

for vid in vids:
    #title = vid.find_element_by_id('video-title').text
    details = vid.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
    for detail in details:
        vid_details.append(detail.text)
    
d1 = pd.DataFrame(vid_details)
d1.to_csv('video_details.csv')





#videos = soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-grid-video-renderer')
#print(videos)

