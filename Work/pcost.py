# pcost.py
#
# Exercise 1.27

'''The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding. Write a program that opens this file, 
reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.
'''

total = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        num_shares = int(row[1])
        price = float(row[2][:-1])
        
        total += num_shares * price
        
print(f'Total cost {total}')


