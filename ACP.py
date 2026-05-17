limit = int(input("Enter a number: "))

odd_numbers = [x for x in range(limit) if x % 2 != 0]

print(f"Odd numbers under {limit}: {odd_numbers}")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print(f"Updated:  {capitalized_fruits}")