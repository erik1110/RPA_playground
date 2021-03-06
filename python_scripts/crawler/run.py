#!/usr/bin/python
# coding:utf-8
'''
github action crawler
'''
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class Crawler:
    '''
    爬蟲測試
    '''
    def __init__(self):
        #規避google bug
        chrome_options = Options() 
        chrome_options.add_argument('--headless')  #規避google bug
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-default-apps")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        self.driver.get('https://www.tpex.org.tw/web/bond/publish/search/latest.php?l=zh-tw')
        self.driver.maximize_window()

    def main(self):
        df = pd.DataFrame()
        tables = self.driver.find_elements_by_xpath('//*[@id="rpt_result"]/tbody/tr')
        for i, row in enumerate(tables):
            data_list = row.find_elements_by_xpath('.//td')
            df.loc[i, '債券代號'] = data_list[0].text
            df.loc[i, '債券名稱'] = data_list[1].text
            df.loc[i, '債券類別'] = data_list[2].text
            df.loc[i, '發行日期'] = data_list[3].text
        df.to_excel('./data/result.xlsx')
        print("爬蟲完成")


if __name__ == "__main__":
    pipeline = Crawler()
    pipeline.main()
