def sumoffirst5(num):
    if num == 0 :
        return 0
    else :
        return num + sumoffirst5(num-1)
    
print("\nSum of First 5 natural number is",sumoffirst5(5))


fact_num = int(input("Enter the Number : "))
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print("Factorial of",fact_num,"is",factorial(fact_num))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  

def gcd(num1,num2):
    if num2== 0:
        return num1
    else:
        return gcd(num1,num1 % num2)
    
def lcm(num1,num2):
    return (num1*num2)//gcd(num1,num2)

print("Gcd of",num1,num2,"is",gcd(num1,num2))
print("LCM of",num1,num2,"is",lcm(num1,num2))


def nraisedtox(n,x):
    if x == 0:
        return 1
    else:
        return n * nraisedtox(n,x-1)
    
print(nraisedtox(3,2))