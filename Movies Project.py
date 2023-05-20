#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# Creating a DataFrame
df1 = pd.read_csv(r"D:\Jupyter\Project\action.csv")
df1


# In[3]:


df2 = pd.read_csv(r"D:\Jupyter\Project\film-noir.csv")
df2


# ## Joining two dataframes

# In[4]:


# Joining two dataframes
df = df1.append(df2, ignore_index = True)
df


# In[5]:


# First 10 rows
df.head(10)


# In[6]:


# Last 10 rows
df.tail(10)


# # Data Cleaning 

# In[7]:


df.info


# In[8]:


# All Column Names
df.columns


# In[9]:


# Total null values in each column
df.isnull().sum()


# In[10]:


# Total dup5licate values in each column
df.duplicated().sum()


# In[11]:


# Dropping rows having all values as null
df.dropna(how="all")


# In[12]:


# Filling Null Values

df["certificate"].fillna("None", inplace = True)
df["runtime"].fillna("Unknown", inplace = True)
df["director"].fillna("Unknown", inplace = True)
df["star"].fillna("Unknown", inplace = True)
df["gross(in $)"].fillna("Unknown", inplace = True)
df


# In[13]:


# Feeding null values of 'rating' column as mean of the same column
df["rating"].fillna(df.rating.mean(), inplace = True)

# Limiting the number of decimals
df = df.round(decimals = 2)
df


# In[14]:


# Feeding null values of 'votes' column as mean of the same column
df["votes"].fillna(df.votes.mean(), inplace = True)

# Limiting the number of decimals
df = df.round(decimals = 1)
df


# In[15]:


# Dropping unnecessary columns
df.drop(columns = ["director_id","star_id","certificate","gross(in $)"],inplace = True)
df


# # Data Analysis 

# In[16]:


# Fetching all columns from row 10000 to 10009
df.iloc[10000:10010]


# In[17]:


# Get Movie Name and decription at location 10009
df.loc[10009,["movie_name","description"]]

# It can be noted that the entire decription is not displayed


# In[18]:


# Display the long string with the given size
pd.options.display.max_colwidth = 10000
df


# In[19]:


# Noted that the entire description is being displayed in row 128
df.loc[128,["movie_name","description"]]


# In[20]:


df.columns


# In[21]:


# Renaming columns 
df.rename(columns = {"movie_id" : "Movie ID", "movie_name" : "Movie Name", "year" : "Year", "runtime" : "Runtime", 
                     "rating" : "Ratings", "description" : "Description", "votes" : "Votes"}, inplace = True)
df


# In[22]:


# Splitting columns
df[["Genre1", "Genre2", "Genre3"]] = df.genre.str.split(",", expand = True)
df


# In[23]:


# Since splitting a column created new columns but the previous one still exists, so lets remove the old column
df.drop(columns = ["genre"], inplace = True)


# In[24]:


df


# In[25]:


df.columns


# In[26]:


# Rearranging columns
df = df.reindex(columns = ['Movie ID', 'Movie Name', 'Year', 'Genre1', 'Genre2', 'Genre3', 'Runtime', 'Ratings', 'Description',
       'director', 'star', 'Votes'])
df


# In[27]:


# Renaming columns
df.rename(columns = {"director" : "Director(s)", "star" : "Stars"}, inplace = True)
df


# ## Name and Description of top 5 voted movies

# In[28]:


# Top 5 values from Votes column
a = df.nlargest(5,"Votes")
a[["Movie Name","Description"]]


# ## Name and Description of bottom 5 voted movies

# In[29]:


# Last 5 values from Votes column
b = df.nsmallest(5,"Votes")
b[["Movie Name","Description"]]


# ## Name and Year of top 10 rated movies 

# In[30]:


# Last 10 values from Ratings column
x = df.nlargest(10,"Ratings")
x[["Movie Name","Year"]]


# ## Name and Year of bottom 5 voted movies

# In[31]:


# Top 10 values from Ratings column
y = df.nsmallest(10,"Ratings")
y[["Movie Name","Year"]]


# In[32]:


# No. of unique values in Director column
df["Director(s)"].nunique()


# In[33]:


# Unique values in Stars column
df["Stars"].unique()


# In[34]:


# No. of unique values in Stars column
df["Stars"].nunique()


# In[35]:


# Sort Ratings and Votes column in descending order
z = df.sort_values(["Ratings","Votes"], ascending = [False,False])
z[["Movie Name"]]


# ## Movie Name and Genre 1 having ratings less than 2 

# In[36]:


df[["Movie Name","Genre1"]].loc[df["Ratings"] < 2.0]


# ## Create a New Column 'Recommendations' 

# In[37]:


df["Recommendations"] = np.nan
df


# In[38]:


df.loc[(df.Ratings >= 7.0), "Recommendations"] = "Best Recommended"
df.loc[((df.Ratings < 7.0) & (df.Ratings >= 5.0)), "Recommendations"] = "Recommended"
df.loc[((df.Ratings < 5.0) & (df.Ratings >= 2.0)), "Recommendations"] = "Average Recommended"
df.loc[(df.Ratings < 2.0), "Recommendations"] = "Not Recommended"
df


# In[39]:


df.loc[df["Ratings"] < 2.0]


# ## Movie Name where Genre 1 is Action 

# In[40]:


df["Movie Name"].loc[df["Genre1"] == "Action"]


# ## Movie Name where Year is 2022 

# In[41]:


df["Movie Name"].loc[df["Year"] == "2022"]


# ## Movie Name which starts with 'The' 

# In[42]:


df["Movie Name"].loc[df["Movie Name"].str.startswith("The")]


# ## Movie Name where Genre1 ends with 'dy'

# In[43]:


df["Movie Name"].loc[df["Genre1"].str.endswith("dy")]


# In[44]:


# Since we have splitted one genre column into three, not every row had 3 genres, so rest of the columns might have null values
df["Genre2"].isnull().sum()


# In[45]:


df["Genre3"].isnull().sum()


# In[46]:


# Filling those Null values in Genre2 and Genre3
df["Genre2"].fillna("None", inplace = True)
df["Genre3"].fillna("None",inplace = True)
df


# In[47]:


# It can be noted that now there arent any null values
df["Genre2"].isnull().sum()


# In[48]:


df["Genre3"].isnull().sum()


# ## Movie Name, Description and Year where recommendations starts with 'Best'

# In[49]:


df[["Movie Name","Description","Year"]].loc[df["Recommendations"].str.startswith('Best')]


# ## Movie Name where ratings is more than 5, runtime is equal 100 mins and year is 2020 

# In[50]:


df[["Movie Name"]].loc[(df.Ratings > 5.0) & (df.Runtime == '100 min') & (df.Year == '2020')]


# In[51]:


# Range of Index
df.index


# In[52]:


df.set_index("Year")


# In[53]:


# Counts the Number of occurences of a particular value
df["Movie Name"].value_counts()


# In[54]:


df.loc[df["Movie Name"] == "Hero"]


# ## Checking if a movie is present in the column

# In[55]:


for x in df["Movie Name"]:
    if x == "Sholay":
        print(df[["Movie Name","Ratings","Description","Year","Runtime"]].loc[df["Movie Name"] == "Sholay"])


# In[56]:


for x in df["Movie Name"]:
    if x == "Titanic":
        print(df[["Movie Name","Ratings","Description","Year","Runtime"]].loc[df["Movie Name"] == "Titanic"])


# In[57]:


for x in df["Movie Name"]:
    if x == "Goblin":
        print(df[["Movie Name","Ratings","Description","Year","Runtime"]].loc[df["Movie Name"] == "Goblin"])
        


# In[58]:


df.describe()


# In[59]:


x = df.groupby("Recommendations")


# In[60]:


x.count()


# In[61]:


x.sum()


# In[62]:


df


# In[63]:


df = df.drop(14465)


# ## Data Visualization 

# In[64]:


a = df.sort_values(["Ratings"], ascending = False)
a


# In[65]:


x = a["Movie Name"].head(30)
y = a["Ratings"].head(30)


# In[66]:


import matplotlib.pyplot as plt


# In[67]:


# LINEPLOT

plt.plot(x,y,color = "Maroon", linewidth = 5)
plt.xlabel("Name of the Movie", font = "Times New Roman", size = 15, color = "olive")
plt.ylabel("Ratings", font = "Times New Roman", size = 15,color = "olive")
plt.title("Top 30 Rated Movies", font = "Times New Roman", size = 25,color = "blue")
plt.xticks(rotation = 90)
plt.show()


# In[68]:


x = a["Movie Name"].tail(30)
y = a["Ratings"].tail(30)


# In[69]:


# SCATTERPLOT

plt.plot(x,y,color = "orange", linewidth = 5 )
plt.xlabel("Name of the Movie", font = "Times New Roman", size = 15, color = "red")
plt.ylabel("Ratings", font = "Times New Roman", size = 15,color = "red")
plt.title("Bottom 30 Rated Movies", font = "Times New Roman", size = 25,color = "purple")
plt.xticks(rotation = 90)
plt.show()


# In[70]:


s = df.loc[df.Year == '2022']
s


# In[71]:


# HISTOGRAM

x = s["Movie Name"]
y = s.Ratings
plt.title("Movies in Year 2022", font = "Times New Roman", size = 25,color = "Hotpink")
plt.hist(y, bins = 15, edgecolor = "black")
plt.show()


# In[72]:


r = df.query("(Recommendations == 'Average Recommended') & (Year == '2015')")
r


# In[73]:


a = r["Movie Name"].iloc[0:30]
b = r["Ratings"].iloc[0:30]

c = r["Movie Name"].iloc[31:60]
d = r["Ratings"].iloc[31:60]


# In[74]:


# SUBPLOT

plt.subplot(2,1,1)
plt.bar(a,b, color = "#D2B48C")
plt.xlabel("Movie Name", color = "red")
plt.ylabel("Ratings",color = "red")
plt.title("0:16")
plt.xticks(rotation = 90)
plt.show()

plt.subplot(2,1,2)
plt.bar(a,b, color = "#FBDD7E")
plt.xlabel("Movie Name", color = "red")
plt.ylabel("Ratings",color = "red")
plt.title("16:30")
plt.xticks(rotation = 90)
plt.show()


# In[75]:


h = df.loc[df["Genre1"] == "Horror"]
a = h["Movie Name"] 
b = h.Ratings

plt.pie(b, autopct = '%1.2f%%')
plt.title("Movies with Ratings having Genre 1 as Horror", font = "Times New Roman", size = 15, color = "#580F41")
plt.legend(labels = a, bbox_to_anchor = (2.5,1.0))
plt.show()


# In[76]:


df.Votes.nlargest()


# In[77]:


s = df.loc[df.Genre1 == 'War']


# In[78]:


# SCATTERPLOT

x = s["Movie Name"]
y = s.Ratings
plt.title("Movies with Genre1 as War", font = "Times New Roman", size = 25,color = "olive")
plt.scatter(x,y,c = "maroon", s = 100, alpha = 0.5)
plt.xticks(rotation = 90)
plt.xlabel("Movie Names", color = "brown", font = "Times New Roman", size =20)
plt.ylabel("Ratings", color = "brown", font = "Times New Roman", size =20)
plt.show()


# In[79]:


a = df.query("(Genre1 == 'Drama') & (Year == 1950)")


# In[80]:


x = a["Movie Name"]
y = a.Ratings

# HORIZONTAL BARGRAPH

plt.barh(x,y,color = "olive", linewidth = 3, alpha = 0.5, height = 0.5)
plt.xlabel("Ratings", font = "Times New Roman", size = 15, color = "red")
plt.ylabel("Name of the Movie", font = "Times New Roman", size = 15,color = "red")
plt.title("Drama Movies in 1950", font = "Times New Roman", size = 25,color = "Brown")
plt.xticks(rotation = 90) 
plt.xlim(5,9)
plt.show()


# In[81]:


df


# In[82]:


import seaborn as sns


# In[83]:


sns.set_style("darkgrid")


# In[84]:


a = df.loc[df.Year == '2000']


# In[85]:


# HISTPLOT

sns.displot(data = a, x = "Ratings", hue = "Recommendations")
plt.title("Movies in year 2000", font = "Times New Roman", size = 20,color = "Green")
plt.show()


# In[86]:


b = df.query("(Runtime == '150 min') & (Year == '2017')")
b


# In[87]:


# LINEPLOT

sns.lineplot(data = b, y = "Ratings", x = "Movie Name",hue = "Recommendations", palette = "dark", marker = "o")
plt.xticks(rotation = 90)
plt.title("Movies in year 2017 having runtime as 150 mins:", font = "Times New Roman", size = 15,color = "Maroon")
plt.show()


# In[88]:


# COUNTPLOT

count = sns.countplot(data = df, x = "Recommendations", palette = "Set2")
plt.xticks(rotation = 45)
plt.title("Count of Recommendations", font = "Times New Roman", size = 20,color = "Maroon")
for label in count.containers:
    count.bar_label(label)
plt.show()


# In[89]:


a = df.query("(Genre1 == 'Crime') ")

# KDE

sns.displot(data = a, x = "Ratings", hue = "Recommendations", kind = "kde", palette = "magma", fill = True) 
plt.title("Genre 1 as Crime", font = "Times New Roman", size = 20,color = "Black")
plt.show()

