person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# If the key exists in the dictionary, it gets adjusted. If not, it gets added

# print(person)


# print out the name of the second child

# mylist = person["children"]
# print(mylist)

print(person["children"][1])


# print out the name of the cat

print(person["pets"]["cat"])

# use a loop to print out the names of each child
for x in person["children"]:
    print(x)

# use a loop to print out the pets in the following format:
# the type of pet is: dog and the name of the pet is: Fido

pets_dict = person["pets"]

for key, value in pets_dict.items():
    print(f"The type of pet is: {key} and the name of the pet is: {value}")
