Days = set(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
Months = {"Jan", "Feb", "Mar"}
dates = {21, 22, 23}

# print(Days)
# print(Months)
# print(dates)

# Acessing values in a set

for d in Days:
    print(d)

# Adding element to the set - there is no specific index

Days.add("New")
print(Days)

# Removing Item from a Set
Days.discard("New")
print(Days)

# Union of Sets
DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
Alldays = DaysA | DaysB
print(Alldays)

# Intersection of sets
AllDays = DaysA & DaysB
print(AllDays)

# Difference of sets
All_days = DaysA - DaysB
print(All_days)

# Compare sets
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
