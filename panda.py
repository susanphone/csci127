import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nums = (45, 3, 850, 12)
sounds = {"cow": "moo", "dog": "woof", "pig": "oink", "cat": "meow"}
price = np.array([2000, 50, 300, 1.25], dtype=int)

farm = list(zip(nums, sounds.values(), price))
print(farm)

df = pd.DataFrame(farm)
print(df)

df = pd.DataFrame(farm, columns= ["A", "B", "C"])
print(df)
df = pd.DataFrame(farm, index= ["W", "X", "Y", "Z"], columns=["A", "B", "C"])
print(df)

rows =["Cows", "Dogs", "Pigs", "Cats"]
cols = ["Nums", "Sounds", "Prices"]
df = pd.DataFrame(farm, index=rows, columns=cols)
print(df)

print(df["Nums"].max())
print(df["Nums"].min())

df.plot(kind="bar", grid=True)
plt.show()


df.plot(y="Nums", kind="bar")
plt.show()

df.plot(y="Prices", kind="pie")
plt.show()
