import os
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib


print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


# The inital set of baby names and birth rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

# zip two lists together
BabyDataSet = list(zip(names, births))

#What are the different types of data?
print(BabyDataSet)
print(type(BabyDataSet))
print(type(BabyDataSet[0]))
print(type(BabyDataSet[2][0]))
print(type(BabyDataSet[2][1]))
test = zip(names,births)
print(type(test))

#cant print a zip
list(test)

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
print(df)
print(type(df))

df.to_csv('births1880.csv', index=False, header=False)
#Turned of the header
#Add second column of numbered elements(indexed)
location = r"/home/susan/csci127/Week14/births1880.csv"
print(location)
df = pd.read_csv(location, header = None)
#without header bob isn't treated as data
print(df)
df = pd.read_csv(location, names=["Names", "Births"])
#Now there are headers
#Whats the difference between adding a heading while reading 
# the csv instead of making header=True?
print(df)

#this removed the CSV
#DANGEROUS!!!!
os.remove(location)
