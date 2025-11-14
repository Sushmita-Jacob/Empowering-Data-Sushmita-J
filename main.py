# This code is written in python
# The following is used to add the .csv file to my export
import os
import sys
import pandas as pd
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
csv_path = resource_path("livwell175.csv")
df = pd.read_csv(csv_path)

# The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt

# Read a comma separated values (CSV) files into a variable
lwd_path = resource_path("livwell175.csv")
lwd=pd.read_csv(lwd_path)
#as a pandas DataFrame

# Print out the number of rows and columns
input("The age of consent in India, like many countries, is 18 years old. However, until 2012, teens as young as 16 years old could legally consent to sexual activity. Press enter to continue.\n")
input("Follow the story of Smitha: A 17-year-old girl living with her parents in Kerala, India. She is still in school in the early 200s, before the age of consent was raised. Despite wanting to pursue an art degree, her parents insist on immediately getting married to stay financially stable. Press enter to continue.\n")
input("For context, higher education in Kerala is expensive. Art education is lacking and not as valued in India. Marriages in Kerala traditionally have many rituals that can be expensive. Coming from a low-income background, Smitha's parents chose investing in marriage rather than education. Most people in Kerala are married, but do they truly want to be? Press enter to continue.\n")
input("As shown in the scatterplot, women in India historically got married at a very young age. For some, societal expectations and pressure may play a part to this. For others, like Smitha, they may not have had a choice to stay single. There are many statistics on how many people are married and at what age. However, there is not enough research on the WHY behind those numbers. Press enter to continue.\n")
print("Proposed research question: Why are women/girls in India getting married at a young age?")

# basic colors:
# 'blue', 'green', 'red', 'cyan', 'magneta', 'yellow', 'black', 'white'

# create a scatter plot
oneCountryBooleanList = lwd["country_name"]=="India"
oneCountryData = lwd.loc[oneCountryBooleanList]
plt.scatter(oneCountryData["year"],oneCountryData["DM_age_marr_mean"],color="red")

# add a title to the plot
plt.title("Average Age of Women at Marriage")

# label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Female Average Age at Marriage")

# set the range for the y-axis
plt.xlim(1992, 2007)
plt.ylim(17,19)

# show the plot
plt.show()
