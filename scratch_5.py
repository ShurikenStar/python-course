a=int(input("Enter a number: "))
def fact(a):
    if a<2:
        return 1
    else:
        return fact(a-1)*a
print(f"Factorial of {a} is {fact(a)}")
