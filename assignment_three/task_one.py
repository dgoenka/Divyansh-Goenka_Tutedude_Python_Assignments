def factorial(number):
    product = 1
    multiplier = 2
    while multiplier <= number:
        product *= multiplier
        multiplier += 1
    return product


num = int(input("Enter a number: "))
print(str(num) + "! = " + str(factorial(num)))
