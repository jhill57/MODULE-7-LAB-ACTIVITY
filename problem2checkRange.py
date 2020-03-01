def numbercheck (x):
    for i in range (10):
        if 0 < x < 11:
            return x, " is in the range."
        else:
            return x, " is not in the range."

number = int(input("What is your number?"))
print (numbercheck(number))

 
