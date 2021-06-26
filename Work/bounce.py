# bounce.py
#
'''
Exercise 1.5: The Bouncing Ball

A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell. Write a program that prints 
a table showing the height of the first 10 bounces.

Your program should make a table that looks something like this:

1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
'''

# Solution
height = 100     # Initial height
num_bounces = 0

while num_bounces < 10:
    height *= 3/5
    num_bounces += 1
    print(num_bounces, round(height, ndigits=4))
    
