# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def smaller(a,b):
    if a > b:
        return b
    else:
        return a
        
def set_range(num_one, num_two, num_three):
    max_num = max(num_one, num_two, num_three)
    if num_one == max_num:
        min_num = smaller(num_two, num_three)
    elif num_two == max_num:
        min_num = smaller(num_one, num_three)
    else:
        min_num = smaller(num_one, num_two)
    return max_num - min_num
    # Your code here


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6