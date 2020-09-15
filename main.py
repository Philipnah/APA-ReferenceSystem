
websiteName = input("Hjemmesidens navn: ")
yearAndLastUpdate = input("('År' 'dato for sidste opdatering af hjemmesiden'): ")

if len(yearAndLastUpdate) == 0:
	yearAndLastUpdate = "u.å."

title = input("Titel: ")
visitDate = input("Hjemmeside besøgt den: ")
url = input("URL: ")

year = yearAndLastUpdate[:4]
yearAndLastUpdate = yearAndLastUpdate[5:]

output = websiteName + ". " + "(" + year + ", " + yearAndLastUpdate + "). " + title + ". Lokaliseret " + visitDate + " på: " + url

print("\n\n" + output + "\n")