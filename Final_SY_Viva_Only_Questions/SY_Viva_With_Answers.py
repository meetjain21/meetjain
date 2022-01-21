#!/usr/bin/env python
# coding: utf-8

# # SY Viva
# 
# - Name
# - Division
# - Roll Number
# 
# ## Instructions
# 1. Answer the two questions below by 4:45 pm
# 2. Upload your work to Github by 4:50 pm. No submissions uploaded after 4:40 pm will be reviewed.
# 3. Invite the following collaborators to the Github Repo: jjadvani01, zoshuateaching, sheamehta, DishaVasa
# 4. Submit a link to your Github repository on Google Classroom. 
# 5. Once completed, raise your hand on Zoom 
# 6. You will be sent to a breakout room for 5 minutes to explain your solution. Your TA will ask you to explain the code you have written. All you need to do is to explain what each line of code does. During the meeting, the TA will not tell you if you are correct or wrong. They will only take notes on your answers. 
# 7
# . Once your Viva is completed, you may feel free to drop off the call. 

# # Part 1: Do Not Touch

# In[4]:


# DO NOT DELETE: Import the Pandas, Seaborn, and Matplotlib Packages
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


# DO NOT DELETE: Print all rows of all dataframes
pd.set_option('display.max_rows', None)
pd.options.display.float_format = "{:,.2f}".format


# # Part 2: Importing the Data

# In[12]:


# Import the "Australian_Grocery_Store_Data_2017.csv" and save it as a dataframe called trans_df
trans_df = pd.read_csv('Australian_Grocery_Store_Data_2017.csv')

# Print the first 5 rows of trans_2017_df. You should see dates from the year 2017 present
trans_2017_df = trans_df.head(5)


# In[13]:


# Create and print a variable called "total_rows" that tells us How many rows in total are present in trans_df
total_rows = trans_df.count
print (total_rows);


# # Part 3: Adding Arithmetic Columns

# In[17]:


# Add a column called "total_buying_price" (Formula: unit_buying_price * quantity)
buying = trans_df.unit_buying_price * trans_df.quantity;
trans_df['total_buying_price'] = buying;


# Add a column called "total_selling price" (Formula: unit_selling_price * quantity)
selling = trans_df.unit_selling_price * trans_df.quantity;
trans_df['total_selling_price'] = selling;


# Add a column called "total_margin" (Formula: unit_price_margin * quantity)
total = trans_df.unit_selling_price * trans_df.quantity;
trans_df['total_selling_price'] = selling;

# Print the first 5 rows of trans_df to show that these columns have been added


# # Part 4: High Level Item Analysis

# In[ ]:


# Using the Group By and Agg Pandas Functions
# Create a dataframe using "trans_df" called "items_df" that has the following columns:
    # item_name
    # unit_buying_price (Mean of Unit Buying Price)
    # unit_selling_price (Mean of Unit Selling Price)
    # unit_price_margin (Mean of Unit Price Margin)
    # quantity (Sum of Quantity)
    # investment (Sum of Total Buying Price)
    # revenue (Sum of Total Selling Price)
    # profit (Sum of Total Margin)
    


# Print the top 20 items in items_df by the profit column in ascending order


# # Part 5: Filtering

# In[ ]:


# DO NOT DELETE THIS LINE
# Reset the index of items_df 
items_df = items_df.reset_index()


# In[14]:


# Make a datframe called "high_revenue_df" that has only items that earned a revenue above or equal to 5,000


# Print high_revenue_df in descending order of revenue
high_revenue_df = trans_df.sort_values(by=['revenue'], ascending=False)


# In[ ]:




