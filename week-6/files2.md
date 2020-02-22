# Files
### How to use files within programs

#### example 1: Census
        census_file = open("census.txt", "r")

        for one_line in census_file:
            values = one_line.split()
            print("State: " + values[0] + ", Population: " + values[1])
        census_file.close()
#### example 1a: Census Challange
        census_file = open("census.txt", "r")

        total = 0
        for one_line in census_file:
            values = one_line.split()
            total += int(values[1])
        print(total)
        census_file.close()

#### example 2: Student Data:
        f = open("studentdata.txt", "r")

        for aline in f:
            items = aline.split()
            if len(items[1:])>6:
                print(items[0])
        f.close()

#### example 2b: Student Average
        f = open("studentdata.txt", "r")
        for aline in f:
            items = aline.split()
        grades = items[1:]
        
        total = 0
        for grade in grades:
            total += int(grade)
        print(items[0], (total/len(grades))

        f.close()