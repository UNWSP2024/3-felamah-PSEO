# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%.
# Write a program the inputs the type of hot dog wanted and optional toppings.
# The program then displays the hot dog cost, tax and total cost.

#Author: Faith Lamah
#Date: 18 September 2025
#Hot Dog

hot_dog = 3.50
chili_dog = 4.50
cheese = .50
peppers = .75
grilled_onions = 1.00

type = input('What type of hot dog do you want? (Hot Dog or Chili Dog)')
if type == 'Hot Dog' or type == 'hot dog':
    cost = hot_dog
    toppings = input('What additional toppings do you want? (cheese, peppers, grilled onions)')
    if toppings == 'cheese':
        cost = hot_dog + cheese
        tax = cost * .07
        print(f'The hot dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost-tax:.2f}')
    elif toppings == 'cheese, peppers' or toppings == 'cheese,peppers' or toppings == 'cheese peppers':
        cost = hot_dog + cheese + peppers
        tax = cost * .07
        print(f'The hot dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'cheese, peppers, grilled onions' or toppings == 'cheese,peppers,grilled onions' or toppings == 'cheese peppers grilled onions':
        cost = hot_dog + cheese + peppers + grilled_onions
        tax = cost * .07
        print(f'The hot dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'grilled onions' or toppings == 'Grilled onions':
        cost = hot_dog + grilled_onions
        tax = cost * .07
        print(f'The hot dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'peppers' or toppings == 'Peppers':
        cost = hot_dog + peppers
        tax = cost * .07
        print(f'The hot dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'peppers, grilled onions' or toppings == 'peppers grilled onions':
        cost = hot_dog + peppers + grilled_onions
        tax = cost * .07
        print(f'The hot dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'cheese, grilled onions' or toppings == 'cheese grilled onions':
        cost = hot_dog + cheese + grilled_onions
        tax = cost * .07
        print(f'The hot dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    else:
        print('Please enter a valid input.')


if type == 'Chili Dog' or type == 'chili dog':
    cost = chili_dog
    toppings = input('What additional toppings do you want? (cheese, peppers, grilled onions)')
    if toppings == 'cheese':
        cost = chili_dog + cheese
        tax = cost * .07
        print(f'The chili dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is &{cost - tax:.2f}')
    elif toppings == 'cheese, peppers' or toppings == 'cheese,peppers' or toppings == 'cheese peppers':
        cost = chili_dog + cheese + peppers
        tax = cost * .07
        print(f'The chili dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'cheese, peppers, grilled onions' or toppings == 'cheese,peppers,grilled onions' or toppings == 'cheese peppers grilled onions':
        cost = chili_dog + cheese + peppers + grilled_onions
        tax = cost * .07
        print(f'The chili dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'grilled onions' or toppings == 'Grilled onions':
        cost = chili_dog + grilled_onions
        tax = cost * .07
        print(f'The chili dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'peppers' or toppings == 'Peppers':
        cost = chili_dog + peppers
        tax = cost * .07
        print(f'The chili dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'peppers, grilled onions' or toppings == 'peppers grilled onions':
        cost = chili_dog + peppers + grilled_onions
        tax = cost * .07
        print(f'The chili dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    elif toppings == 'cheese, grilled onions' or toppings == 'cheese grilled onions':
        cost = chili_dog + cheese + grilled_onions
        tax = cost * .07
        print(f'The chili dog is ${cost}')
        print(f'The tax is ${tax: .2f}')
        print(f'The total is ${cost - tax:.2f}')
    else:
        print('Please enter a valid input.')


