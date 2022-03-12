#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install beautifulsoup4')


# In[2]:


get_ipython().system(' pip install requests')


# In[3]:


import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
positive=pd.read_csv('positivewords.txt',header=None)
positive.columns=['words']
negative=pd.read_csv('negativewords.txt',header=None)
negative.columns=['words']


# In[4]:


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


# # ARTICLE 1

# ## DATA EXTRACTION

# In[5]:


url = 'https://insights.blackcoffer.com/how-is-login-logout-time-tracking-for-employees-in-office-done-by-ai/'
page = requests.get(url, headers = headers)
file = open("1.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[6]:


file = open("1.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[7]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("1.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed1.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed1.txt' ")


# In[8]:


#Counting number of clean words

file = open("stopwords-removed1.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[9]:


file = open("stopwords-removed1.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[10]:


file = open("stopwords-removed1.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[11]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[12]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1799]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1800]:


#Counting number of sentences

file = open("stopwords-removed1.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1801]:


#Counting syllable length & Complex words

file = open("stopwords-removed1.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1802]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1803]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1804]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1805]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1806]:


file = open("stopwords-removed1.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1807]:


#Counting sum of number of characters in each word

file = open("stopwords-removed1.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1808]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 2

# ## DATA EXTRACTION

# In[1809]:


url = 'https://insights.blackcoffer.com/how-does-ai-help-to-monitor-retail-shelf-watches/'
page = requests.get(url, headers = headers)
file = open("2.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1810]:


file = open("2.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing stopwords from the text file

# In[1813]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("2.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed2.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed2.txt' ")


# In[1814]:


#Counting number of clean words

file = open("stopwords-removed2.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1815]:


file = open("stopwords-removed2.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1816]:


file = open("stopwords-removed2.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1817]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1820]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1821]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1822]:


#Counting number of sentences

file = open("stopwords-removed2.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1823]:


#Counting syllable length & Complex words

file = open("stopwords-removed2.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1825]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1826]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1827]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1828]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1829]:


file = open("stopwords-removed2.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1832]:


#Counting sum of number of characters in each word

file = open("stopwords-removed2.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1833]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 3

# ## DATA EXTRACTION

# In[1834]:


url = 'https://insights.blackcoffer.com/ai-and-its-impact-on-the-fashion-industry/'
page = requests.get(url, headers = headers)
file = open("3.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1835]:


file = open("3.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1836]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("3.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed3.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed3.txt' ")


# In[1837]:


#Counting number of clean words

file = open("stopwords-removed3.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1838]:


file = open("stopwords-removed3.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1839]:


file = open("stopwords-removed3.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1844]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1845]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1846]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1847]:


#Counting number of sentences

file = open("stopwords-removed3.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1848]:


#Counting syllable length & Complex words

file = open("stopwords-removed3.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1849]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1850]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1851]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1852]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1853]:


file = open("stopwords-removed3.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1856]:


#Counting sum of number of characters in each word

file = open("stopwords-removed3.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1857]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 4

# ## DATA EXTRACTION 

# In[1858]:


url = 'https://insights.blackcoffer.com/how-do-deep-learning-models-predict-old-and-new-drugs-that-are-successfully-treated-in-healthcare/'
page = requests.get(url, headers = headers)
file = open("4.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1859]:


file = open("4.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ## Removing Stopwords from the text file

# In[1860]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("4.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed4.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed4.txt' ")


# ### Counting number of clean words

# In[1861]:


file = open("stopwords-removed4.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1862]:


file = open("stopwords-removed4.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1863]:


file = open("stopwords-removed4.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[1864]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1865]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1866]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1867]:


#Counting number of sentences

file = open("stopwords-removed4.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1868]:


#Counting syllable length & Complex words

file = open("stopwords-removed4.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[1869]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1870]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1871]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1872]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1873]:


file = open("stopwords-removed4.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1874]:


#Counting sum of number of characters in each word

file = open("stopwords-removed4.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1875]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 5

# ## DATA EXTRACTION

# In[1876]:


url = 'https://insights.blackcoffer.com/how-artificial-intelligence-can-boost-your-productivity-level/'
page = requests.get(url, headers = headers)
file = open("5.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1877]:


file = open("5.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1878]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("5.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed5.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed5.txt' ")


# ### Counting number of clean words

# In[1879]:


file = open("stopwords-removed5.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1880]:


file = open("stopwords-removed5.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1881]:


file = open("stopwords-removed5.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[1882]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1883]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1884]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1885]:


#Counting number of sentences

file = open("stopwords-removed5.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1886]:


#Counting syllable length & Complex words

file = open("stopwords-removed5.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[1887]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1888]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1889]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1890]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1891]:


file = open("stopwords-removed5.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1892]:


#Counting sum of number of characters in each word

file = open("stopwords-removed5.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1893]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 6

# ## DATA EXTRACTION

# In[1894]:


url = 'https://insights.blackcoffer.com/how-are-genetic-sequencing-maps-affected-by-deep-learning-and-ai/'
page = requests.get(url, headers = headers)
file = open("6.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1895]:


file = open("6.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1896]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("6.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed6.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed6.txt' ")


# In[1897]:


#Counting number of clean words

file = open("stopwords-removed6.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1898]:


file = open("stopwords-removed6.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1899]:


file = open("stopwords-removed6.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[1900]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1901]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1902]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1903]:


#Counting number of sentences

file = open("stopwords-removed6.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1904]:


#Counting syllable length & Complex words

file = open("stopwords-removed6.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[1905]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1906]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1907]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1908]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1909]:


file = open("stopwords-removed6.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1910]:


#Counting sum of number of characters in each word

file = open("stopwords-removed3.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1911]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 7

# ## DATA EXTRACTION 

# In[1912]:


url = 'https://insights.blackcoffer.com/how-is-ai-used-to-solve-traffic-management/'
page = requests.get(url, headers = headers)
file = open("7.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1913]:


file = open("7.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1914]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("7.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed7.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed7.txt' ")


# In[1915]:


#Counting number of clean words

file = open("stopwords-removed7.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive and negative words

# In[1916]:


file = open("stopwords-removed7.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1917]:


file = open("stopwords-removed7.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[1918]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1919]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1920]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1921]:


#Counting number of sentences

file = open("stopwords-removed7.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1922]:


#Counting syllable length & Complex words

file = open("stopwords-removed7.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[1923]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1924]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1925]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1926]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1927]:


file = open("stopwords-removed7.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1928]:


#Counting sum of number of characters in each word

file = open("stopwords-removed7.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1929]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 8

# ## DATA EXTRACTION

# In[1930]:


url = 'https://insights.blackcoffer.com/benefits-of-big-data-in-different-fields/'
page = requests.get(url, headers = headers)
file = open("8.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1931]:


file = open("8.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1932]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("8.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed8.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed8.txt' ")


# In[1933]:


#Counting number of clean words

file = open("stopwords-removed8.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1934]:


file = open("stopwords-removed8.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1935]:


file = open("stopwords-removed8.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[1939]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1937]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1938]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1940]:


#Counting number of sentences

file = open("stopwords-removed8.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1941]:


#Counting syllable length & Complex words

file = open("stopwords-removed8.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[1942]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1943]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1944]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1945]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1946]:


file = open("stopwords-removed8.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1947]:


#Counting sum of number of characters in each word

file = open("stopwords-removed8.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1948]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 9

# ## DATA EXTRACTION

# In[1949]:


url = 'https://insights.blackcoffer.com/how-big-data-will-impact-the-future-of-business/'
page = requests.get(url, headers = headers)
file = open("9.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1950]:


file = open("9.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1953]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("9.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed9.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed9.txt' ")


# In[1954]:


#Counting number of clean words

file = open("stopwords-removed9.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[567]:


file = open("stopwords-removed9.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[568]:


file = open("stopwords-removed9.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[569]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[570]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[571]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[572]:


#Counting number of sentences

file = open("stopwords-removed9.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[573]:


#Counting syllable length & Complex words

file = open("stopwords-removed9.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[574]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[575]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[576]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[577]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[578]:


file = open("stopwords-removed9.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[579]:


#Counting sum of number of characters in each word

file = open("stopwords-removed9.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[580]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 10

# ## DATA EXTRACTION

# In[583]:


url = 'https://insights.blackcoffer.com/how-will-ai-make-decisions-in-tomorrows-wars/'
page = requests.get(url, headers = headers)
file = open("10.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[584]:


file = open("10.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[585]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("10.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed10.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed10.txt' ")


# In[586]:


#Counting number of clean words

file = open("stopwords-removed10.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[587]:


file = open("stopwords-removed10.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[588]:


file = open("stopwords-removed10.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[589]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[590]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[591]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[592]:


#Counting number of sentences

file = open("stopwords-removed10.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[593]:


#Counting syllable length & Complex words

file = open("stopwords-removed10.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[594]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[595]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[596]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[597]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[598]:


file = open("stopwords-removed10.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[599]:


#Counting sum of number of characters in each word

file = open("stopwords-removed10.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[600]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 11

# ## DATA EXTRACTION

# In[607]:


url = 'https://insights.blackcoffer.com/which-one-is-better-ai-or-big-data/'
page = requests.get(url, headers = headers)
file = open("11.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[608]:


file = open("11.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ## Removing Stopwords from the text file

# In[610]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("11.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed11.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed11.txt' ")


# In[611]:


#Counting number of clean words

file = open("stopwords-removed11.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[613]:


file = open("stopwords-removed11.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[614]:


file = open("stopwords-removed11.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[616]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[617]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[618]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[619]:


#Counting number of sentences

file = open("stopwords-removed11.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[620]:


#Counting syllable length & Complex words

file = open("stopwords-removed11.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[621]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[622]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[623]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[624]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[625]:


file = open("stopwords-removed11.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[626]:


#Counting sum of number of characters in each word

file = open("stopwords-removed11.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[627]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 12

# ## DATA EXTRACTION

# In[630]:


url = 'https://insights.blackcoffer.com/how-robots-can-help-in-e-learning-platforms/'
page = requests.get(url, headers = headers)
file = open("12.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[631]:


file = open("12.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[632]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("12.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed12.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed12.txt' ")


# In[633]:


#Counting number of clean words

file = open("stopwords-removed12.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[634]:


file = open("stopwords-removed12.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[635]:


file = open("stopwords-removed12.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[636]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[637]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[638]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[639]:


#Counting number of sentences

file = open("stopwords-removed12.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[640]:


#Counting syllable length & Complex words

file = open("stopwords-removed12.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[641]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[642]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[643]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[644]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[645]:


file = open("stopwords-removed12.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[646]:


#Counting sum of number of characters in each word

file = open("stopwords-removed12.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[647]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 13

# ## DATA EXTRACTION

# In[650]:


url = 'https://insights.blackcoffer.com/how-does-big-data-help-in-finance-and-the-growth-of-large-firms/'
page = requests.get(url, headers = headers)
file = open("13.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[651]:


file = open("13.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[652]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("13.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed13.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed13.txt' ")


# In[653]:


#Counting number of clean words

file = open("stopwords-removed13.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[654]:


file = open("stopwords-removed13.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[655]:


file = open("stopwords-removed13.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[656]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[657]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[658]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[659]:


#Counting number of sentences

file = open("stopwords-removed13.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[660]:


#Counting syllable length & Complex words

file = open("stopwords-removed13.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[661]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[662]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[663]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[664]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[665]:


file = open("stopwords-removed13.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[666]:


#Counting sum of number of characters in each word

file = open("stopwords-removed13.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[667]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 14

# ## DATA EXTRACTION

# In[670]:


url = 'https://insights.blackcoffer.com/future-of-work-robot-ai-and-automation/'
page = requests.get(url, headers = headers)
file = open("14.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[671]:


file = open("14.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[672]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("14.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed14.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed14.txt' ")


# In[673]:


#Counting number of clean words

file = open("stopwords-removed14.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# In[ ]:


### List of positive & negative words


# In[674]:


file = open("stopwords-removed14.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[675]:


file = open("stopwords-removed14.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[676]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[677]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[678]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[679]:


#Counting number of sentences

file = open("stopwords-removed14.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[680]:


#Counting syllable length & Complex words

file = open("stopwords-removed14.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[681]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[682]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[683]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[684]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[685]:


file = open("stopwords-removed14.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[686]:


#Counting sum of number of characters in each word

file = open("stopwords-removed14.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[687]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 15

# ## DATA EXTRACTION

# In[691]:


url = 'https://insights.blackcoffer.com/how-ai-will-help-the-defense-power-of-a-country/'
page = requests.get(url, headers = headers)
file = open("15.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[692]:


file = open("15.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[693]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("15.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed15.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed15.txt' ")


# In[694]:


#Counting number of clean words

file = open("stopwords-removed15.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[695]:


file = open("stopwords-removed15.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[696]:


file = open("stopwords-removed15.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived variables

# In[697]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[698]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[699]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[700]:


#Counting number of sentences

file = open("stopwords-removed15.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[701]:


#Counting syllable length & Complex words

file = open("stopwords-removed15.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[702]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[703]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[704]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[705]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[706]:


file = open("stopwords-removed15.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[707]:


#Counting sum of number of characters in each word

file = open("stopwords-removed15.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[708]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 16

# ## DATA EXTRACTION

# In[711]:


url = 'https://insights.blackcoffer.com/future-of-ai-and-machine-roles-in-the-medical-sector/'
page = requests.get(url, headers = headers)
file = open("16.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[712]:


file = open("16.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[713]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("16.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed16.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed16.txt' ")


# In[714]:


#Counting number of clean words

file = open("stopwords-removed16.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[715]:


file = open("stopwords-removed16.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[716]:


file = open("stopwords-removed16.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[717]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[718]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[719]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[720]:


#Counting number of sentences

file = open("stopwords-removed16.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[721]:


#Counting syllable length & Complex words

file = open("stopwords-removed16.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[722]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[723]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[724]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[725]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[726]:


file = open("stopwords-removed16.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[727]:


#Counting sum of number of characters in each word

file = open("stopwords-removed16.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[728]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 17

# ## DATA EXTRACTION

# In[734]:


url = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'
page = requests.get(url, headers = headers)
file = open("17.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[735]:


file = open("17.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[736]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("17.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed17.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed17.txt' ")


# In[737]:


#Counting number of clean words

file = open("stopwords-removed17.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[738]:


file = open("stopwords-removed17.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[739]:


file = open("stopwords-removed17.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[740]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[741]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[742]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[743]:


#Counting number of sentences

file = open("stopwords-removed17.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[744]:


#Counting syllable length & Complex words

file = open("stopwords-removed17.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[745]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[746]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[747]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[748]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[749]:


file = open("stopwords-removed17.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[750]:


#Counting sum of number of characters in each word

file = open("stopwords-removed17.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[751]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 18

# ## DATA EXTRACTION

# In[755]:


url = 'https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/'
page = requests.get(url, headers = headers)
file = open("18.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[756]:


file = open("18.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[757]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("18.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed18.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed18.txt' ")


# In[758]:


#Counting number of clean words

file = open("stopwords-removed18.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[759]:


file = open("stopwords-removed18.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[760]:


file = open("stopwords-removed18.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[761]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[762]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[763]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[764]:


#Counting number of sentences

file = open("stopwords-removed18.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[765]:


#Counting syllable length & Complex words

file = open("stopwords-removed18.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of readability

# In[766]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[767]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[768]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[769]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[770]:


file = open("stopwords-removed18.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[771]:


#Counting sum of number of characters in each word

file = open("stopwords-removed18.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[772]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 19

# ## DATA EXTRACTION

# In[776]:


url = 'https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/'
page = requests.get(url, headers = headers)
file = open("19.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[777]:


file = open("19.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[778]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("19.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed19.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed19.txt' ")


# In[779]:


#Counting number of clean words

file = open("stopwords-removed19.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[780]:


file = open("stopwords-removed19.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[781]:


file = open("stopwords-removed19.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[782]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[783]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[784]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[785]:


#Counting number of sentences

file = open("stopwords-removed19.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[786]:


#Counting syllable length & Complex words

file = open("stopwords-removed19.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[787]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[788]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[789]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[790]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[791]:


file = open("stopwords-removed19.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[792]:


#Counting sum of number of characters in each word

file = open("stopwords-removed19.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[793]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 20

# ## DATA EXTRACTION

# In[13]:


url = 'https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/'
page = requests.get(url, headers = headers)
file = open("20.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[14]:


file = open("20.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[15]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("20.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed20.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed20.txt' ")


# In[16]:


#Counting number of clean words

file = open("stopwords-removed20.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[17]:


file = open("stopwords-removed20.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[18]:


file = open("stopwords-removed20.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[19]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[20]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[21]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[22]:


#Counting number of sentences

file = open("stopwords-removed20.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[23]:


#Counting syllable length & Complex words

file = open("stopwords-removed20.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[24]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[25]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[26]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[27]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[28]:


file = open("stopwords-removed20.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[29]:


#Counting sum of number of characters in each word

file = open("stopwords-removed20.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[30]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 21

# ## DATA EXTRACTION

# In[817]:


url = 'https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/'
page = requests.get(url, headers = headers)
file = open("21.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[818]:


file = open("21.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing stopwords from the text file

# In[819]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("21.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed21.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed21.txt' ")


# In[820]:


#Counting number of clean words

file = open("stopwords-removed21.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[821]:


file = open("stopwords-removed21.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[822]:


file = open("stopwords-removed21.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[823]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[824]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[825]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[826]:


#Counting number of sentences

file = open("stopwords-removed3.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[827]:


#Counting syllable length & Complex words

file = open("stopwords-removed21.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[828]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[829]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[830]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[831]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[832]:


file = open("stopwords-removed21.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[833]:


#Counting sum of number of characters in each word

file = open("stopwords-removed21.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[834]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 22

# ## DATA EXTRACTION

# In[838]:


url = 'https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/'
page = requests.get(url, headers = headers)
file = open("22.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[839]:


file = open("22.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[840]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("22.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed22.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed22.txt' ")


# In[841]:


#Counting number of clean words

file = open("stopwords-removed22.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[842]:


file = open("stopwords-removed22.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[843]:


file = open("stopwords-removed22.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[844]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[845]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[846]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[847]:


#Counting number of sentences

file = open("stopwords-removed22.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[848]:


#Counting syllable length & Complex words

file = open("stopwords-removed22.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[849]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[850]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[851]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[852]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[853]:


file = open("stopwords-removed22.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[854]:


#Counting sum of number of characters in each word

file = open("stopwords-removed22.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[855]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 23

# ## DATA EXTRACTION

# In[31]:


url = 'https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/'
page = requests.get(url, headers = headers)
file = open("23.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[32]:


file = open("23.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[33]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("23.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed23.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed23.txt' ")


# In[34]:


#Counting number of clean words

file = open("stopwords-removed23.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[35]:


file = open("stopwords-removed23.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[36]:


file = open("stopwords-removed23.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[37]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[38]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[39]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[40]:


#Counting number of sentences

file = open("stopwords-removed23.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[41]:


#Counting syllable length & Complex words

file = open("stopwords-removed23.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[42]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[43]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[44]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[45]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[46]:


file = open("stopwords-removed23.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[47]:


#Counting sum of number of characters in each word

file = open("stopwords-removed23.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[48]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 24

# ## DATA EXTRACTION

# In[877]:


url = 'https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/'
page = requests.get(url, headers = headers)
file = open("24.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[878]:


file = open("24.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### REMOVING STOPWORDS FROM TEXT FILE

# In[879]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("24.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed24.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed24.txt' ")


# In[49]:


#Counting number of clean words

file = open("stopwords-removed24.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[880]:


file = open("stopwords-removed24.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[881]:


file = open("stopwords-removed24.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[882]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[883]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[884]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[885]:


#Counting number of sentences

file = open("stopwords-removed24.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[887]:


#Counting syllable length & Complex words

file = open("stopwords-removed24.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[888]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[889]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[890]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[891]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[892]:


file = open("stopwords-removed24.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[893]:


#Counting sum of number of characters in each word

file = open("stopwords-removed24.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[894]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 25

# ## DATA EXTRACTION

# In[50]:


url = 'https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/'
page = requests.get(url, headers = headers)
file = open("25.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[51]:


file = open("25.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from text file

# In[52]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("25.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed25.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed25.txt' ")


# In[53]:


#Counting number of clean words

file = open("stopwords-removed25.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[54]:


file = open("stopwords-removed25.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[55]:


file = open("stopwords-removed25.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived Variables

# In[56]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[57]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[58]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[59]:


#Counting number of sentences

file = open("stopwords-removed25.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[60]:


#Counting syllable length & Complex words

file = open("stopwords-removed25.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[61]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[62]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[63]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[64]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[65]:


file = open("stopwords-removed25.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[66]:


#Counting sum of number of characters in each word

file = open("stopwords-removed25.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[67]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 26

# ## DATA EXTRACTION

# In[68]:


url = 'https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/'
page = requests.get(url, headers = headers)
file = open("26.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[69]:


file = open("26.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[70]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("26.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed26.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed26.txt' ")


# In[71]:


#Counting number of clean words

file = open("stopwords-removed26.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[72]:


file = open("stopwords-removed26.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[73]:


file = open("stopwords-removeD26.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[74]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[75]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[76]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[77]:


#Counting number of sentences

file = open("stopwords-removed26.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[78]:


#Counting syllable length & Complex words

file = open("stopwords-removed26.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[79]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[80]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[81]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[82]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[83]:


file = open("stopwords-removed26.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[84]:


#Counting sum of number of characters in each word

file = open("stopwords-removed26.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[85]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 27

# ## DATA EXTRACTION

# In[86]:


url = 'https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/'
page = requests.get(url, headers = headers)
file = open("27.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[87]:


file = open("27.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[88]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("27.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed27.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed27.txt' ")


# In[89]:


#Counting number of clean words

file = open("stopwords-removed27.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[90]:


file = open("stopwords-removed3.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[91]:


file = open("stopwords-removed3.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[92]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[93]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[94]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[95]:


#Counting number of sentences

file = open("stopwords-removed3.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[96]:


#Counting syllable length & Complex words

file = open("stopwords-removed27.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[97]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[98]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[99]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[100]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[101]:


file = open("stopwords-removed27.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[102]:


#Counting sum of number of characters in each word

file = open("stopwords-removed27.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[103]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 28

# ## DATA EXTRACTION

# In[104]:


url = 'https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/'
page = requests.get(url, headers = headers)
file = open("28.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[105]:


file = open("28.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[106]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("28.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed28.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed28.txt' ")


# In[107]:


#Counting number of clean words

file = open("stopwords-removed28.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# In[108]:


### List of positive & negative words

file = open("stopwords-removed28.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[109]:


file = open("stopwords-removed28.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[110]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[111]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[112]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[113]:


#Counting number of sentences

file = open("stopwords-removed28.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[114]:


#Counting syllable length & Complex words

file = open("stopwords-removed28.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[115]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[116]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[117]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[118]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[119]:


file = open("stopwords-removed28.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[120]:


#Counting sum of number of characters in each word

file = open("stopwords-removed28.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[121]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 29

# ## DATA EXTRACTION

# In[122]:


url = 'https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/'
page = requests.get(url, headers = headers)
file = open("29.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[974]:


file = open("29.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[975]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("29.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed29.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed29.txt' ")


# In[976]:


#Counting number of clean words

file = open("stopwords-removed29.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[977]:


file = open("stopwords-removed29.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[978]:


file = open("stopwords-removed29.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting derived Variables

# In[979]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[980]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[981]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[982]:


#Counting number of sentences

file = open("stopwords-removed29.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[983]:


#Counting syllable length & Complex words

file = open("stopwords-removed29.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[984]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[985]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[986]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[987]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[988]:


file = open("stopwords-removed29.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[989]:


#Counting sum of number of characters in each word

file = open("stopwords-removed29.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[990]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 30

# ## DATA EXTRACTION

# In[123]:


url = 'https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/'
page = requests.get(url, headers = headers)
file = open("30.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[124]:


file = open("30.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[125]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("30.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed30.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed30.txt' ")


# In[126]:


#Counting number of clean words

file = open("stopwords-removed30.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[127]:


file = open("stopwords-removed30.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[128]:


file = open("stopwords-removed30.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[129]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[130]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[131]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[132]:


#Counting number of sentences

file = open("stopwords-removed30.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[133]:


#Counting syllable length & Complex words

file = open("stopwords-removed30.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[134]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[135]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[136]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[137]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[138]:


file = open("stopwords-removed30.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[139]:


#Counting sum of number of characters in each word

file = open("stopwords-removed30.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[140]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 31

# ## DATA EXTRACTION

# In[1016]:


url = 'https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/'
page = requests.get(url, headers = headers)
file = open("31.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1017]:


file = open("31.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1018]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("31.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed31.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed31.txt' ")


# In[1020]:


#Counting number of clean words

file = open("stopwords-removed31.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1021]:


file = open("stopwords-removed31.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1022]:


file = open("stopwords-removed31.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1023]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1024]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1025]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1026]:


#Counting number of sentences

file = open("stopwords-removed31.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1027]:


#Counting syllable length & Complex words

file = open("stopwords-removed31.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1028]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1029]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1030]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1031]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1032]:


file = open("stopwords-removed31.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1033]:


#Counting sum of number of characters in each word

file = open("stopwords-removed31.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1034]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 32

# ## DATA EXTRACTION

# In[1037]:


url = 'https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/'
page = requests.get(url, headers = headers)
file = open("32.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1038]:


file = open("32.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1039]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("32.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed32.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed32.txt' ")


# In[1040]:


#Counting number of clean words

file = open("stopwords-removed32.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1041]:


file = open("stopwords-removed32.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1042]:


file = open("stopwords-removed32.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1043]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1044]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1045]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1046]:


#Counting number of sentences

file = open("stopwords-removed32.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1047]:


#Counting syllable length & Complex words

file = open("stopwords-removed32.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1048]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1049]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1050]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1051]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1052]:


file = open("stopwords-removed32.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1053]:


#Counting sum of number of characters in each word

file = open("stopwords-removed32.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1054]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 33

# ## DATA EXTRACTION

# In[1058]:


url = 'https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/'
page = requests.get(url, headers = headers)
file = open("33.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1059]:


file = open("33.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1060]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("33.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed33.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed33.txt' ")


# In[1061]:


#Counting number of clean words

file = open("stopwords-removed33.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1062]:


file = open("stopwords-removed33.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1063]:


file = open("stopwords-removed33.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1064]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1065]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1066]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1067]:


#Counting number of sentences

file = open("stopwords-removed33.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1068]:


#Counting syllable length & Complex words

file = open("stopwords-removed33.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1069]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1070]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1071]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1072]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1073]:


file = open("stopwords-removed33.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1074]:


#Counting sum of number of characters in each word

file = open("stopwords-removed33.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1075]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 34

# ## DATA EXTRACTION

# In[1080]:


url = 'https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/'
page = requests.get(url, headers = headers)
file = open("34.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1081]:


file = open("34.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1082]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("34.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed34.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed34.txt' ")


# In[1083]:


#Counting number of clean words

file = open("stopwords-removed34.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1084]:


file = open("stopwords-removed34.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1086]:


file = open("stopwords-removed34.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1087]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1088]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1089]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1090]:


#Counting number of sentences

file = open("stopwords-removed34.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1091]:


#Counting syllable length & Complex words

file = open("stopwords-removed34.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1092]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1093]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1094]:


og_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1095]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1096]:


file = open("stopwords-removed34.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1097]:


#Counting sum of number of characters in each word

file = open("stopwords-removed34.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1098]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 35

# ## DATA EXTRACTION

# In[1103]:


url = 'https://insights.blackcoffer.com/evolution-of-advertising-industry/'
page = requests.get(url, headers = headers)
file = open("35.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1104]:


file = open("35.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1105]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("35.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed35.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed35.txt' ")


# In[1106]:


#Counting number of clean words

file = open("stopwords-removed35.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1107]:


file = open("stopwords-removed35.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1108]:


file = open("stopwords-removed35.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1109]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1110]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1111]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1112]:


#Counting number of sentences

file = open("stopwords-removed35.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1113]:


#Counting syllable length & Complex words

file = open("stopwords-removed35.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1114]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1115]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1116]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1118]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1119]:


file = open("stopwords-removed35.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1120]:


#Counting sum of number of characters in each word

file = open("stopwords-removed35.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1121]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 36

# ## DATA EXTRACTION

# In[1124]:


url = 'https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/'
page = requests.get(url, headers = headers)
file = open("36.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1125]:


file = open("36.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1126]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("36.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed36.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed36.txt' ")


# In[1127]:


#Counting number of clean words

file = open("stopwords-removed36.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1128]:


file = open("stopwords-removed36.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1129]:


file = open("stopwords-removed36.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1130]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1131]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1132]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1133]:


#Counting number of sentences

file = open("stopwords-removed36.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1134]:


#Counting syllable length & Complex words

file = open("stopwords-removed36.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1135]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1136]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1137]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1138]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1139]:


file = open("stopwords-removed36.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1140]:


#Counting sum of number of characters in each word

file = open("stopwords-removed36.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1141]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 37

# ## DATA EXTRACTION

# In[1145]:


url = 'https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/'
page = requests.get(url, headers = headers)
file = open("37.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1146]:


file = open("37.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1147]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("37.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed37.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed37.txt' ")


# In[1148]:


#Counting number of clean words

file = open("stopwords-removed37.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1149]:


file = open("stopwords-removed37.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1150]:


file = open("stopwords-removed37.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1151]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1152]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1153]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1154]:


#Counting number of sentences

file = open("stopwords-removed37.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1155]:


#Counting syllable length & Complex words

file = open("stopwords-removed37.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1156]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1157]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1158]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1159]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1160]:


file = open("stopwords-removed37.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1161]:


#Counting sum of number of characters in each word

file = open("stopwords-removed37.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1162]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 38

# ## DATA EXTRACTION

# In[1186]:


url = 'https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/'
page = requests.get(url, headers = headers)
file = open("38.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1187]:


file = open("38.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1188]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("38.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed38.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed38.txt' ")


# In[1189]:


#Counting number of clean words

file = open("stopwords-removed38.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1190]:


file = open("stopwords-removed38.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1191]:


file = open("stopwords-removed38.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1192]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1193]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1194]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1195]:


#Counting number of sentences

file = open("stopwords-removed38.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1196]:


#Counting syllable length & Complex words

file = open("stopwords-removed38.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1197]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1198]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1199]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1200]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1201]:


file = open("stopwords-removed38.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1202]:


#Counting sum of number of characters in each word

file = open("stopwords-removed38.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1203]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 39

# ## DATA EXTRACTION

# In[1206]:


url = 'https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/'
page = requests.get(url, headers = headers)
file = open("39.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1207]:


file = open("39.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1208]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("39.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed39.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed39.txt' ")


# In[1209]:


#Counting number of clean words

file = open("stopwords-removed39.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1210]:


file = open("stopwords-removed39.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1211]:


file = open("stopwords-removed39.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1212]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1213]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1214]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1215]:


#Counting number of sentences

file = open("stopwords-removed39.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1216]:


#Counting syllable length & Complex words

file = open("stopwords-removed39.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1218]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1219]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1220]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1221]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1222]:


file = open("stopwords-removed39.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1223]:


#Counting sum of number of characters in each word

file = open("stopwords-removed39.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1224]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 40

# ## DATA EXTRACTION

# In[1227]:


url = 'https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/'
page = requests.get(url, headers = headers)
file = open("40.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1228]:


file = open("40.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1229]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("40.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed40.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed40.txt' ")


# In[1230]:


#Counting number of clean words

file = open("stopwords-removed40.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1231]:


file = open("stopwords-removed40.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1232]:


file = open("stopwords-removed40.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1233]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1234]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1235]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1236]:


#Counting number of sentences

file = open("stopwords-removed40.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1237]:


#Counting syllable length & Complex words

file = open("stopwords-removed40.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1238]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1239]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1240]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1241]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1242]:


file = open("stopwords-removed40.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1243]:


#Counting sum of number of characters in each word

file = open("stopwords-removed40.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1244]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 41

# ## DATA EXTRACTION

# In[1248]:


url = 'https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/'
page = requests.get(url, headers = headers)
file = open("41.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1249]:


file = open("41.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1250]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("41.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed41.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed41.txt' ")


# In[1251]:


#Counting number of clean words

file = open("stopwords-removed41.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1252]:


file = open("stopwords-removed41.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1253]:


file = open("stopwords-removed41.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1254]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1255]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1256]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1257]:


#Counting number of sentences

file = open("stopwords-removed41.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1258]:


#Counting syllable length & Complex words

file = open("stopwords-removed41.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1259]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1260]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1261]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1262]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1263]:


file = open("stopwords-removed41.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1264]:


#Counting sum of number of characters in each word

file = open("stopwords-removed41.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1265]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 42

# ## DATA EXTRACTION

# In[1268]:


url = 'https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/'
page = requests.get(url, headers = headers)
file = open("42.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1269]:


file = open("42.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1270]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("42.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed42.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed42.txt' ")


# In[1271]:


#Counting number of clean words

file = open("stopwords-removed42.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1272]:


file = open("stopwords-removed42.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1273]:


file = open("stopwords-removed42.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1274]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1275]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1276]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1277]:


#Counting number of sentences

file = open("stopwords-removed42.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1278]:


#Counting syllable length & Complex words

file = open("stopwords-removed42.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1279]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1280]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1281]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1282]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1283]:


file = open("stopwords-removed42.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1284]:


#Counting sum of number of characters in each word

file = open("stopwords-removed42.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1285]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 43

# ## DATA EXTRACTION

# In[1302]:


url = 'https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/'
page = requests.get(url, headers = headers)
file = open("43.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1303]:


file = open("43.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1304]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("43.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed43.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed43.txt' ")


# In[1305]:


#Counting number of clean words

file = open("stopwords-removed43.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1306]:


file = open("stopwords-removed43.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1307]:


file = open("stopwords-removed43.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1308]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1309]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1310]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1312]:


#Counting number of sentences

file = open("stopwords-removed43.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1313]:


#Counting syllable length & Complex words

file = open("stopwords-removed43.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1314]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1315]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1316]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1317]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# file = open("stopwords-removed43.txt", "r")
# line = file.read()
# word = line.split()
# pers_pronouns = 0
# for wo in word:
#     if wo in ("I","we","my","ours","us","We","My"):
#         pers_pronouns += 1
# print(pers_pronouns)

# In[141]:


file = open("stopwords-removed43.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[142]:


#Counting sum of number of characters in each word

file = open("stopwords-removed43.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[143]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 45

# ## DATA EXTRACTION

# In[1324]:


url = 'https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/'
page = requests.get(url, headers = headers)
file = open("45.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1325]:


file = open("45.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1326]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("45.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed45.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed45.txt' ")


# In[1327]:


#Counting number of clean words

file = open("stopwords-removed45.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1329]:


file = open("stopwords-removed45.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1330]:


file = open("stopwords-removed45.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# In[1331]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1332]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1333]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1334]:


#Counting number of sentences

file = open("stopwords-removed45.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1335]:


#Counting syllable length & Complex words

file = open("stopwords-removed45.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1336]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1337]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1338]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1339]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1340]:


file = open("stopwords-removed45.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1341]:


#Counting sum of number of characters in each word

file = open("stopwords-removed45.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1342]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 46

# ## DATA EXTRACTION

# In[1346]:


url = 'https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/'
page = requests.get(url, headers = headers)
file = open("46.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1347]:


file = open("46.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1348]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("46.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed46.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed46.txt' ")


# In[1349]:


#Counting number of clean words

file = open("stopwords-removed46.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1350]:


file = open("stopwords-removed46.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1351]:


file = open("stopwords-removed46.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1352]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1353]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1354]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1355]:


#Counting number of sentences

file = open("stopwords-removed46.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1356]:


#Counting syllable length & Complex words

file = open("stopwords-removed46.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1357]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1358]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1359]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1360]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1361]:


file = open("stopwords-removed46.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1362]:


#Counting sum of number of characters in each word

file = open("stopwords-removed46.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1363]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 47

# ## DATA EXTRACTION

# In[1366]:


url = 'https://insights.blackcoffer.com/how-we-forecast-future-technologies/'
page = requests.get(url, headers = headers)
file = open("47.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1367]:


file = open("47.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1368]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("47.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed47.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed47.txt' ")


# In[1369]:


#Counting number of clean words

file = open("stopwords-removed47.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1370]:


file = open("stopwords-removed47.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1371]:


file = open("stopwords-removed47.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1372]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1373]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1374]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1375]:


#Counting number of sentences

file = open("stopwords-removed47.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1376]:


#Counting syllable length & Complex words

file = open("stopwords-removed47.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1377]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1378]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1379]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1380]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1381]:


file = open("stopwords-removed47.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1382]:


#Counting sum of number of characters in each word

file = open("stopwords-removed47.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1383]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 48

# ## DATA EXTRACTION

# In[1386]:


url = 'https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/'
page = requests.get(url, headers = headers)
file = open("48.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1387]:


file = open("48.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1388]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("48.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed48.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed48.txt' ")


# In[1389]:


#Counting number of clean words

file = open("stopwords-removed48.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1390]:


file = open("stopwords-removed48.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1391]:


file = open("stopwords-removed48.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1392]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1393]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1394]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1395]:


#Counting number of sentences

file = open("stopwords-removed48.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1396]:


#Counting syllable length & Complex words

file = open("stopwords-removed48.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1397]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1398]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1399]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1400]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1401]:


file = open("stopwords-removed48.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1402]:


#Counting sum of number of characters in each word

file = open("stopwords-removed48.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1403]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 49

# ## DATA EXTRACTION

# In[1407]:


url = 'https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/'
page = requests.get(url, headers = headers)
file = open("49.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1408]:


file = open("49.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1409]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("49.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed49.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed49.txt' ")


# In[1410]:


#Counting number of clean words

file = open("stopwords-removed49.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1411]:


file = open("stopwords-removed49.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1412]:


file = open("stopwords-removed49.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1413]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1414]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1415]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1416]:


#Counting number of sentences

file = open("stopwords-removed49.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1417]:


#Counting syllable length & Complex words

file = open("stopwords-removed49.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1418]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1419]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1420]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1421]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1422]:


file = open("stopwords-removed49.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1423]:


#Counting sum of number of characters in each word

file = open("stopwords-removed49.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1424]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 50

# ## DATA EXTRACTION

# In[1428]:


url = 'https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/'
page = requests.get(url, headers = headers)
file = open("50.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1429]:


file = open("50.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1430]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("50.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed50.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed50.txt' ")


# In[1431]:


#Counting number of clean words

file = open("stopwords-removed50.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1435]:


file = open("stopwords-removed50.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1436]:


file = open("stopwords-removed50.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1437]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1438]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1439]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1440]:


#Counting number of sentences

file = open("stopwords-removed50.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1441]:


#Counting syllable length & Complex words

file = open("stopwords-removed50.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1442]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1443]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1444]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1445]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1446]:


file = open("stopwords-removed50.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1447]:


#Counting sum of number of characters in each word

file = open("stopwords-removed50.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1448]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 51

# ## DATA EXTRACTION

# In[1451]:


url = 'https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/'
page = requests.get(url, headers = headers)
file = open("51.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1452]:


file = open("51.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1453]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("51.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed51.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed51.txt' ")


# In[1454]:


#Counting number of clean words

file = open("stopwords-removed51.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1455]:


file = open("stopwords-removed51.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1456]:


file = open("stopwords-removed51.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1457]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1458]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1459]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1460]:


#Counting number of sentences

file = open("stopwords-removed51.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1461]:


#Counting syllable length & Complex words

file = open("stopwords-removed51.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1462]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1463]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1464]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1465]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1466]:


file = open("stopwords-removed51.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1467]:


#Counting sum of number of characters in each word

file = open("stopwords-removed51.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1468]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 52

# ## DATA EXTRACTION

# In[1471]:


url = 'https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/'
page = requests.get(url, headers = headers)
file = open("52.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1472]:


file = open("52.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1473]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("52.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed52.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed52.txt' ")


# In[1474]:


#Counting number of clean words

file = open("stopwords-removed52.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1476]:


file = open("stopwords-removed52.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1477]:


file = open("stopwords-removed52.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1478]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1479]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1480]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1481]:


#Counting number of sentences

file = open("stopwords-removed52.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1482]:


#Counting syllable length & Complex words

file = open("stopwords-removed52.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1483]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1484]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1485]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1486]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1487]:


file = open("stopwords-removed52.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1488]:


#Counting sum of number of characters in each word

file = open("stopwords-removed52.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1489]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 53

# ## DATA EXTRACTION

# In[1492]:


url = 'https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/'
page = requests.get(url, headers = headers)
file = open("53.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1493]:


file = open("53.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1494]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("53.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed53.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed53.txt' ")


# In[1495]:


#Counting number of clean words

file = open("stopwords-removed53.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1496]:


file = open("stopwords-removed53.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1497]:


file = open("stopwords-removed53.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1498]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1499]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1500]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1501]:


#Counting number of sentences

file = open("stopwords-removed53.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1502]:


#Counting syllable length & Complex words

file = open("stopwords-removed53.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1503]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1504]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1505]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1506]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1507]:


file = open("stopwords-removed53.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1508]:


#Counting sum of number of characters in each word

file = open("stopwords-removed53.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1509]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 54

# ## DATA EXTRACTION

# In[1512]:


url = 'https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/'
page = requests.get(url, headers = headers)
file = open("54.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1513]:


file = open("54.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1514]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("54.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed54.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed54.txt' ")


# In[1515]:


#Counting number of clean words

file = open("stopwords-removed54.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1516]:


file = open("stopwords-removed54.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1517]:


file = open("stopwords-removed54.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1518]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1519]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1520]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1521]:


#Counting number of sentences

file = open("stopwords-removed54.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1522]:


#Counting syllable length & Complex words

file = open("stopwords-removed54.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1523]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1524]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1525]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1526]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1527]:


file = open("stopwords-removed54.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1528]:


#Counting sum of number of characters in each word

file = open("stopwords-removed54.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1529]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 55

# ## DATA EXTRACTION

# In[1537]:


url = 'https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/'
page = requests.get(url, headers = headers)
file = open("55.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1538]:


file = open("55.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1539]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("55.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed55.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed55.txt' ")


# In[1540]:


#Counting number of clean words

file = open("stopwords-removed55.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1541]:


file = open("stopwords-removed55.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1542]:


file = open("stopwords-removed55.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1543]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1545]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1546]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1547]:


#Counting number of sentences

file = open("stopwords-removed55.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1548]:


#Counting syllable length & Complex words

file = open("stopwords-removed55.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1549]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1550]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1551]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1552]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1553]:


file = open("stopwords-removed55.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1554]:


#Counting sum of number of characters in each word

file = open("stopwords-removed55.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1555]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 56

# ## DATA EXTRACTION

# In[1558]:


url = 'https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/'
page = requests.get(url, headers = headers)
file = open("56.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1559]:


file = open("56.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1560]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("56.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed56.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed56.txt' ")


# In[1561]:


#Counting number of clean words

file = open("stopwords-removed56.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# In[1563]:


### List of positive & negative words


# In[1564]:


file = open("stopwords-removed56.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1565]:


file = open("stopwords-removed56.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1566]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1567]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1568]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1569]:


#Counting number of sentences

file = open("stopwords-removed56.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1570]:


#Counting syllable length & Complex words

file = open("stopwords-removed56.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1571]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1572]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1573]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1574]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1575]:


file = open("stopwords-removed56.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1576]:


#Counting sum of number of characters in each word

file = open("stopwords-removed56.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1577]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 57

# ## DATA EXTRACTION

# In[1580]:


url = 'https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/'
page = requests.get(url, headers = headers)
file = open("57.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1581]:


file = open("57.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1582]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("57.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed57.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed57.txt' ")


# In[1583]:


#Counting number of clean words

file = open("stopwords-removed57.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1584]:


file = open("stopwords-removed57.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1585]:


file = open("stopwords-removed57.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1586]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1587]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1588]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1589]:


#Counting number of sentences

file = open("stopwords-removed57.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1590]:


#Counting syllable length & Complex words

file = open("stopwords-removed57.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1591]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1592]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1593]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1594]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1595]:


file = open("stopwords-removed57.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1596]:


#Counting sum of number of characters in each word

file = open("stopwords-removed57.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1597]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 58

# ## DATA EXTRACTION

# In[1600]:


url = 'https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/'
page = requests.get(url, headers = headers)
file = open("58.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1601]:


file = open("58.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1602]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("58.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed58.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed58.txt' ")


# In[1603]:


#Counting number of clean words

file = open("stopwords-removed58.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1604]:


file = open("stopwords-removed58.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1605]:


file = open("stopwords-removed58.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1606]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1607]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1608]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1609]:


#Counting number of sentences

file = open("stopwords-removed58.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1610]:


#Counting syllable length & Complex words

file = open("stopwords-removed58.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1611]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1612]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1613]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1614]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1615]:


file = open("stopwords-removed58.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1616]:


#Counting sum of number of characters in each word

file = open("stopwords-removed58.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1617]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 59

# ## DATA EXTRACTION

# In[1620]:


url = 'https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/'
page = requests.get(url, headers = headers)
file = open("59.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1621]:


file = open("59.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1622]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("59.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed59.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed59.txt' ")


# In[1623]:


#Counting number of clean words

file = open("stopwords-removed59.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1624]:


file = open("stopwords-removed59.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1625]:


file = open("stopwords-removed59.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1626]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1627]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1628]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1629]:


#Counting number of sentences

file = open("stopwords-removed59.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1630]:


#Counting syllable length & Complex words

file = open("stopwords-removed59.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1631]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1632]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1633]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1634]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1635]:


file = open("stopwords-removed59.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1636]:


#Counting sum of number of characters in each word

file = open("stopwords-removed59.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1637]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 60

# ## DATA EXTRACTION

# In[1641]:


url = 'https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/'
page = requests.get(url, headers = headers)
file = open("60.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1642]:


file = open("60.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1643]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("60.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed60.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed60.txt' ")


# In[1644]:


#Counting number of clean words

file = open("stopwords-removed60.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1645]:


file = open("stopwords-removed60.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1646]:


file = open("stopwords-removed60.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1647]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1648]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1649]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1650]:


#Counting number of sentences

file = open("stopwords-removed60.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1651]:


#Counting syllable length & Complex words

file = open("stopwords-removed60.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1652]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1653]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1654]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1655]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1656]:


file = open("stopwords-removed60.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1657]:


#Counting sum of number of characters in each word

file = open("stopwords-removed60.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1658]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 61

# ## DATA EXTRACTION

# In[1662]:


url = 'https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/'
page = requests.get(url, headers = headers)
file = open("61.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1663]:


file = open("61.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1664]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("61.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed61.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed61.txt' ")


# In[1665]:


#Counting number of clean words

file = open("stopwords-removed61.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1666]:


file = open("stopwords-removed61.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1667]:


file = open("stopwords-removed61.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1668]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1669]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1670]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1671]:


#Counting number of sentences

file = open("stopwords-removed61.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1672]:


#Counting syllable length & Complex words

file = open("stopwords-removed61.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1673]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1674]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1675]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1676]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1677]:


file = open("stopwords-removed61.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1678]:


#Counting sum of number of characters in each word

file = open("stopwords-removed61.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1679]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 62

# ## DATA EXTRACTION

# In[1686]:


url = 'https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/'
page = requests.get(url, headers = headers)
file = open("62.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1687]:


file = open("62.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1688]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("62.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed62.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed62.txt' ")


# In[1689]:


#Counting number of clean words

file = open("stopwords-removed62.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1690]:


file = open("stopwords-removed62.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1691]:


file = open("stopwords-removed62.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1692]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1694]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1695]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1696]:


#Counting number of sentences

file = open("stopwords-removed62.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1697]:


#Counting syllable length & Complex words

file = open("stopwords-removed62.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1699]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1700]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1701]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1702]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1703]:


file = open("stopwords-removed62.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1704]:


#Counting sum of number of characters in each word

file = open("stopwords-removed62.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1705]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 63

# ## DATA EXTRACTION

# In[1709]:


url = 'https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/'
page = requests.get(url, headers = headers)
file = open("63.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1710]:


file = open("63.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1711]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("63.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed63.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed63.txt' ")


# In[1712]:


#Counting number of clean words

file = open("stopwords-removed63.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1713]:


file = open("stopwords-removed63.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1714]:


file = open("stopwords-removed63.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1715]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1716]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1717]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1718]:


#Counting number of sentences

file = open("stopwords-removed63.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1719]:


#Counting syllable length & Complex words

file = open("stopwords-removed63.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1720]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1721]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1722]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1723]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1724]:


file = open("stopwords-removed63.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1725]:


#Counting sum of number of characters in each word

file = open("stopwords-removed63.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1726]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)


# # ARTICLE 64

# ### DATA EXTRACTION

# In[1730]:


url = 'https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/'
page = requests.get(url, headers = headers)
file = open("64.txt", "r")
soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find('h1', {'class': "entry-title"}).get_text()
print(title)

content = soup2.find('div', {'class': "td-post-content"}).get_text()
print(content)


# In[1731]:


file = open("64.txt", "w")
print(title)
file.write(title)
print(content)
file.write(content)

file.flush()
file.close


# ## DATA ANALYSIS

# ### Removing Stopwords from the text file

# In[1732]:


import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
stemmer = PorterStemmer()
# Get nltk stopword list into a set.
stop_words = set(stopwords.words('english'))
 
# Open and read in a text file.
txt_file = open("64.txt")
txt_line = txt_file.read()
txt_words = txt_line.split()
 
# stopwords found counter.
sw_found = 0
 
# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in txt_words:
    if not check_word.lower() in stop_words:
        # Not found on stopword list, so append.
        appendFile = open('stopwords-removed64.txt','a')
        appendFile.write(" "+check_word)
        appendFile.close()
        print(check_word)
print("Saved as 'stopwords-removed64.txt' ")


# In[1733]:


#Counting number of clean words

file = open("stopwords-removed64.txt")
line = file.read()
words = line.split()
count = 0
for word in words:
    count = count+1
words_cleaned = count
print(words_cleaned)


# ### List of positive & negative words

# In[1734]:


file = open("stopwords-removed64.txt")
line = file.read()
words = line.split()
positive_words = []
for w in words:
    if w in list(positive['words']):
        print(w)
        positive_words.append(w)
        
file.close()


# In[1735]:


file = open("stopwords-removed64.txt")
line = file.read()
words = line.split()
negative_words = []
for w in words:
    if w in list(negative['words']):
        print(w)
        negative_words.append(w)
        
file.close()


# ### Extracting Derived Variables

# In[1736]:


pos_score = len(positive_words)
neg_score = len(negative_words)
print(pos_score)
print(neg_score)


# In[1737]:


polarity_score = (pos_score - neg_score)/ ((pos_score + neg_score) + 0.000001)
print(round(polarity_score,2))


# In[1738]:


subjectivity_score = (pos_score + neg_score)/ ((words_cleaned) + 0.000001)
print(subjectivity_score)


# In[1739]:


#Counting number of sentences

file = open("stopwords-removed64.txt", "r")
sentences = 0
for line in file:
    sentences += line.count('.') + line.count('!') + line.count('?')
print(sentences)

    
file.close()


# In[1740]:


#Counting syllable length & Complex words

file = open("stopwords-removed64.txt", "r")
line = file.read()
word = line.split()
complex_words = 0
vowels = 'aeiouy'

for wo in word:
    syllable_count = 0
    if wo[0] in vowels:
        syllable_count += 1
    for index in range(1, len(wo)):
        if wo[index] in vowels and wo[index-1] not in vowels:
            syllable_count+=1
    if wo.endswith('e'):
        syllable_count -= 1
    if wo.endswith('le') and len(wo) > 2 and wo[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
        
    if (syllable_count>2):
        print(wo)
        complex_words += 1
        print(syllable_count)
    
print(complex_words)


# ### Analysis of Readability

# In[1741]:


avg_sen_len = words_cleaned/sentences
print(avg_sen_len)


# In[1742]:


perc_complex_words = complex_words/words_cleaned
print(perc_complex_words)


# In[1743]:


fog_index = 0.4 * (avg_sen_len + perc_complex_words)
print(fog_index)


# In[1744]:


avg_words_per_sen = words_cleaned/sentences
print(avg_words_per_sen)


# In[1745]:


file = open("stopwords-removed64.txt", "r")
line = file.read()
word = line.split()
pers_pronouns = 0
for wo in word:
    if wo in ("I","we","my","ours","us","We","My"):
        pers_pronouns += 1
print(pers_pronouns)


# In[1746]:


#Counting sum of number of characters in each word

file = open("stopwords-removed64.txt", "r")
line = file.read()
word = line.split()
count_char = 0
for wo in word:
    characters = 0
    characters += len(wo)
    count_char += characters
    
print(count_char)


# In[1747]:


avg_word_len = count_char/words_cleaned
print(avg_word_len)

