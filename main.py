# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell175.csv")

# Print out the number of rows and columns
input("The age of consent in India, like many countries, is 18 years old. However, until 2012, teens as young as 16 years old could legally consent to sexual activity. Press enter to continue.\n")
input("Follow the story of Smitha: A 17-year-old girl living with her parents in Kerala, India. She is still in school in the early 2000s, before the age of consent was raised. Despite wanting to pursue an art degree, her parents insist on immediately getting married to stay financially stable. Press enter to continue.\n")
input("For context, higher education in Kerala is expensive. Art education is lacking and not as valued in India. Marriages in Kerala traditionally have many rituals that can be expensive. Coming from a low-income background, Smitha's parents chose investing in marriage rather than education. Most people in Kerala are married, but do they truly want to be? Press enter to continue.\n")
input("As shown in the scatterplot, women in India historically got married at a very young age. For some, societal expectations and pressure may play a part to this. For others, like Smitha, they may not have had a choice to stay single. There are many statistics on how many people are married and at what age. However, there is not enough research on the WHY behind those numbers. Press enter to continue.\n")
print("Proposed research question: Why are women/girls in India getting married at a young age?")

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
oneCountryBooleanList = lwd["country_name"]=="India"
oneCountryData = lwd.loc[oneCountryBooleanList]
plt.scatter(oneCountryData["year"],oneCountryData["DM_age_marr_mean"],color="red" )

# add a title to the plot
plt.title("Average Age of Women at Marriage")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Female Average Age at Marriage")

# set the range for the y-axis
plt.xlim(1992,2007)
plt.ylim(17,19)

# show the plot
plt.show()
