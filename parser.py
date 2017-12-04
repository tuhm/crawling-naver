#import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import sys

print("initializing")
email = ["@naver.com","@gmail.com","@hanmail.net","@daum.net","@hotmail.com","@nate.com"]
users = []

#login credential required
driver = webdriver.Chrome('/Users/tuhm/Documents/Dr_Kitchen/crawling/chromedriver')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('doctorkitchen')
driver.find_element_by_name('pw').send_keys('drkitchen1507')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

url = sys.argv[1]
#url = "http://cafe.naver.com/ArticleList.nhn?search.clubid=20353045&search.menuid=123&search.boardtype=L&search.questionTab=A&search.totalCount=151&search.page="
pages = int(sys.argv[2])
for i in range(1,pages):
    print(url+str(i))
    driver.get(url+str(i))
    web_data = driver.page_source
#    web_data = urllib.request.urlopen(url+str(i)).read()
    web_data_soup = BeautifulSoup(web_data, "html.parser")
    ids = web_data_soup.findAll("span",{"id":True})
    for user in ids:
        users.append(user['id'])

for i,user in enumerate(users):
    u = ''.join(user.split('_')[1:-1])
    users[i] = u;

user_emails = [ x + y for x in users for y in email]

f = open('target.csv',"w")
f.write(','.join(user_emails))
