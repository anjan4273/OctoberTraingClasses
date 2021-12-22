# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]
Even = []; odd = []
for i in seq:
    if i % 2 != 0:
        Even.append(i)
    else:
        odd.append(i)
print(Even)
print(odd)
exit(1)


# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
