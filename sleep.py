l = [1, 2, 19849, 4, 5, 6]
t = tuple(l)
print(t)
print(len(l))
print(sorted(l, reverse = True))
print(tuple(reversed(t)))
print(sum(t, 1748129847))
print(max(l), min(t))
l2 = list(zip(l, tuple(reversed(t))))
print(l2)