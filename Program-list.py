input_file = "classics.csv"
file = open(input_file, "r")
rank = []
for downloads in file:
    file_list = downloads.split(",")
    most_downloaded = file_list[5]
    book_title = file_list[3]
    key = most_downloaded
    value = book_title
    ranked = {key : value}

    value = ranked.get(key)
    if most_downloaded == "metadata.downloads":
        continue
    try:
        rank.append(int(most_downloaded))
    except ValueError:
        pass #Ignore most_downloaded which are not numbers
    # returned = rank(ranked.keys())
    print(key, value)

    # if bk has higher downloads take that book

    # print(most_downloaded, book_title)
    # print(book_title)
    # print(most_downloaded + "       " + book_title)
file.close()
rank.sort()

