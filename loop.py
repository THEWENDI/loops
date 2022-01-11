
for x in range(0,151):
    print(x)

for mul5 in range(5,1000,5):
    print(mul5)

for dojo in range(1,101):
    if dojo % 10 == 0:
        print("Coding Dojo")
    elif dojo % 5 == 0:
        print("Coding")
    else:
        print(dojo)

oddsum = 0 
for odd in range(1,500000,2):
    oddsum = oddsum + odd
print(oddsum)

for num in range(2018,0,-4):
    print(num)

lownum = 2
highnum = 9
mult = 3

for f in range(lownum, highnum + 1):
    if f % mult == 0:
        print(f)