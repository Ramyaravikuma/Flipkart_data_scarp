import requests 
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook
wb = Workbook()
ws = wb.active
ws.title = "30page details"

ws.append(["rating","summary","review"])


for i in range(2,32):

    url="https://www.flipkart.com/oneplus-y1s-108-cm-43-inch-full-hd-led-smart-android-tv-11-bezel-less-frame/product-reviews/itm178846d2e1567?pid=TVSGAXEVSNT3HBQA&lid=LSTTVSGAXEVSNT3HBQAKRCYE0&marketplace=FLIPKART&page="+str(i)
    r=requests.get(url)
    # print(r)

    soup=BeautifulSoup(r.text,"lxml")
    np=soup.find("a",class_="_1LKTO3").get("href")
    cnp="https://www.flipkart.com"+np
    rows = soup.find_all('div',attrs={'class':'col _2wzgFH K0kLPL'})
    # print(f"Count of rows(reviews):{len(rows)}\n\n\n")
   
    for row in rows:
        
        sub_row = row.find_all('div',attrs={'class':'row'})
            
        rating = sub_row[0].find('div').text
        # print(f"rating:{rating} \n\n")
        
        summary = sub_row[0].find('p').text
        # print(f"summary:{summary} \n\n")
        
        review = sub_row[1].find_all('div')[2].text
        # print(f"review:{review} \n\n")
        
        ws.append([rating,summary,review])
    


wb.save(filename = 'Product Details.xlsx')
        