
websiteName = input("Website name: ")
yearAndLastUpdate = input("Year & date of latest update: ")
title = input("Title: ")
visitDate = input("Date when website was retreived: ")
url = input("URL: ")

year = yearAndLastUpdate[:4]
yearAndLastUpdate = yearAndLastUpdate[5:]

output = websiteName + ". " + "(" + year + ", " + yearAndLastUpdate + "). " + title + ". Retrieved " + visitDate + "at: " + url

print("\n\n" + output + "\n")