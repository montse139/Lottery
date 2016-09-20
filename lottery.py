import random
numbers = []
amount_numbers = []

print "Welcome to the Lottery numbers generator!"
user_numbers = int(raw_input("Please enter the amount of random numbers that you would like to have: "))
for i in range(user_numbers):
    amount_numbers.append(i)
for i in range(1,100):
    numbers.append(i)

print random.sample(numbers, len(amount_numbers))
print "END"# Lottery
