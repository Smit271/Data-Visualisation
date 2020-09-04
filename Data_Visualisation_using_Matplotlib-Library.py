#!/usr/bin/env python
# coding: utf-8

# # Majorly Used Charts and plots are described below
# ### 1> Line_plot
# ### 2> Bar_chart
# ### 3> Histogram_plot
# ### 4> Scatter_plot
# ### 5> Pie_chart
# ### 6> Stack/Area_plot ---> not_in_this_notebook

# # Data Visualisation using Matplotlib Library

# ## Importing Some Libraries

# In[2]:


import numpy as np # -->  numpy is matrix data manupulation and math operation library
import pandas as pd # -->  Pandas is data processing and collection library 
from matplotlib import pyplot as plt # -->  Data Visualisation Library


# ## Line plotting using fill_between method to better visualisation

# In[207]:


x = list(np.arange(0,100))
w = [i*2 for i in x]
a = [i*3 for i in x]
b = [i*4 for i in x]
d = [np.log(i+1) for i in x]
plt.style.use('seaborn') # -->  style to use | to see available style plt.style.availabel print it 
plt.figure(figsize = (16,5)) # --> figsize indicates figure size best is (16 , 5)
plt.plot(x , a , label = 'x*3')
plt.plot(x , b ,  label = 'x*4')
plt.plot(x , w ,  label = 'x*2')
plt.plot(x , d,  label = 'log(x+1)')
plt.xlabel('X------>')
plt.ylabel('Y------>')
plt.title('Fill_Between Method')
plt.ylim(0,200) # -->  setting y axis limit
plt.xlim(0,50) # -->  setting x axis limit
plt.fill_between(x ,a,b  ,label = 'b--->a' ,color = 'green',alpha = 0.5 ) #--> color between b and a line 
plt.fill_between(x ,a,w  ,label = 'a--->w' ,color = 'red',alpha = 0.50 ) # --> same as first one but between a and w
plt.fill_between(x ,d,w  ,label = 'w--->d' ,color = 'blue',alpha = 0.25 )
plt.fill_between(x ,d,0  ,label = 'd--->0' ,color = 'black',alpha = 0.5 )
plt.legend(loc = 'upper left') # --> locs option set location of lables in graph or chart
plt.show()


# ## Data Collection using Pandas

# In[3]:


# shooting.csv is Us shot person data-set 
df = pd.read_csv('shootings.csv')
df.age=df.age.replace(37.11793090137039, 37)
age = list(df['age'])


# ## US Shooting Data Visualisation  using plt and bar chart

# In[4]:


from collections import Counter
count = Counter(age) # --> Counter counts repeat of perticular number or thing
c = count.most_common() # --> will give most-common things list of tuples
#print(c)
ages = []
cts = []
width = 0.50
for i in c:
    ages.append(i[0])
    cts.append(i[1])    
plt.figure(figsize = (16,5))
plt.style.use('ggplot')    
plt.bar(ages , cts , width = width)
plt.title('Count of death -> Ages')
plt.xlabel('Ages')
plt.ylabel('Count of death')
plt.show()


# ## Histograph of above age data

# In[5]:


bins = list(range(0,110,5))
plt.figure(figsize = (16, 5))
plt.style.use('ggplot')
plt.hist(age , bins = bins , edgecolor = 'white' , color = '#ae0001' )
plt.title('Count of death -> Ages (Histogram)')
plt.xlabel('Ages')
plt.ylabel('Count of death')
plt.tight_layout() # --> to give some padding for better view
plt.show()


# ## Scatter plotting

# In[119]:


plt.figure(figsize = (16, 5))
plt.style.use('ggplot')
x = list(np.random.randint(100 , size = 100))
y = list(np.random.randint(1000 , size = 100))
color = list(np.random.randint(100 , size = 100)) #--> different color by their value like percentage or ratio
size = list(np.random.randint(100 , size = 100)) # --> same as color
plt.scatter(x , y , s = size, c = color , cmap = 'Greens', alpha = 0.50, edgecolor = 'black')
cbar = plt.colorbar() #--> scaling of color we have given 
cbar.set_label('Scale') # --> will give measurement scale
plt.xlabel('X------->')
plt.ylabel('Y------->')
plt.title('Scatter Plotting')
plt.show()


# ## Pie Chart

# In[118]:


x = [40,15,10,15,20]
y = [1,2,3,4,5]
explode = [0,0,0.2,0,0] # --> explode will give space from origin by measures given
plt.figure(figsize = (15,6))
plt.pie(x , labels = y , explode = explode ,startangle = 90,shadow = True, autopct = '%1.1f%%' ,wedgeprops ={'edgecolor' : 'black'})
plt.show()
#startangle --> from which anglke pie plot should start
#shadow -->  shadow by default is False 
#autopct -->  to indicates percentages on pie chart


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




