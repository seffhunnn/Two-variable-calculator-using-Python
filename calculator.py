#Basic two variable calculator 


a=int(input("Enter your first digit: "))
b=int(input("Enter your second digit: "))

n=input("Enter your preference '+', '-', '/', '*': ")


def add(a,b):
    sum=a+b
    print(sum)
def sub(a,b):
    sub=a-b
    print(sub)
def multiply(a,b):
    multi=a*b
    print(multi)
def divide(a,b):
    div=a/b
    print(div)

if(n=="+"):
    add(a,b)
elif(n=="-"):
    sub(a,b)
elif(n=="*"):
    multiply(a,b)
elif(n=="/"):
    divide(a,b)
else:
    print("Invalid preference")