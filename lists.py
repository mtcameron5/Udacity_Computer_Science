def find_element(list, target):
    index = 0
    for x in list:
        if x == target:
            return index
        index += 1
    return -1


def find_element(list_example, target_string):
    if target_string in list_example:
        return list_example.index(target_string)
    else:
    	return -1