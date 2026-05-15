#COUNT NUMBER
c = 0
address = "D-1 267/268 MAYUR-VIHAR-PHASE-3 110096"
number = "1234567890"
for i in address:
    if i in number:
        c+=1
print(c)