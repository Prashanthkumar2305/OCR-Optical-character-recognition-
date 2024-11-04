#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import pandas as pd
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import time
from concurrent.futures import ThreadPoolExecutor ,as_completed


# In[3]:


get_ipython().run_cell_magic('time', '', 'df1=pd.read_csv(r"C:\\Users\\mmmm\\Desktop\\new\\photo_file.csv")\n')


# In[4]:


df1['apmc_check']='No'


# In[5]:


df1


# In[7]:


df1['source_invoice_link']


# In[8]:


# df[df['apmc_check']=='Yes'].count()


# In[9]:


get_ipython().run_cell_magic('time', '', 'import pandas as pd\nimport requests\nfrom PIL import Image\nfrom io import BytesIO\nimport pytesseract\ncount=0\nfor url in df1[\'source_invoice_link\']:\n    try:\n        response=requests.get(url)\n        if response.status_code==200:\n            image=Image.open(BytesIO(response.content))\n            image.convert("L")\n            text=pytesseract.image_to_string(image)\n            count+=1\n            print(count)\n            \n            if \'apmc yard\' in text.lower() or \'apmc\' in text.lower():\n                df1.loc[df1[\'source_invoice_link\']==url,\'apmc_check\']=\'Yes\'\n            else:\n                df1.loc[df1[\'source_invoice_link\'] == url, \'apmc_check\']="No"\n        else:\n            print(f"We\'re getting error because of this {url} status_code is {response.status_code}")\n    except Exception as e:\n        print(f"error occuring {url}: {e}")\n')


# In[12]:


df1[df1['apmc_check']=='Yes']


# In[17]:


from IPython.display import FileLink


# In[18]:


df1.to_csv('png_format.csv',index=False)


# In[19]:


FileLink(r'png_format.csv')


# In[ ]:




