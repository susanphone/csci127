import csv
import numpy as np
import matplotlib.pyplot as plt

# data_path = "spring-2020.csv"
# with open(data_path, "r") as f:
#     reader = csv.reader(f, delimeter=',')
#     headers = next(reader)
#     data = np.array(list(reader)).astype(str)

# print(headers)
# print(data.shape)
# print(data[:1])

  

# data_path = 'spring-2020.csv'
# with open(data_path, 'r') as f:
#     reader = csv.reader(f, delimiter=',')
#     headers = next(reader)
#     data = np.array(list(reader)).astype(str)


# plt.plot(data[:, 0], data[:, 1])
# plt.bar
# plt.axis('equal')
# plt.xlabel("College")
# plt.ylabel("Population")
# plt.show()


csv = open("spring-2020.csv", "r")
file = csv.readlines()
college = []
for line in file:
    items = line.split(",")
    college = items[0]
    print(line)
    ray = np.array(line)
    print(ray)
    

csv.close()


