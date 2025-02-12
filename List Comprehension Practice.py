print("\033c")

# 1st code
n = int(input("Enter an integer: "))

even = [i for i in range(n) if i % 2 == 0]
odd = [j for j in range(n) if j % 2 == 1]

print(f"Even numbers less than {n} are:\n{even}")
print(f"Odd numbers less than {n} are:\n{odd}")

# 2nd code
fruit = ["apple", "banana", "blueberry", "grape", "mango", "orange", "pineapple", "strawberry", "watermelon"]
print(f"Original list:\n{fruit}")

fruitCapital = [k.capitalize() for k in fruit]
print(f"Capitalized list:\n{fruitCapital}")