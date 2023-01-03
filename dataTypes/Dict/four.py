
# pop()

# it is used to remove item in dict. based on keyname.

data={'name': 'pavan', 'sal': 45000, 'age': 25, 'gender': 'Male', 'status': 'good'}

data.pop("age")
print(data)


# or

# del keyword. 

del data["gender"]  # it deletes single item.
print(data)
