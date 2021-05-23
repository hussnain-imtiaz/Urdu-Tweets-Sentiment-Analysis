import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge, EdgeOptions
from termcolor import colored
import pandas as pd


def scrap_tweets(post):
        try:
            username=post.find_element_by_xpath(".//span").text
            text=post.find_element_by_xpath(".//div[2]/div[2]/div[2]").text
            if len(text)!=0:
                print("𝗙𝗥𝗢𝗠 𝗧𝗪𝗜𝗧𝗧𝗘𝗥.......\n")
                print(f"{username}:")
                print(f"{text}\n")
            
        #rofile=post.find_element_by_xpath(".//div[1][@a='href']").text
        except NoSuchElementException:
            return
        
        tweet=(username,text)
        return tweet
def scrape(secure=False):
    
    options=EdgeOptions()
    options.use_chromium=True
    driver=Edge(options=options)

    query=input("▁ ▂ ▄ ▅ ▆ ▇ █ 𝐄𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐓𝐞𝐱𝐭 𝐭𝐨 𝐬𝐞𝐚𝐫𝐜𝐡 █ ▇ ▆ ▅ ▄ ▂ ▁\n\n ")
    
    print("\n𝘚𝘵𝘢𝘳𝘵𝘦𝘥 𝘚𝘤𝘳𝘢𝘱𝘪𝘯𝘨 ↦↦↦↦↦↦↦↦↦↦")
    print("\nPlease Wait ............\n")
    
    driver.get("https://www.twitter.com/login")
    driver.maximize_window()

    username=driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
    username.send_keys("studyp608@gmail.com")
    #password=getpass()

    userpas=driver.find_element_by_xpath('//input[@name="session[password]"]')
    userpas.send_keys('-----')
    userpas.send_keys(Keys.RETURN)
    sleep(2)
    
    if secure:
        username=driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
        username.send_keys("031-----")

        userpas=driver.find_element_by_xpath('//input[@name="session[password]"]')
        userpas.send_keys('----')
        userpas.send_keys(Keys.RETURN)
        sleep(2)



    search=driver.find_element_by_xpath('//input[@aria-label="Search query"]')
    search.send_keys('"پاک فوج" lang:ur -filter:links filter:replies')
    search.send_keys(Keys.RETURN)
    sleep(1.5)
    driver.find_element_by_link_text("Latest").click()
    data=[]
    tweet_ids=set()
    last_position=driver.execute_script("return window.pageYOffset;")
    scrolling=True

    while scrolling:
        posts=driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        for post in posts[-15:]:
            tweet=scrap_tweets(post)
            if tweet:
                tweet_id="".join(tweet)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    data.append(tweet)
                
        scroll_attempt=0
        while True:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            sleep(1)
        
            curr_position=driver.execute_script("return window.pageYOffset;")
            if last_position==curr_position:
                scroll_attempt += 1
            
                if scroll_attempt >= 3:
                    scrolling=False
                    break
                
                else:
                    sleep(2)
            else:
                last_position=curr_position
                break
    return data

def data_to_df(data):
    with open("Data/demo_tweets.csv", "w", newline="", encoding="utf-8") as f:
        header=["user_name","tweets"]
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    df=pd.read_csv("Data/demo_tweets.csv")
    df.dropna(inplace=True)
    df.reset_index(drop=True,inplace=True)
    return df
