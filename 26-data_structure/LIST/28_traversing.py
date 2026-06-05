# marks =[10,23,2,3,43,6,7,44]
# for i in range(len(marks)):
#     print(i)
# marks =[10,11,22,30,40,50,60,70]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(f"This elem is even: {marks[i]}")
#     else:
#         print(f"This elem is odd: {marks[i]}")

marks =[10,11,22,30,40,50,60,70]

# for i in marks:
#     if i%2 == 0:
#         print(f"even: {i}")
#     else:
#         print(f"odd: {i}")
total = 0
for i in marks:
    total=total + i
print(total)

