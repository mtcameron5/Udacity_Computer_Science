# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(pence):
    stamps_of_five = 0
    stamps_of_two = 0
    stamps_of_one = 0
    while pence / 5 >= 1:
        pence -= 5 
        stamps_of_five += 1
    while pence / 2 >= 1:
        pence -= 2 
        stamps_of_two += 1 
    while pence >= 1:
        pence -= 1
        stamps_of_one += 1
    return stamps_of_five, stamps_of_two, stamps_of_one