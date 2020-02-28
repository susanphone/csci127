# -------------------------------------------
# CSCI 127, Lab 6                           |
# February 27, 2020                         |
# Susan McCartney                           |
# -------------------------------------------
# Find the average magnitude of earthquakes |
# using information from a file.            |
# -------------------------------------------

#Functions: 
    #average_magnitude---- calculates and returns average magnitude
    #earthquake_locations--- identifies every unique location in alphabetical order
    #count_earthquakes--- calculate the number of recorded earthquakes with a magnitude greater than or equal to the low bound AND less than or equale to the high bound. 
        #Assume user enters valid numbers.
#Format of the output must match exactly
    #In this sample run, the user inputs 5.0 for the lower bound and 6.0 for the upper bound.
# Spreadsheet columns go A - Q, Need H - Q
#Q-1 P-2 O-3 N-4 M-5 L-6 K-7 J-8 I-9 H-10

#magnitude is J
def average_magnitude(file_name):
    csv = open(file_name, "r")
    total = 0.0
    numLines = 0
    for line in csv:
        items = line.split(",")
        mag = items[-8]
        if mag == "magnitude":
            continue
        numLines += 1
        total += float(mag)
    csv.close()
    return total/numLines


def earthquake_locations(file_name):
    csv = open(file_name, "r")
    locations = []
    for line in csv:
        items = line.split(",")
        name = items[-5]
        if name == "name":
            continue
        if name not in locations:
            locations.append(name)
    
    csv.close()
    locations.sort()
    print("Alphabetical Order of Earthquake Locations")
    print("------------------------------------------")
    for i in range(len(locations)):
        print("%d. %s" % (i+1, locations[i]))

    

def count_earthquakes(file_name, lower_bound, upper_bound):
    csv = open(file_name, "r")
    count = 0
    for line in csv:
        items = line.split(",")
        mag = items[-8]
        if mag == "magnitude":
            continue
        if float(mag) >= lower_bound and float(mag) <= upper_bound:
            count += 1

    csv.close()
    return count

# # The missing functions go here.

# # --------------------------------------


def main(file_name):
    magnitude = average_magnitude(file_name)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))

    earthquake_locations(file_name)
    print("")
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(
        lower_bound, upper_bound, how_many))

# --------------------------------------


main("earthquakes.csv")

# earthquakes.close()
