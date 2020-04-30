from selenium import webdriver as wd
from bs4 import BeautifulSoup
import pandas as pd
import os

page_num = 1
number = list()
category = list()
content = list()
date = list()
agree = list()


while page_num < 148:
    driver = wd.Chrome(executable_path="chromedriver.exe")
    url = "https://www1.president.go.kr/petitions/?c=0&only=1&page=" + str(page_num) + "&order=1"
    driver.get(url)
    html_source = driver.page_source
    page_num += 1
    driver.close()

    soup = BeautifulSoup(html_source, "lxml")
    numbers = soup.select("ul.petition_list > li > div.bl_wrap > div.bl_no")
    categorys = soup.select("ul.petition_list > li > div.bl_wrap > div.bl_category.ccategory.cs.wv_category")
    contents = soup.select("ul.petition_list > li > div.bl_wrap > div.bl_subject")
    dates = soup.select("ul.petition_list > li > div.bl_wrap > div.bl_date.light")
    agrees = soup.select("ul.petition_list > li > div.bl_wrap > div.bl_agree.cs")

    for x in range(len(numbers)):
        number.append(numbers[x].get_text().split(sep=' ', maxsplit=1)[1])
        category.append(categorys[x].get_text().split(sep=' ', maxsplit=1)[1])
        content.append(contents[x].get_text().split(sep=' ', maxsplit=1)[1])
        date.append(dates[x].get_text().split(sep=' ', maxsplit=2)[2])
        agree.append(agrees[x].get_text().split(sep=' ', maxsplit=1)[1])

bluehouse_problem = pd.DataFrame({
    '번호': number,
    '종류': category,
    '내용': content,
    '날짜': date,
    '추천수': agree
})

if os.path.isfile("bluehouse.xlsx") is True:
    file_name = "bluehouse"
    flag = False
    for x in range(1, 10):
        if os.path.isfile(file_name + str(x) + ".xlsx"):
            idx = x + 1
            flag = True
            break
    if flag:
        bluehouse_problem.to_excel(file_name + str(idx) + ".xlsx", index=False)
    else:
        bluehouse_problem.to_excel(file_name + "1.xlsx", index=False)

else:
    bluehouse_problem.to_excel("bluehouse.xlsx", index=False)



