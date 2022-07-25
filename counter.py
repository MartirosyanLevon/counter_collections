from collections import Counter

counter = Counter('Hello')
print(counter)
counter.update('World')
print(counter)
print(counter.most_common(1))

c = Counter([1, 2, 3, 5, 4, 4])
print(c)

#
#
d = 'aaa bbb ccc aaa'.split()
d = Counter(d)
print(d.most_common(3))
