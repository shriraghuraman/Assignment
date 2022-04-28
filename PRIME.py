import sympy
sum=0
lst1=[]

for num in range(1,1000):
    if sympy.isprime(num) is True:
        sum+=num
        lst1.append(sum)

print("The sum list 1 is: ",lst1)

lst2=[]
for sum in lst1:
    if sum<1000:
        if sympy.isprime(sum)==True:
            lst2.append(sum)
print("The list 2 is: ",lst2)
print("The required answer is :",max(lst2))