from selenium import webdriver
import os
import urllib.request
from urllib.error import HTTPError, URLError 
from selenium.webdriver.firefox.options import Options        #comment this for chrome usage
#from selenium.webdriver.chrome.options import Options        #uncomment this for chrome usage

searchlist = ["Pyoderma", "paronychia", "furunculosis","bacterial skin"]                                   #input your search item here
for searchterm in searchlist:
    img_goal = 500                                             #number of images to be downloaded
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    opts=Options()
    opts.headless=True
    browser = webdriver.Firefox(options=opts)                 #use webdriver.Chrome() if using chrome 
    browser.get(url)               
    extensions_exclude = {"gif"}
    if not os.path.exists(searchterm):
        os.mkdir(searchterm)

    for _ in range(700):
        browser.execute_script("window.scrollBy(0,10000)")
        
    html = browser.page_source.split('["')
    imges = []
    for i in html:
        if i.startswith('http') and i.split('"')[0].split('.')[-1] not in extensions_exclude:
            imges.append(i.split('"')[0])

    img_downloaded=0
    idx=1
    for url in imges:
        try:
            file_name=searchterm+"_"+str(idx)+"."+url.split("/")[-1].split(".")[-1]
            urllib.request.urlretrieve(url,os.path.join(searchterm,file_name))
            img_downloaded += 1
            idx += 1
            if img_downloaded == img_goal:
                print(searchterm+" images downloaded")
                break
        except (URLError, HTTPError, OSError) as errors:
            continue

    if img_downloaded != img_goal:
        print(str(img_goal-img_downloaded)+" images of" +searchterm+ "not downloaded")
        browser.quit()