# Selve hjemmesidens navn. (år/seneste opdatering). Titel(udgave). Lokaliseret [besøgsdato] på: URL
# 
# Eksempel:
# Holten, N. (2008, 20. februar{"u.å.", hvis man ikke har nogen skribent}). Etik. Lokaliseret d. 23. november 2009 på: http://fysio.dk/fafo/Etik/


websiteName = input("Website name: ")
yearAndLastUpdate = input("Year & date of latest update: ")
title = input("Title: ")
visitDate = input("Date when website was accessed: ")
url = input("URL: ")

year = yearAndLastUpdate[:4]
yearAndLastUpdate = yearAndLastUpdate[5:]

output = websiteName + ". " + "(" + year + ", " + yearAndLastUpdate + "). " + title + ". Visited on " + visitDate + "at: " + url

print("\n\n" + output + "\n")