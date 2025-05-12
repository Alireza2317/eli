#nonths name-numbers

year = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

m = input("Insert the 3 letters month's name: ")
print(f"the month {m} is the {year[m]}-th of the year")

m2 = input("Insert the 3 letters for another month's name: ")
diff = year[m2] - year[m]
print(f"there are {abs(diff)} months between them")