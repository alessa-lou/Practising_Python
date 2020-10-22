def fizz_buzz(input):
    
    if input % 15 == 0:
        return "Fizzbuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(45))