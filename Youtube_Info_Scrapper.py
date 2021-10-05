# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:24:27 2021

@author: Adrián
"""
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

urls = [
    'https://www.youtube.com/c/ElUniversalMex/featured'
    # 'https://www.youtube.com/user/thenewboston',
    # 'https://www.youtube.com/user/gotreehouse',
    # 'https://www.youtube.com/user/derekbanas',
    # 'https://www.youtube.com/channel/UCWr0mx597DnSGLFk1WfvSkQ',
    # 'https://www.youtube.com/user/ProgrammingKnowledge'
]

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for url in urls:
        driver.get('{}/videos'.format(url))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        titles = soup.findAll('a',id='video-title')
        views = soup.findAll('span',class_='style-scope ytd-grid-video-renderer')
        video_urls = soup.findAll('a',id='video-title')
        print('Channel: {}'.format(url))
        i = 0 # views and time
        j = 0 # urls
        for title in titles[:10]:
            print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text, views[i].text, views[i+1].text, video_urls[j].get('href')))
            i+=2
            j+=1


