#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('python -c "import wget" || pip install -q "wget"')

from skimage import io
import wget

test_input_path = "input/d.jpg"


print(f"Test input file path: {test_input_path}")

test_image = io.imread(test_input_path)
io.imshow(test_image)


# In[5]:





# In[ ]:




