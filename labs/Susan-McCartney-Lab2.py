# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Lab 2: Season Checker
# Susan McCartney
# Last Modified: January 23, 2020 
# ---------------------------------------
# Create a program that tells you what season
#it is based on the day and the month
# ---------------------------------------

def main():
    user_month = input("Enter month: ")
    user_day = int(input("Enter day: "))
    season = season_checker(user_month, user_day)

    if season is "Invalid":
        print("That is not a valid date.")
    else:
        print("That's a "+ season + " Day.")

def season_checker(user_month, user_day):
    if user_month in ("February") and user_day >= 1 <= 28:
        return ("Winter")
    if user_month in ("December") and user_day >= 1 <= 31:
        return("Winter")
    if user_month in ("January") and user_day >= 1 <= 31:
        return ("Winter")

    if user_month in ("March") and user_day >= 1 <= 31:
        return ("Spring")
    if user_month in ("April") and user_day >= 1 <= 30:
        return ("Spring")
    if user_month in ("May") and user_day >= 1 <= 31:
        return ("Spring")

    if user_month in ("June") and user_day >= 1 <= 30:
        return ("Summer")
    if user_month in ("July") and user_day >=1 <= 31:
        return ("Summer")
    if user_month in ("August") and user_day >= 1 <= 31:
        return ("Summer")

    if user_month in ("September") and user_day >= 1 <= 30:
        return ("Fall")
    if user_month in ("October") and user_day >= 1 <= 31:
        return ("Fall")
    if user_month in ("November") and user_day >= 1 <= 30:
        return ("Fall")
    
    return "Invalid"

main()
