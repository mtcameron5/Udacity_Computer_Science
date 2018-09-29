def greatest(list_of_numbers):
    if len(list_of_numbers) == 0:
        return 0
        
    number = list_of_numbers[0]
    for i in list_of_numbers:
        if i > number:
            number = i
    return number

