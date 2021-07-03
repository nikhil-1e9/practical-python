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

#
'''
Exercise 2.15: A practical enumerate() example

Recall that the file Data/missing.csv contains data for a stock portfolio, but has some rows with missing data. Using enumerate(), modify your pcost.py program so that 
it prints a line number with the warning message when it encounters bad input.
'''

def portfolio_cost(filename):
    import csv
    
    total = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for rownum, row in enumerate(rows, start=1):
            try:
                shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print(f'Row {rownum}: Couldn\'t convert: {row}')
            
            total += shares * price
        
        return total


cost = portfolio_cost('Data/missing.csv')


