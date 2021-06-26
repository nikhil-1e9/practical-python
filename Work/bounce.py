# bounce.py
#
# Exercise 1.5

height = 100     # Initial height
num_bounces = 0

while num_bounces < 10:
    height *= 3/5
    num_bounces += 1
    print(num_bounces, round(height, ndigits=4))
    
