num1=[1,2,3]
num2=[4,5,6]
a=list(zip(num1,num2))
print(a)
b=list(zip(num1,num2[::-1]))
print(b)
z={num1:num2 for num1,num2 in zip(num1,num2)}
print(z)