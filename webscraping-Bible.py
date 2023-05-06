import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

biblehub = 'https://biblehub.com/asv/john/1.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

# req = Request(biblehub, headers=headers)

# page = urlopen(biblehub).read()			

# soup = BeautifulSoup(page, 'html.parser')


# phrase = soup.findAll("p",class_='reg')
# # print(len(phrase))
# # input()
# # for p in phrase:
# #     print(p.text)

# phrase_list = [p.text.split('.') for p in phrase]

# # # print(len(phrase_list))
# # print(phrase_list)

# print(random.choice(random.choice((phrase_list))))

chapters = list(range(1,22))

random_chapter = random.choice(chapters)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

edible = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

req = Request(edible, headers=headers)

page = urlopen(req).read()			

soup = BeautifulSoup(page, 'html.parser')

# print(soup.title.text)

page_verses = soup.findAll("div", class_='main')

for p in page_verses:
    verse_list = p.text.split(".")


myverse = verse_list[:-5]

mychoice = random.choice(myverse)

print(f'Chapter: {random_chapter}')
print(mychoice)

import keys
from twilio.rest import Client

client = Client(keys.accountSID,keys.auth_token)
TWnumber = "+13204088142"
myphone = "+15129130434"
textmsg = client.messages.create(to=myphone,from_=TWnumber,body=mychoice)
print(textmsg.status)