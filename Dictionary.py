#Dictionary {}

MonthConversion = {"Jan":"January","Feb":"February","Mar":"March","Apr":"April"}

print(MonthConversion["Jan"])

#print(MonthConversion["Dec"])

print(MonthConversion.get("Dec","Not a valid Key"))

for x in MonthConversion.values():  
    print(x)

for x,y in MonthConversion.items():
    print(x,y)


"""
January
February
March
April

Jan January
Feb February
Mar March
Apr April
"""

MonthConcersion.pop("Jan") # Remove with key as an arguement

MonthConversion.popitem() # remove last key value pair from Dictionary
