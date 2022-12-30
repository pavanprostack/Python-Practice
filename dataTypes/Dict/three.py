
# How to append or add item to dict.

data={"name":"pavan", "sal":45000, "age":25}

data["gender"]="Male"

print(data)

# or

emp={'name': 'pavan', 'sal': 45000, 'age': 25, 'gender': 'Male'}

emp.update({"status":"good"})
print(emp)
