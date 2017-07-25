import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc="
loc = "New+York,+NY"
page = 20
current_page = 0

while current_page < 201:
    url = base_url + loc + "&start=" + str(current_page)
    yulp_r = requests.get(url)
    yulp_soup = BeautifulSoup(yulp_r.text, 'html.parser')
    file_path = "yelp-{loc}-2.txt".format(loc=loc)

    with open(file_path, "a") as textfile:
        businesses = yulp_soup.findAll('div', {'class': 'biz-listing-large'})
        for biz in businesses:
            title = biz.findAll('a', {'class': 'biz-name'})[0].text
            websiteLink = "https://www.yelp.com" + biz.findAll('a')[0]['href']
            print(title)
            print(websiteLink)
            website = ""
            bizPage = requests.get(websiteLink)
            bizPage = BeautifulSoup(bizPage.text, 'html.parser')
            bizDetail = bizPage.findAll('div', {'class': 'mapbox-text'})
            if len(bizDetail) > 0:
                websiteBlock = bizDetail[0].findAll('span', {'class': 'biz-website'})
                if len(websiteBlock) > 0:
                    website = "https://www." + websiteBlock[0].findAll('a')[0].getText()
                else:
                    website = None
            else:
                website = None
            # website = bizDetail.findAll('span', {'class': 'biz-website'})
            # print(website)
            second_line = ""
            first_line = ""
            try:
                address = biz.findAll('address')[0].contents
                for item in address:
                    if "br" in str(item):
                        # print(item.getText())
                        second_line += item.getText().strip(' \n\t\r')

                    else:
                        # print(item.strip(' \n\t\r'))
                        first_line += item.strip(' \n\t\r')
                print(first_line)

            except:
                address = None
            try:
                phone = biz.findAll('span', {'class': 'biz-phone'})[0].getText().strip(' \n\t\r')
                print(second_line, phone)
            except:
                phone = None
            print("\n")
            page_line = "{title}\n{address1}\n{address2}{phone}\nwebsite: {website}\n\n".format(
                title=title,
                address1=first_line,
                address2=second_line,
                phone=phone,
                website=website
            )
            textfile.write(page_line)
    current_page += 10
