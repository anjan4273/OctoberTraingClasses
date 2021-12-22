def fun(variable):
    letters = ['bang', 'chennai', 'pune', 'hyd', 'delhi']
    if (variable in letters):
        return True
    else:
        return False

sequence = ['pune', 'delhi']

filtered = filter(fun, sequence)
print(list(filtered))
