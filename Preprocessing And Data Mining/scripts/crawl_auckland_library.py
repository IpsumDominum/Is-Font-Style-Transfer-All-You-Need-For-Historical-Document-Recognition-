from bs4 import BeautifulSoup
import requests 
import random
import os
 
headers = { 
	'authority': 'httpbin.org', 
	'cache-control': 'max-age=0', 
	'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 
	'sec-ch-ua-mobile': '?0', 
	'upgrade-insecure-requests': '1', 
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
	'sec-fetch-site': 'none', 
	'sec-fetch-mode': 'navigate', 
	'sec-fetch-user': '?1', 
	'sec-fetch-dest': 'document', 
	'accept-language': 'en-US,en;q=0.9', 
} 

images = [
    [6526,2],
    [14249,130],
    [10674,159],
    [5610,8],
    [6489,10],
    [14390,498],
    [6113,4],
    [13372,41],
    [5009,4],
    [5043,4],
    [5221,2],
]


directory = "https://kura.aucklandlibraries.govt.nz/digital/api/singleitem/image/manuscripts/"
def get_html(url):
    response = requests.get(url,headers=headers,allow_redirects=True)     
    return response
"""
for pair in images:
    code = pair[0]
    length = pair[1]
    for i in range(length):
        save_dir = os.path.join("crawled",str(code+i)+'.jpg')
        print(save_dir)
        if(os.path.isfile(save_dir)):
            continue
        else:
            response = get_html(directory + str(code+i)+ "/default.jpg")
            if(response.headers.get('content-type')=="image/jpeg"):
                open(save_dir, 'wb').write(response.content)
            else:
                print("nope")
"""
code = 100
for i in range(10000,20000):
    save_dir = os.path.join("crawled",str(code+i)+'.jpg')
    print(save_dir)
    if(os.path.isfile(save_dir)):
        continue
    else:
        response = get_html(directory + str(code+i)+ "/default.jpg")
        if(response.headers.get('content-type')=="image/jpeg"):
            open(save_dir, 'wb').write(response.content)
        else:
            print("nope")