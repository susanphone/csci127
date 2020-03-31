infile = open("grades.csv", "r")    #r is for reading
outfile = open("grades2.csv", "w")    #w is for writing

first = infile.readline()              #remove first line in csv
first = first[:-1]
first += ", Average" 
outfile.write(first)   

ave = 0
for line in infile:
    cells = line.split(",")

    # print(cells)
    print(cells[1], cells[2])

    ave = (int(cells[1]) + int(cells[2]))/2
    print(ave)

    # if line[-1] is '\n':
    #     outline = line[:-1] #what about the 9 at the very end?
    # else:
    #     outline = line
    # outline += ","
    # outline += str(ave)
    # outline += "\n"
    if line[-1] is '\n':
        outline = line.replace('\n', ', ' + str(ave) + '\n')
    else:
        outline = line + ',' + str(ave) + '\n'

    outfile.write(outline)

infile.close()
outfile.close()
    