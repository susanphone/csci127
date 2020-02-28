earthquakes = open("earthquakes.csv", "r")
for magnitude in earthquakes:
    mag = earthquakes.split()
    print(mag)

earthquakes.close()
