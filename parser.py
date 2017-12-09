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
driver.find_element_by_name('id').send_keys('doctorkitchen')
driver.find_element_by_name('pw').send_keys('drkitchen1507')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

urls = ["https://cafe.naver.com/dangsamo?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10096425%26search.menuid=3%26userDisplay=50%26search.boardtype=L%26search.questionTab=A%26search.totalCount=501%26search.page=",
        "http://cafe.naver.com/ArticleList.nhn?search.clubid=14110564&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.questionTab=A&search.totalCount=501&search.page=",
        "http://cafe.naver.com/ArticleList.nhn?search.clubid=22552330&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.questionTab=A&search.totalCount=501&search.page=",
        "http://cafe.naver.com/ArticleList.nhn?search.clubid=11345493&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.questionTab=A&search.totalCount=501&search.page=",
        "http://cafe.naver.com/ArticleList.nhn?search.clubid=16192600&userDisplay=50&search.boardtype=L&search.specialmenutype=&search.questionTab=A&search.totalCount=501&search.page="]
pages = 3
filename = ["dangsamo.csv", "gungangnara.csv", "danggab.csv", "haneul.csv", "gungangmi.csv"]
#url = sys.argv[1]
#pages = int(sys.argv[2])

for j in range(1,5):
    url = urls[j]
    for i in range(1,pages):
        print(url+str(i))
        driver.get(url+str(i))
        driver.switch_to_frame(driver.find_element_by_name("cafe_main"))
        web_data = driver.page_source
#       web_data = urllib.request.urlopen(url+str(i)).read()
        web_data_soup = BeautifulSoup(web_data, "html.parser")
        # ids = driver.find_element_by_xpath("//span/@id")
        ids = web_data_soup.findAll("span", {
            "id":True,
            "class": "wordbreak",
        })

        for user in ids:
            user_id = ''.join(user['id'].split('_')[1:-1])

#           print(user_id)

            if user_id not in users:
                users.append(user_id)

        time.sleep(3)

    user_emails = [ x + y for x in users for y in email]

    f = open(filename[j],"w")
#sys.argv[3] = 'target.csv':: csv_filename
#f = open('treasure.csv',"w")

    f.write(',\n'.join(user_emails))

    f.close()
