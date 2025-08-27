marks = {
    "sharda":100,
    "priyanka":99,
    "tulsi":98,
    0:"khushi"
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"sharda":99})
print(marks)

#print(marks["sharda1"]) # print Error
#print(marks.get("sharda1")) # print none

my_dict = {"ab" : 34,"cd" : 789 , "ef" : 5.90}
my_dict.copy()
print(my_dict)

my_dict.clear()
print(my_dict)

print(my_dict.popitem("ab"))