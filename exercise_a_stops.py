stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

stops.append("Edinburgh Waverly"),
stops.insert(0, "Glasgow Queen St"),
stops.insert(3, "Polmont"),
print(stops[5])
stops.remove("Livingston")
# stops.pop(2)
stops.pop(stops.index("Cumbernauld"))
# print(len(stops))
# stops.sort()
# print(stops)
# stops.reverse()

# total_stops = 7

for stop in stops:
    print(stop)
 

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop