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

# url = sys.argv[1]
# pages = int(sys.argv[2])
url = "https://cafe.naver.com/ArticleList.nhn?search.clubid=10096425&search.menuid=3&userDisplay=50&search.boardtype=L&search.questionTab=A&search.totalCount=501&search.page="
pages = 2
for i in range(1,pages):
    print(url+str(i))
    driver.get(url+str(i))
    driver.switch_to_frame(driver.find_element_by_name("cafe_main"))
    web_data = driver.page_source
#    web_data = urllib.request.urlopen(url+str(i)).read()
    web_data_soup = BeautifulSoup(web_data, "html.parser")
    # ids = driver.find_element_by_xpath("//span/@id")
    ids = web_data_soup.findAll("span", {
        "id":True,
        "class": "wordbreak",
    })

    for user in ids:
        user_id = ''.join(user['id'].split('_')[1:-1])

        print(user_id)

        if user_id not in users:
            users.append(user_id)

    time.sleep(5)

# for i, user in enumerate(users):
#     u = ''.join(user.split('_')[1:-1])
#     users[i] = u;

user_emails = [ x + y for x in users for y in email]

#sys.argv[3] = 'target.csv':: csv_filename
# f = open('sys.argv[3]',"w")

f = open('treasure.csv',"w")

f.write(',\n'.join(user_emails))

f.close()
