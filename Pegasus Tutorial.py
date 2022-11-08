#!/usr/bin/env python
# coding: utf-8

# # 0. Install dependencies

# In[1]:


# Install PyTorch
get_ipython().system('pip install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html')


# In[ ]:


# Install transformers
get_ipython().system('pip install transformers')


# # 1. Import and Load Model

# In[38]:


# Importing dependencies from transformers
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


# In[39]:


# Load tokenizer 
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")


# In[40]:


# Load model 
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")


# # 2. Perform Abstractive Summarization

# In[41]:


text = """
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[31]

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[32] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting. Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.[33]

Python consistently ranks as one of the most popular programming languages.[34][35][36][37]"""


# In[42]:


# Create tokens - number representation of our text
tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")


# In[44]:


# Input tokens
tokens


# In[45]:


# Summarize 
summary = model.generate(**tokens)


# In[47]:


# Output summary tokens
summary[0]


# In[48]:


# Decode summary
tokenizer.decode(summary[0])

