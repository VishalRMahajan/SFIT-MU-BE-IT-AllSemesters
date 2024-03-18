"""
Syntax:
def function_name(argument):
    function code block

function_name(argument) //this is to call the Function
"""

#without argument
def hello():
    print("Hello from a function")
hello()

#with single argument
def my_funtion(fname):
    print(fname+ " SE IT A ")
my_funtion("Vishal")

#with two argument
def my_function(fname,lname):
    print("Hello, My name is ",fname,lname)
my_function("Vishal","Mahajan")


#with n number of argument
def my_function(*details):
    print("I am "+ details[0]+details[1]+details[2]+details[3])
my_function("Vishal"," Rajesh"," Mahajan"," SEITA3")

#with keys assigned with value passed as paramenter
def my_function(name,middle,last):
    print("\nMy first name is "+name)
    print("My middle name is "+middle)
    print("My last name is "+last)
my_function(name="Vishal",middle="Rajesh",last="Mahajan")
