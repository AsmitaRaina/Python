Q) Create a calculator function 

def calculator(a,b):
    print("1. Addition \
      2. Subtraction \
    3. Multiplication \
    4. Division")
    n=int(input("Choose your option"))
    if n==1:
        print(a+b)
    elif n==2:
        print(a-b)
    elif n==3:
        print(a*b)
    elif n==4:
        print(a/b)
    
a=int(input("Enter first number"))
b=int(input("Enter second number"))
calculator(a,b)

Q) Create any function with 3-4 parameters

def funct(a,b,c):
    sum=a+b+c
    ans=a*b//c
    print(sum, ans)
funct(2,3,4)

