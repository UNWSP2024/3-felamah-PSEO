# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

#Author: Faith Lamah
#Date: 19 September 2025
#Shipping Charges
def weight_conversion(weight):
    # Calculate the shipping charge.

    if weight <= 2:
        shippingCost = weight * 1.50
    elif weight > 2 and weight <= 6:
        shippingCost = weight * 3
    elif weight > 6 and weight <= 10:
        shippingCost = weight * 4
    elif weight > 10:
        shippingCost = weight * 4.75
    ######################
    # WRITE YOUR CODE HERE
    ######################
    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables

    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))