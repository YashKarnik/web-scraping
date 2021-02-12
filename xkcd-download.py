#!/usr/bin/env python
# coding: utf-8

# ## Importing Essential Libraries

# In[16]:


import urllib
import bs4
import requests


# ## Get comic source and title 

# In[18]:


comics=[]
c=1
for i in range(1,10):
    source=requests.get('https://xkcd.com/{}/'.format(i)).text
    soup=bs4.BeautifulSoup(source,'html.parser')
    print(str(100*c/10)+'%')
    c+=1
    comic=soup.find('div',{'id':'comic'}).find('img')
    title=comic['title']
    src='https://'+comic['src'][2:]
    comics.append({'title':title,'src':src})


# ## Create essential directories

# In[19]:


import os
try:
    os.mkdir('./Comics')
    os.mkdir('./Comics/XKCD')
    os.mkdir('./Comics/XKCD/PDFS')
except Exception as e:
    pass


# 
# ## Save comics as .jpg file

# In[20]:


destination_folder='./Comics/XKCD'
c=1
for i in comics:
    print(str(100*c/len(comics))+'%')
    c+=1
    path=destination_folder+i['title']+'.jpg'
    urllib.request.urlretrieve(i['src'],path)


# ## (Optional) Save Downloaded comics as pdfs

# In[21]:


import img2pdf
import glob


# In[22]:


downloaded=glob.glob('./Comics/XKCD*.jpg')


# In[23]:


for i in downloaded:
    filename='./Comics/XKCD/PDFS/'+i.split('\\')[-1][:-5]
    with open(filename+".pdf","wb") as f:
        f.write(img2pdf.convert(i))

