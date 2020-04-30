#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from splinter import Browser
import os 
from bs4 import BeautifulSoup as bs


# In[3]:


# The purpose of thsi notebook is to complete all scareping and analysis


# In[4]:


# Scrap teh NASA Mars news site. Collect lattest news titles and Prapraphs


# In[5]:


filepath = os.path.join("Nasa.html")
with open(filepath, encoding='utf-8') as file:
    html = file.read()


# In[7]:


soup = bs(html, 'html.parser')


# In[12]:


news_title = soup.title.text
print(news_title)


# In[13]:


news_p = soup.find_all('p')
for paragraph in news_p:
    print(paragraph.text)


# In[14]:


# Use splinter to navigate the site and find the image url for the current Featured Mars
# Image and assign the url string to a variable

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

html = browser.html

image = soup.find('span', class_='text')

browser.click_link_by_partial_text('Next')


# In[15]:


# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 
# Save the tweet text for the weather report as a variable called mars_weather.

url_twitter = 'https://twitter.com/MarsWxReport/status/1255842151205941250'
mars_weather = soup.find(class="css-901oao r-jwli3a r-1qd0xha r-1blvdjr r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0">).text


# In[16]:


# Visit the Mars Facts webpage here and use Pandas to scrape the table containing 
# facts about the planet including Diameter, Mass, etc.

url_mars_facts = 'https://space-facts.com/mars/'
tables = pd.read_html(url_mars_facts)
tables


# In[17]:


df = tables[0]
df.columns = ['Fact','Units']

df.head()


# In[18]:


# Use Pandas to convert the data to a HTML table string.
html_table = df.to_html()
html_table.replace('\n', '')


# In[ ]:


# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

