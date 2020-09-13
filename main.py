# Eksempel:
# Holten, N. (2008, 20. februar{"u.å.", hvis man ikke har nogen skribent}). Etik. Lokaliseret d. 23. november 2009 på: http://fysio.dk/fafo/Etik/


websiteName = input("Hjemmesidens navn: ")
yearAndLastUpdate = input("år og dato for sidste opdatering af hjemmesiden: ")
title = input("Titel: ")
visitDate = input("Dato for besøg af hjemmesiden: ")
url = input("URL: ")

year = yearAndLastUpdate[:4]
yearAndLastUpdate = yearAndLastUpdate[5:]

output = websiteName + ". " + "(" + year + ", " + yearAndLastUpdate + "). " + title + ". Lokaliseret " + visitDate + "på: " + url

print("\n\n" + output + "\n")