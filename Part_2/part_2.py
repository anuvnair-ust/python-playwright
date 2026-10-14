# Question 6: Function with return value
# Write a function calculate_bill(price, quantity) that returns the total bill amount. If the bill exceeds ₹2,000, apply a 10% discount.
# Example: calculate_bill(500, 5) should return 2250.0.

def calculate_bill(price,quantity):
    amount = price * quantity
    if amount > 2000:
        amount *= 0.9
    return  f"The total amount is: {amount}"


print(calculate_bill(500,5))
print(calculate_bill(667,3))
print(calculate_bill(1999,1))



# Question 7: Lambda function
# Given the list:
# numbers = [12, 5, 18, 7, 24, 9, 30]
# Use lambda function to obtain all numbers multiplied by 3.

numbers = [12, 5, 18, 7, 24, 9, 30]

triple = lambda num: num * 3

triple_list = [triple (num) for num in numbers]

print(triple_list)





# Question 8: Recursion
# Write a recursive function to calculate the factorial of a number.
# Example: factorial(5) returns 120.

def factorial(n):

    if n == 1:
        return 1

    else:
        return n * factorial (n-1)

print(factorial(5))




# Question 9: String processing
# Write a function that accepts a string and returns the number of vowels, consonants, digits, and spaces.
# Example input: "Python 123"
# Expected counts:
# ●	Vowels: 1
# ●	Consonants: 5
# ●	Digits: 3
# ●	Spaces: 1

def string_processing(st):

    vowels = "aeiou"
    st = st.lower()

    count = {
        "Vowels" : 0,
        "Consonants" : 0,
        "Digits"  : 0,
        "Spaces" : 0
    }

    for ch in st :
        if ch in vowels:
            count["Vowels"] += 1
        elif ch.isalpha():
            count["Consonants"] += 1
        elif ch.isdigit():
            count["Digits"] += 1
        elif ch.isspace():
            count["Spaces"] += 1
    return count

print(string_processing("Python 123"))