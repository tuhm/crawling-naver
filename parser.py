#import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import time

#print("initializing")
email = ["@naver.com","@gmail.com","@hanmail.net","@daum.net","@hotmail.com","@nate.com"]
users = []

#login credential required
driver = webdriver.Chrome('/Users/tuhm/Documents/Dr_Kitchen/crawling-naver/chromedriver')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('ketopeople')
driver.find_element_by_name('pw').send_keys('dkcomm!!')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

urls = ["https://cafe.naver.com/lchfkorea?iframe_url=/ArticleList.nhn%3Fsearch.clubid=28737666%26search.menuid=8%26userDisplay=50%26search.boardtype=L%26search.specialmenutype=%26search.questionTab=A%26search.totalCount=501%26search.page=",
        "https://cafe.naver.com/lchfkorea?iframe_url=/ArticleList.nhn%3Fsearch.clubid=28737666%26search.menuid=1%26userDisplay=50%26search.boardtype=L%26search.specialmenutype=%26search.questionTab=A%26search.totalCount=501%26search.page=",
        "https://cafe.naver.com/lchfkorea?iframe_url=/ArticleList.nhn%3Fsearch.clubid=28737666%26search.menuid=1%26userDisplay=50%26search.boardtype=L%26search.specialmenutype=%26search.questionTab=A%26search.totalCount=501%26search.page=",
        "https://cafe.naver.com/ketogenic?iframe_url=/ArticleList.nhn%3Fsearch.clubid=25217948%26search.menuid=5%26userDisplay=50%26search.boardtype=L%26search.specialmenutype=%26search.questionTab=A%26search.totalCount=501%26search.page=",
        "https://cafe.naver.com/ketogenic?iframe_url=/ArticleList.nhn%3Fsearch.clubid=25217948%26search.menuid=118%26userDisplay=50%26search.boardtype=L%26search.specialmenutype=%26search.questionTab=A%26search.totalCount=501%26search.page=",
        "https://cafe.naver.com/ketogenic?iframe_url=/ArticleList.nhn%3Fsearch.clubid=25217948%26search.menuid=56%26userDisplay=50%26search.boardtype=L%26search.specialmenutype=%26search.questionTab=A%26search.totalCount=501%26search.page="]
#        "https://cafe.naver.com/ketogenic?iframe_url=/ArticleList.nhn%3Fsearch.clubid=25217948%26search.menuid=147%26userDisplay=50%26search.boardtype=L%26search.specialmenutype=%26search.questionTab=A%26search.totalCount=501%26search.page="]

pages = 151
filename = ["keto_free.csv", "keto_qna.csv", "keto_today.csv", "lchf_today.csv", "lchf_free.csv", "lchf_board.csv"]
#"keto_gongu.csv"

for j in range(len(urls)):
    url = urls[j]
    for i in range(1,pages):
#        print(url+str(i))
        driver.get(url+str(i))
        driver.switch_to_frame(driver.find_element_by_name("cafe_main"))
        web_data = driver.page_source
#       web_data = urllib.request.urlopen(url+str(i)).read()
        web_data_soup = BeautifulSoup(web_data, "html.parser")

        # ids = driver.find_element_by_xpath("//span/@id")
        scr_lst = web_data_soup.findAll("script", {
            "id":False,
            "type": "text/javascript",
        })

        for scr in scr_lst:
            if (scr.get_text()[0:9] == "wordBreak"):
                tmp = scr.get_text()[13:-1]
                if (tmp[0:2] != "top"):
                    user_id = ''.join(tmp.split('_')[1:-1])

                    if user_id not in users:
                       users.append(user_id)


    user_emails = [ x + y for x in users for y in email]

    f = open(filename[j],"w")

    f.write(',\n'.join(user_emails))

    f.close()
