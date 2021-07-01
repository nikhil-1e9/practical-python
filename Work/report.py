# report.py
#
# Exercise 1.30
 
# This function takes a filename as input, reads the portfolio data in that file, and returns the total cost of the portfolio as a float.

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
  
  
  # Exercise 2.4
  
  '''In that file, define a function read_portfolio(filename) that opens a given portfolio file and reads it into a list of tuples.
  
