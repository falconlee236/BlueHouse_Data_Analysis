# coding=utf-8
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# import pprint pprint.pprint(dict())하면 이쁘게 출력된다.

'''
ctr + k = commit
ctr + shift + k = push
'''

data = pd.read_excel("bluehouse.xlsx")
data_type = {"정치개혁": 0, "외교/통일/국방": 0, "일자리": 0, "미래": 0,
             "성장동력": 0, "농산어촌": 0, "보건복지": 0, "육아/교육": 0,
             "안전/환경": 0, "저출산/고령화대책": 0, "행정": 0, "반려동물": 0,
             "교통/건축/국토": 0, "경제민주화": 0, "인권/성평등": 0, "문화/예술/체육/언론": 0, "기타": 0}

for x in data["종류"]:  # data["종류"]와 data."종류"가 같다.
    data_type[x] += 1

'''
#WordCloud(fontpath == 폰트, bacground_color = 배경 색, colormap = 색깔 종류).generate(text) - > text만 출력,
.generate_from_frequencies(dict()) 빈도수만큼 크기가 변함
'''

wordcloud = WordCloud(font_path="스플래툰K[Ver.3.0].ttf", background_color='black',
                      colormap="Accent_r",
                      width=1500, height=1000).generate_from_frequencies(data_type)

plt.imshow(wordcloud)  # wordcloud 출력 >>  matplotlib.pyplot.imshow == 이미지 파일 출력하기
plt.axis('off')  # 축 삭제
plt.show()  ## matplot 출력



