Practical = ["Vishal", "Rajesh","Mahajan"]

print("\nIterating Using Iter")
iterator = iter(Practical)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("\nIterating thorugh Generator")
def generator(Practical):
    for i in Practical:
        yield i

generator_prac = generator(Practical)
print(next(generator_prac))
print(next(generator_prac))
print(next(generator_prac))
