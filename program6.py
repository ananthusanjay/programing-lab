n = int(input("enter the num of n terms"))
f1 = 0
f2 = 1
sum = 0
count = 1
print("fibanocci series of n terms",end="")
while(count <= n):
    print(sum, end="")
    count += 1
    f1 = f2
    f2 = sum
    sum = f1 + f2

