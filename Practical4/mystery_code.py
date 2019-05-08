# What does this piece of code do?
# Answer: randomly select prime number in range(1,100)

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
    # random n
    n = randint(1,100)
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        # if n can be divided by any smaller number keep going
        if n%i == 0:
            p=False


     
print(n)
