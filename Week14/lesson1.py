import pandas as pd
import matplotlib.pyplot as plt
import sys          # to determine Python version number
import matplotlib   # to determine Matplotlib version number

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print()

# Create Data --------------------------

# http://www.onthesnow.com/montana/bridger-bowl/historical-snowfall.html
years = [2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]    # bridger bowl year
total_snowfall = [319, 346, 254, 316, 166, 228, 209, 271, 177, 186]   # inches
largest_snowfall = [16, 20, 25, 20, 14, 14, 21, 20, 15, 21]         # inches

BridgerDataSet = list(zip(years, total_snowfall, largest_snowfall))
print("BridgerDataSet:", BridgerDataSet, "\n")

data = pd.DataFrame(data=BridgerDataSet, columns=["Year", "Total", "Largest"])
print("Bridger DataFrame")
print("-----------------")
print(data)

data.to_csv('bridger.csv', index=False, header=False)

# Get Data -----------------------------

bridger = pd.read_csv('bridger.csv', names=['Year', 'Total', 'Largest'])
print("\nBridger DataFrame after reading csv file")
print("----------------------------------------")
print(bridger)

# Prepare Data -------------------------

if (bridger.Total.dtype == 'int64'):
    print("\nTotal snowfall is of type int64")
else:
    print("\nTotal Snowfall is of type", bridger.Total.dtype)

# Analyze Data -------------------------

sorted_data = bridger.sort_values(['Total']) #, ascending=False)
print("\nSorted Bridger Data Set")
print("-----------------------")
print(sorted_data)

# print("\nThe least total snowfall was", bridger['Total'].min())

# Display Data -------------------------

# bridger.plot(x="Year", y="Largest", kind="bar", color="steelblue")
# plt.xlabel("Year")
# plt.ylabel("Biggest Snow Day")
# plt.show()

# speed = [0.1, 17.5, 40, 48, 52, 69, 88]
# lifespan = [2, 8, 70, 1.5, 25, 12, 28]
# index = ['snail', 'pig', 'elephant', 'rabbit', 'giraffe', 'coyote', 'horse']
# df=pd.DataFrame({'speed':speed, 'lifespan':lifespan}, index=index)
# ax = df.plot.bar(rot=0)
# plt.show()

bridger2 = pd.DataFrame({'total':total_snowfall, 'largest':largest_snowfall}, index=years)
bridger2.plot(kind='bar', grid='True')
plt.show()

col_headers = list(data.columns)
print(col_headers)