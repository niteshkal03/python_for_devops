# emp_name = ["aman", "SHIVAM", "shubham"]
# res=[n.lower() for n in emp_name]
# res=[n.upper() for n in emp_name]
# res=["-".join(n) for n in emp_name]

# print(res)

fruits_list=["apple", "mango", "papaya", "banana", "orange", "grapes"]
user="p"
#first method
res = [i for i in fruits_list if user in i]
print(res)

#second method
res = [i.upper() for i in fruits_list if user in i]
print(res)

#old Method
# for i in fruits_list:
#     print(i)
#     if "n" in i:
#         print(i)