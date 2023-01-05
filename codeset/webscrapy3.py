#!/usr/bin/env python
# coding: utf-8

# In[6]:


#!/usr/bin/env python
# coding: utf-8

# ### 웹 데이터 수집

# ### 1. requests, beautifulsoup 라이브러리

# In[1]:


# requests: 내가 웹에 데이터를 요청하는 라이브러리!
# bs4: 웹페이지의 데이터를 이쁘게 추출하는 라이브러리!
import requests, bs4
import pandas as pd
import datetime


targetUrl = "https://sparkkorea.com/%ed%80%b4%ec%a6%88/"

resp = requests.get(targetUrl)

# In[4]:


html = resp.text


# In[5]:


bsobj = bs4.BeautifulSoup(html,"html.parser")
bsobj

divScope =     bsobj.find(name="div", attrs={"class":"class_spark_quiz"})

atags = divScope.findAll(name="a")

titleList = []
linkList = []

for i in range(0, len(atags)):

    quizTitle = atags[i].text # 퀴즈 타이틀 정보 수집
    quizLink = atags[i].attrs["href"] # 퀴즈 링크 정보 수집
    titleList.append(quizTitle) # 빈리스트에 하나씩 저장
    linkList.append(quizLink) # 빈리스트에 하나씩 저장

quizInfoDf = pd.DataFrame( zip(titleList, linkList) , columns=["제목","링크"] )


# In[7]:


### revised by cjs
### 작업: 저장파일명 위에 시간정보 삽입


# In[15]:


# 현재날짜 가져오기
currentDate = datetime.datetime.now()

# 현재날짜 정보를 formatting 하기
timeTag = currentDate.strftime("%Y_%m_%d_%H_%M_%S_%Z")


# In[16]:


timeTag


# In[17]:


quizInfoDf.to_csv("../dataset/quizinfo{}.csv".format(timeTag), encoding="ms949")


# In[ ]:




