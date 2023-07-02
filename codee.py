n=int(input("Enter the age:"))
if n<18:
    print("You are a minor")
elif (n>=18 and n<65):
    print("You are an adult")
elif n>=65:
    print("You are a senior")
