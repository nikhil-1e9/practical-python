# report.py
# 
'''
Exercise 1.30: Turning a script into a function

Define a function that takes a filename as input, reads the portfolio data in that file, and returns the total cost of the portfolio as a float.
'''

import csv

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)    # Skip header
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
  
  
'''
Exercise 2.4: A list of tuples
  
Define a function read_portfolio(filename) that opens a given portfolio file and reads it into a list of tuples.
'''

import csv

def read_portfolio(filename):
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)    # Skip header
        for row in rows:
            
            name = row[0]
            nshares = int(row[1])
            price = float(row[2])
            
            portfolio.append((name, nshares, price))
    
    return portfolio
   
   
'''
Exercise 2.5: List of Dictionaries
   
Take the function you wrote in Exercise 2.4 and modify to represent each stock in the portfolio with a dictionary instead of a tuple. In this dictionary use the 
field names of "name", "shares", and "price" to represent the different columns in the input file.
'''
   
import csv

def read_portfolio(filename):
    portfolio_list = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)    # Skip header
        for row in rows:
            portfolio = {}
            
            portfolio['name'] = row[0]
            portfolio['shares'] = int(row[1])
            portfolio['price'] = float(row[2])
            
            portfolio_list.append(portfolio)
    
    return portfolio_list

   
'''
Exercise 2.6: Dictionaries as a container

The file Data/prices.csv contains a series of lines with stock prices. The file looks something like this:

"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
Write a function read_prices(filename) that reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in
the dictionary are the stock prices.
'''

def read_prices(filename):
    stocks = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = row[0]
                price = float(row[1])
            except:
                continue
            
            stocks[name] = price
            
    return stocks
   

'''   
Exercise 2.7: Finding out if you can retire

Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss. These statements should take the list of stocks
in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.
'''

def curr_portfolio(stocks_list, stocks_dict):
    report = [('name', 'shares', 'curr_price', 'change')]
    
    for stock in stocks_list:
        name = stock['name']
        shares = stock['shares']
        price = stock['price']
        curr_price = stocks_dict[name]
        change = curr_price - price
        
        report.append((name, shares, curr_price, round(change, 2)))
        
    return report


#
# Exercises 2.8 to 2.12

def make_report(stocks, prices):
    report = []
    
    for stock in stocks:
        name = stock['name']
        shares = stock['shares']
        price = stock['price']
        curr_price = prices[name]
        change = curr_price - price
        
        report.append((name, shares, '$'+str(curr_price), change))
        
    return report

# Reading the portfolio list and prices dictionary and making report
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

# String Formatting to make a table 
headers = ('Name', 'Shares', 'Price', 'Change')
separators = ('-' * 10 + ' ') * 4
print('%10s %10s %10s %10s' % headers)
print(separators)
for r in report:
    print('%10s %10d %10s %10.2f' % r)

    
