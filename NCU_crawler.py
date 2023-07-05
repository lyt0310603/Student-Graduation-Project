import time
import bs4
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

# count time
process_start = time.perf_counter()

# parameter for web crawler
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'}
dp = "C:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=dp)
url = 'https://forum.gamer.com.tw/C.php?page=1&bsn=60076&snA=4671705'

# save the information of Bahamut article
ArticleContent = []
ArticleReply = []
ArticlePostTime = []
ArticleFloor = []
ContentAndReply = []

# count the page
PageNum = 0

# load page
browser.get(url)

HaveNext = True
while HaveNext:
    # if run the same page number than break the loop
    NowPage = browser.find_element(By.CLASS_NAME, 'pagenow')
    if PageNum == NowPage.text:
        break
    else:
        PageNum = NowPage.text

    # use selenium
    # open the article which is fold
    # in Bahamut if the article get too much hush it will be folded
    FoldArticle = browser.find_elements(By.CLASS_NAME, 'show')
    if len(FoldArticle) != 0:
        time.sleep(0.1)
        for i in FoldArticle:
            i.click()

    # use selenium
    # open the fold reply
    # in Bahamut if the num of reply more than 5 it will be folded
    target = browser.find_elements(By.CLASS_NAME, 'more-reply')
    for i in target:
        i.click()
    time.sleep(0.1)

    # use beautifulsoup
    ObjSoup = bs4.BeautifulSoup(browser.page_source, 'lxml')
    ObjTag = ObjSoup.find_all('section', class_='c-section', id=re.compile('post'))
    for i in ObjTag:
        # get article content
        ObjContent = i.find('div', class_='c-article__content')

        # get article reply
        ObjReply = i.find_all('span', class_='comment_content')

        # get article time
        ObjTime = i.find('a', class_='edittime tippy-post-info')

        # get article floor
        ObjFloor = i.find('a', class_='floor tippy-gpbp')

        # save article content
        ArticleContent.append(ObjContent.text.strip())

        # save article time
        ArticlePostTime.append(ObjTime['data-mtime'])

        # save article floor
        ArticleFloor.append(ObjFloor['data-floor'])

        # save article reply
        # use list to save replies
        ArticleReply.append([])
        s = "Content:" + '\n' + ObjContent.text.strip() + '\n' + "Reply:" + '\n'
        for reply in ObjReply:
            ReplyWithoutBlank = reply.text.strip()
            s += ReplyWithoutBlank
            ArticleReply[len(ArticleReply) - 1].append(ReplyWithoutBlank)
            if reply != ObjReply[len(ObjReply) - 1]:
                s += ", "
        # for convenience in label task save content and replies in one term
        ContentAndReply.append(s)

    NextPage = browser.find_element(By.CLASS_NAME, 'next')
    NextPage.click()
    time.sleep(0.5)

# print the time consume
process_end = time.perf_counter()
print('共耗時'+str(process_end-process_start)+'秒')
print(ContentAndReply)

# save in csv
s_reply = pd.Series(ArticleReply)
s_content = pd.Series(ArticleContent)
s_time = pd.Series(ArticlePostTime)
s_floor = pd.Series(ArticleFloor)
s_content_reply = pd.Series(ContentAndReply)
t = pd.concat([s_time, s_floor, s_content_reply, s_content, s_reply], axis=1)
adj = ['time', 'floor', 'content_and_reply', 'content', 'reply']
t.columns = adj
t.to_csv('中央大學.csv', index=False, encoding='utf-8-sig')
