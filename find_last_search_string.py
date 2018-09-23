def find_last(s, target):

    next_target = s.find(target)

    if next_target == -1:
        return - 1

    while next_target != -1:

        x = next_target
        next_target = s.find(target, next_target + 1)

    return x

def find_last(s, t):
	last_pos = -1
	while True:
		pos = s.find(t, last_pos + 1)
		if pos == -1:
			return last_pos 
		last_pos = pos

