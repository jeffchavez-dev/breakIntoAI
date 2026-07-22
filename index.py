
spam_amount = 0

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)

# spam_amount = spam_amount + 4
# print(spam_amount)

# if spam_amount > 0:
#     print("My spam amount is too few")

# viking_song = "Spam " * spam_amount
# print(viking_song)

# print(type(spam_amount))
# print(type(19.95))
a = 65
b = 60
# print(a // b)

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
# print("Height in meters =", total_height_meters, "?")

# print(min(5,6,7))
# print(max(5,6,7))

# print("You've successfully run some Python code")
# print("Congratulations!")

# Add parentheses to the following expression so that it evaluates to 0.

8 - 3 * 2 - 1 + 1
print((8 - 3) * (2 - (1 + 1)))

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = -1
total_candies = alice_candies + bob_candies + carol_candies
to_smash = total_candies % 3
# print(to_smash)
# print(alice_candies / 60)

# Lesson 2 - Functions and Getting Help

# help(print)


def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return min(abs(a - b), abs(b - c), abs(c - a))


# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
# )

# print(str(least_difference(1, 10, 100)) + " this is nice")


def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))
"""
print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
"""