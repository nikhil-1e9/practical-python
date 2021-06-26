# mortgage.py
#
# Exercise 1.7
'''
Exercise 1.7: Dave's mortgage
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and 
the monthly payment is $2684.11.
'''
#
# Exercise 1.8
'''
Exercise 1.8: Extra payments
Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.
'''
#
# Exercise 1.9
'''
Exercise 1.9: Making an Extra Payment Calculator
Modify the program so that extra payment information can be more generally handled. Make it so that the user can set these variables:

How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first five years have already been paid?
'''
#
# Exercise 1.10
'''
Exercise 1.10: Making a table
Modify the program to print out a table showing the month, total paid so far, and the remaining principal. The output should look something like this:    

1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
4 10736.44 497581.83
5 13420.55 496970.98
...
308 874705.88 3478.83
309 877389.99 809.21
310 880074.1 -1871.53
Total paid 880074.1
Months 310
'''
# Solution
principal = 500000.0
rate = 0.05
payment = 2684.11
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0

while principal > 0:
    
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        extra_payment = 1000.0
    else:
        extra_payment = 0.0
        
    principal = principal * (1+rate/12) - (payment + extra_payment)

    # Fixing the problem of overpayment occuring in the last month
    if principal < 0:                     
        payment += principal
        principal = 0.0
    
    total_paid += payment + extra_payment
    month += 1
    print(month, round(total_paid, ndigits=2), round(principal, ndigits=2))

print('Total paid', round(total_paid, ndigits=2))
print('Total months', month)


