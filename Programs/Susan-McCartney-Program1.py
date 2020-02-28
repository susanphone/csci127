# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: Receipt Cruncher
# Susan McCartney
# Last Modified: February 7, 2020
# --------------------------------------
# Input the item quantity and cost in the
# receipt cruncher and it will tell you
# it that was a cheap, typical, or expensive
# purchase.
# --------------------------------------


def main():
    # input the number of different items purchased
    entries = int(input("How many entries are listed on the reciept? "))

    # set values to zero so they are defined and typed
    totalItems = 0
    totalCost = 0.0
    maxItemCost = 0
    minItemCost = float("inf")
    '''
    The for loop will give user an input option for 
    every entry, the cost of each entry, and add the 
    cost and the number of items together.
    '''
    for i in range(entries):
        entry = i + 1
       
        numberItems = int(input("Enter number of items in entry %d: " % entry))
        entryTotalCost = float(input("Enter that entry's total cost: "))
       
        itemCost = round(entryTotalCost/numberItems, 2)
        totalItems += numberItems
        totalCost += entryTotalCost
        print("Cost per item of entry %d is: %.2f" % (entry, itemCost))
        
        # Check to see if this item is the most or least
        # expensive seen so far.
        if itemCost < minItemCost:  
            minItemCost = itemCost
        if itemCost > maxItemCost:
            maxItemCost = itemCost

    # Prompt the user to enter sales tax.
    tax = float(input("Enter sales tax(%): "))
    
    grandTotal = ((tax/100) * totalCost) + totalCost 
    roundedGrandTotal = round(grandTotal, 2)
    averageCost = (grandTotal / totalItems) 

    print("total cost (with tax): %.2f" % roundedGrandTotal)
    print("total number of items: %d" % totalItems)
    print("average cost per item is %.2f" % averageCost)
    
    rating = get_rating(averageCost, minItemCost, maxItemCost, tax)
    print(rating)

# get_rating calculates and returns the rating for the receipt.
def get_rating(item, lo, hi, tax):
    if item < 3:
        if tax < 2:
            return "That store seems cheap, but it helps that the sales tax is " + str(tax) + "%!"
        return "That store seems cheap"
    if item > 3 and item < 5:
        return "That store seems typical"
    if item > 5:
        if tax > 5:
            return "That store seems expensive, but you could blame that on the " + str(tax) + "% tax."
        return "That store seems expensive"


main()
