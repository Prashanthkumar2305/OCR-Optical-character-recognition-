#!/usr/bin/env python

import pandas as pd
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import time


# In[3]:


df1=pd.read_csv(r"C:\\Users\\mmmm\\Desktop\\new\\photo_file.csv")


# In[4]:


df1['apmc_check']='No'


# In[5]:


df1


# In[7]:


df1['source_invoice_link']


# In[8]:


# df[df['apmc_check']=='Yes'].count()


# In[9]:


%%time
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import pytesseract
count=0
for url in df1['source_invoice_link']:
  try:
  response=requests.get(url)
  if response.status_code==200:
    image=Image.open(BytesIO(response.content))
    image.convert("L")
    text=pytesseract.image_to_string(image)
    count+=1
    print(count)
    if 'apmc yard' in text.lower() or 'apmc' in text.lower():
      df1.loc[df1['source_invoice_link']==url,'apmc_check']='Yes'
    else:
      df1.loc[df1['source_invoice_link'] == url, 'apmc_check']="No"
  else:
  print(f"We're getting error because of this {url} status_code is {response.status_code}")
  except Exception as e:
    print(f"error occuring {url}: {e}")')


# In[12]:


df1[df1['apmc_check']=='Yes']


# In[17]:


from IPython.display import FileLink


# In[18]:


df1.to_csv('png_format.csv',index=False)


# In[19]:


FileLink(r'png_format.csv')


# In[ ]:




